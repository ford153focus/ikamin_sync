import hashlib
import logging
import mimetypes
import os
import pathlib

import requests
from PIL import Image

import cfg


def process_picture(yml_offer):
    picture = yml_offer.find('picture').text

    if picture is None:
        logging.info(f'#{yml_offer.attrib["id"]} :: no image')
        return

    if pathlib.Path(picture).suffix not in ['jpg', 'png', 'jpeg']:
        logging.info(f'#{yml_offer.attrib["id"]} :: wrong image format')
        return

    vendor_code = yml_offer.find('vendorCode').text
    hashed_vendor_code = hashlib.md5(vendor_code.encode())
    main_img_filename = f'{hashed_vendor_code}.{pathlib.Path(picture).suffix}'
    target = os.path.join(cfg.root_image_path, str(630), str(587), main_img_filename)
    if not os.path.isfile(target):
        r = requests.get(picture, allow_redirects=True)
        open(target, 'wb').write(r.content)

    main_img_size = os.path.getsize(target)
    main_img_mimetype, main_img_encoding = mimetypes.guess_type(target)
    main_img_str = f'{main_img_filename}:{main_img_mimetype}:{main_img_size}:630/587/{main_img_filename}'

    thumb_filename = f'thumb_{hashed_vendor_code}.png'
    thumb_path = os.path.join(cfg.root_image_path, str(630), str(587), thumb_filename)
    image = Image.open(target)
    new_image = image.resize((120, 120))
    new_image.save(thumb_path)
    thumb_image_str = f'{thumb_filename}:image/png:{os.path.getsize(thumb_filename)}:630/587/{thumb_filename}'

    small_filename = f'small_{hashed_vendor_code}.png'
    small_path = os.path.join(cfg.root_image_path, str(630), str(587), small_filename)
    image = Image.open(target)
    new_image = image.resize((240, 240))
    new_image.save(small_path)
    small_image_str = f'{small_filename}:image/png:{os.path.getsize(thumb_filename)}:630/587/{small_filename}'

    return {
        'main': main_img_str,
        'thumb': thumb_image_str,
        'small': small_image_str
    }
