import logging
import os
import sys
import xml.etree.ElementTree as et
import pathlib
import hashlib
import mimetypes

import mysql.connector as mc
import mysql.connector.cursor as mcc
import requests
from PIL import Image

import cfg
import dicts

# logging.basicConfig(filename='/tmp/proxy.log', encoding='utf-8', level=logging.DEBUG)
import lib

logging.basicConfig(level=logging.DEBUG)

connection: mc.MySQLConnection = mc.connect(
    host=cfg.mysql["host"],
    user=cfg.mysql["username"],
    password=cfg.mysql["password"],
    database=cfg.mysql["database"]
)
cursor: mcc.MySQLCursorBufferedDict = connection.cursor(dictionary=True, buffered=True)

def get_param(yml_offer, param_name):
    return yml_offer.find(f'param[@name="{param_name}"]').text


yml_str = open('/home/focus/Downloads/kamin2.ru.xml', 'r', encoding='cp1251').read()
yml_root = et.fromstring(yml_str)
yml_offers = yml_root.findall("shop/offers/offer")

if len(yml_offers) == 0:
    logging.critical("Записей для импорта не нейдено")
    sys.exit(1)

logging.info(f"Прочитано {len(yml_offers)} записей")

# noinspection SpellCheckingInspection,SqlWithoutWhere
cursor.execute("UPDATE `Message57` SET 'Price'=0,'aviable'=0,'Checked'=0")
connection.commit()

for yml_offer in yml_offers:
    if yml_offer.find('model') is None: continue
    if yml_offer.find('vendorCode') is None: continue
    if yml_offer.find('currencyId').text != 'RUR': continue

    vendorCode = yml_offer.find('vendorCode').text

    cursor.execute(f"SELECT * FROM `Message57` WHERE `ItemID`={vendorCode}")
    result = cursor.fetchone()

    if result is not None:
        material = dicts.materials[get_param(yml_offer, 'Материал изготовления')]
        isolation = dicts.isolations[get_param(yml_offer, 'Изоляция, мм')]

        cursor.execute(f"UPDATE `Message57` SET `Price`='{yml_offer.find('price').text}' WHERE `Message_ID`={result['Message_ID']}")
        cursor.execute(f"UPDATE `Message57` SET `aviable`='{yml_offer.attrib['available']}' WHERE `Message_ID`={result['Message_ID']}")
        cursor.execute(f"UPDATE `Message57` SET `Name`='{yml_offer.find('model').text}' WHERE `Message_ID`={result['Message_ID']}")
        cursor.execute(f"UPDATE `Message57` SET `materializgotovleniya`='{material}' WHERE `Message_ID`={result['Message_ID']}")
        cursor.execute(f"UPDATE `Message57` SET `izolyaciyamm`='{isolation}' WHERE `Message_ID`={result['Message_ID']}")
        cursor.execute(f"UPDATE `Message57` SET `diametrmm`='{get_param(yml_offer, 'Диаметр, мм')}' WHERE `Message_ID`='{result['Message_ID']}'")
        cursor.execute(f"UPDATE `Message57` SET `hbmm`='{get_param(yml_offer, 'H, мм')}' WHERE `Message_ID`='{result['Message_ID']}'")
        cursor.execute(f"UPDATE `Message57` SET `dmmm`='{get_param(yml_offer, 'd, мм')}' WHERE `Message_ID`='{result['Message_ID']}'")
        cursor.execute(f"UPDATE `Message57` SET `h1mm`='{get_param(yml_offer, 'h, мм')}' WHERE `Message_ID`='{result['Message_ID']}'")
        cursor.execute(f"UPDATE `Message57` SET `wxbmm`='{get_param(yml_offer, 'WxB, мм')}' WHERE `Message_ID`='{result['Message_ID']}'")
        cursor.execute(f"UPDATE `Message57` SET `massakg`='{get_param(yml_offer, 'Масса, кг, мм')}' WHERE `Message_ID`='{result['Message_ID']}'")
        cursor.execute(f"UPDATE `Message57` SET `naruzhnyjdymohod`='{get_param(yml_offer, 'Наружный контур дымохода, мм')}' WHERE `Message_ID`='{result['Message_ID']}'")
        cursor.execute(f"UPDATE `Message57` SET `tolnaruzhnogokonturamm`='{get_param(yml_offer, 'Толщина наружного контура, мм')}' WHERE `Message_ID`='{result['Message_ID']}'")
        cursor.execute(f"UPDATE `Message57` SET `Currency`='1' WHERE `Message_ID`='{result['Message_ID']}'")
        cursor.execute(f"UPDATE `Message57` SET `Checked`='1' WHERE `Message_ID`='{result['Message_ID']}'")

        img = lib.process_picture(yml_offer)

        cursor.execute(f"UPDATE `Message57` SET `Image`='{img['main']}' WHERE `Message_ID`='{result['Message_ID']}'")
        cursor.execute(f"UPDATE `Message57` SET `ImageThumb`='{img['thumb']}' WHERE `Message_ID`='{result['Message_ID']}'")
        cursor.execute(f"UPDATE `Message57` SET `ImageSmall`='{img['small']}' WHERE `Message_ID`='{result['Message_ID']}'")

        connection.commit()
    else:
        vendor_id = dicts.vendors[yml_offer.find('vendor').text]
        img = lib.process_picture(yml_offer)

        fuel = get_param(yml_offer, "Вид топлива")
        if fuel is None: fuel = get_param(yml_offer, "Топливо")
        fuel_id = dicts.fuels[fuel]

        style = get_param(yml_offer, "Стиль")
        style_id = dicts.styles[style]

        material_id = dicts.materials[get_param(yml_offer, 'Материал изготовления')]
        isolation_id = dicts.isolations[get_param(yml_offer, 'Изоляция, мм')]

        insert_values = [
            '`User_ID`="11"',
            '`Sub_Class_ID`="587"',
            '`Priority`="1"',
            '`Subdivision_ID`="630"',
            '`Subdivision_ID`="11"',
            '`Currency`="1"',
            f'`ItemID`="{yml_offer.find("vendorCode").text}"',
            f'`Name`="{yml_offer.find("model").text}"',
            f'`Price`="{yml_offer.find("price").text}"',
            f'`aviable`="{get_param(yml_offer, "available")}"',
            f'`Vendor`="{vendor_id}"',
            f'`Image`="{img["main"]}"',
            f'`ImageThumb`="{img["thumb"]}"',
            f'`ImageSmall`="{img["small"]}"',
            f'`Details`="{get_param(yml_offer, "Полное описание")}"',
            f'`Width`="{get_param(yml_offer, "Ширина, см")}"',
            f'`Height`="{get_param(yml_offer, "Высота, см")}"',
            f'`Weight`="{get_param(yml_offer, "Вес, кг")}"',
            f'`Depth`="{get_param(yml_offer, "Глубина, см")}"',
            f'`Power`="{get_param(yml_offer, "Мощность, кВт")}"',
            f'`ChimneyDiameter`="{get_param(yml_offer, "Диаметр дымохода, мм")}"',
            f'`Efficiency`="{get_param(yml_offer, "КПД, %")}"',
            f'`HeatedVolume`="{get_param(yml_offer, "Отапливаемый объем, м3")}"',
            f'`diametrmm`="{get_param(yml_offer, "Диаметр, мм")}"',
            f'`hbmm`="{get_param(yml_offer, "Изоляция, мм")}"',
            f'`dmmm`="{get_param(yml_offer, "H, мм")}"',
            f'`h1mm`="{get_param(yml_offer, "d, мм")}"',
            f'`wxbmm`="{get_param(yml_offer, "h, мм")}"',
            f'`massakg`="{get_param(yml_offer, "WxB, мм")}"',
            f'`naruzhnyjdymohod`="{get_param(yml_offer, "Масса, кг")}"',
            f'`tolnaruzhnogokonturamm`="{get_param(yml_offer, "Наружный контур дымохода")}"',
            f'`Fuel`="{fuel_id}"',
            f'`Style`="{style_id}"',
            f'`materializgotovleniya`="{material_id}"',
            f'`izolyaciyamm`="{isolation_id}"',
        ]

        insert_values2 = {}

        sub_id = dicts.subdivisions[yml_offer.find("categoryId").text]
        cat_id = dicts.catalogue_mapper[sub_id]
        insert_values2['Subdivision_ID']=cat_id[0]

        if isinstance(cat_id[1], dict):
            insert_values2 = {**insert_values2, **cat_id[1]}
    pass
