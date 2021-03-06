# noinspection SpellCheckingInspection

materials = {
    'нержавеющая сталь': 1,
    'сталь': 2,
    'искусственный камень': 3,
    'натуральный камень': 4,
    'мрамор': 5,
    'дерево': 6,
    'изразцы': 7,
    'оцинкованная сталь': 8,
    'нержавеющая сталь/оцинкованная сталь': 9,
}

isolations = {
    'без изоляции': 1,
    '50': 2,
    '100': 3,
}

vendors = {
    'Aito': 4,
    'Ala': 5,
    'Allos International Co': 6,
    'Argemi': 8,
    'Arkiane': 9,
    'Arriaga': 3,
    'Art World': 50,
    'Axis': 10,
    'Biokaitra': 68,
    'Brothers': 11,
    'Cashin': 57,
    'Coavantia': 63,
    'Concept Feuer': 65,
    'Continental': 51,
    'Crumar': 12,
    'DMO': 64,
    'Dimplex': 59,
    'Dixneuf': 13,
    'Don-Bar': 14,
    'EIMA & Aquarelia': 16,
    'EdilKamin': 1,
    'Ferguss': 61,
    'Ferlux': 17,
    'Fugar': 18,
    'Gonzyroc': 48,
    'Hark': 47,
    'Hart': 20,
    'Heda/Keddy': 28,
    'Helo': 22,
    'Hergom': 23,
    'J. Corradi': 25,
    'Kastor': 27,
    'Keddy': 28,
    'Kerkes': 54,
    'Kota': 29,
    'LSM': 30,
    'Larearte': 52,
    'Liseo Castiron': 72,
    'Liseo': 55,
    'Megaprom': 62,
    'Narvi': 32,
    'Nestor Martin': 15,
    'NunnaUuni': 33,
    'Palazzetti': 60,
    'Plamen': 70,
    'Richard Le Droff': 35,
    'Rockwool': 36,
    'STAV': 73,
    'Sergio Leoni': 38,
    'Sideros': 39,
    'Skamol': 40,
    'Sotomar': 41,
    'Sunday': 56,
    'Supra': 42,
    'Supra-Russia': 66,
    'Thorma': 43,
    'Traforart': 44,
    'Tubest': 45,
    'TyloHelo': 71,
    'Wekos': 67,
    'World Kamin': 53,
    'Вулкан': 46,
    'Ками': 69,
}

fuels = {
    'дрова': 1,
    'пеллеты': 3,
    'этанол': 5,
    'электричество': 2,
    'брикеты': 7,
    'газ': 4,
    'Газ': 4,
    'Древесный уголь': 8,
    'дрова, около 30 см': 1,
    'дрова, не более 40 см': 1,
    'Дрова. Газ, биоэтанол - по запросу.': "1,4,5",
    'дрова, макс. 50 см': 1,
    'дрова, макс. 65 см': 1,
    'Дрова': 1,
}

styles = {
    'кантри': 2,
    'модерн': 1,
    'классика': 5,
}

subdivisions = {
    3173: 118,
    3205: 429,  # Аксессуары->Аксессуары для барбекю
    3174: 268,  # Аксессуары->Быки, подставки для дров
    3175: 270,  # Аксессуары->Ведра для угля
    3176: 255,  # Аксессуары->Дверцы для каминов и печей
    3177: 255,  # Аксессуары->Дверцы зольников, печей для выпечки
    3178: 266,  # Аксессуары->Декорирующие элементы
    3179: 438,  # Аксессуары->Деревянные кадкиnull, ковши
    3180: 264,  # Аксессуары->Дровницы, тележки, корзины
    3181: 256,  # Аксессуары->Духовые шкафы
    3182: 257,  # Аксессуары->Задвижки, зольные коробки, кладочные втулки
    3183: 263,  # Аксессуары->Каминные и печные наборы
    3184: 269,  # Аксессуары->Каминные решетки
    3185: 259,  # Аксессуары->Колосниковые решетки
    3186: 265,  # Аксессуары->Меха
    3187: 261,  # Аксессуары->Настилы для печей, конфорки
    3188: 257,  # Аксессуары->Передние панели, панели задвижек
    3189: 266,  # Аксессуары->Пластины декоративные
    3190: 267,  # Аксессуары->Подставки для каминных спичек
    3191: 262,  # Аксессуары->Предтопочные листы
    3192: 255,  # Аксессуары->Прочистные дверцы
    3193: 267,  # Аксессуары->Экраны для каминов
    3194: 270,  # Аксессуары->Ящики для золы
    3199: 112,
    3196: 438,  # Баня, сауна->Аксессуары и комплектующие для бань и саун
    3197: 228,  # Баня, сауна->Баки и теплообменники
    3198: 438,  # Баня, сауна->Камни для бань и саун
    3200: 226,  # Баня, сауна->Печи банные (каменки для сауны)->Дровяные аккумулирующие
    3201: 226,  # Баня, сауна->Печи банные (каменки для сауны)->Дровяные конвекторные
    3202: 227,  # Баня, сауна->Печи банные (каменки для сауны)->Электрические
    3204: 115,
    3206: 234,  # Барбекю-грили->Барбекю
    3207: 232,  # Барбекю-грили->Грили
    3208: 231,  # Барбекю-грили->Коптильни
    3209: 233,  # Барбекю-грили->Печи для пиццы, духовки
    17659: 287,  # Биокамины
    3211: 217,
    3215: 328,
    3212: 330,  # Дымоходы->Гибкие дымоходы
    3213: 332,  # Дымоходы->Дымоходы из вулканической пемзы
    3214: 331,  # Дымоходы->Керамические дымоходы
    3217: 487,  # Дымоходы->Модульные дымоходы из нержавеющей стали->Коаксиальные
    3218: 488,  # Дымоходы->Модульные дымоходы из нержавеющей стали->Коллективные
    3220: 486,  # Дымоходы->Модульные дымоходы из нержавеющей стали->Одностенные (овальное сечение)
    3221: 484,  # Дымоходы->Модульные дымоходы из нержавеющей стали->Одностенные (раструбно-профильное соединение)
    16322: 485,  # Дымоходы->Модульные дымоходы из нержавеющей стали->Система двухконтурных элементов с изоляцией
    3222: 333,  # Дымоходы->Одностенные дымоходы из окрашенной стали
    3223: 496,  # Дымоходы->Чугунные элементы подключения к дымоходу
    3224: 653,  # Изделия из мрамора
    3227: 654,  # Изделия из мрамора->Колонны и капители
    15771: 655,  # Изделия из мрамора->Лестницы, балясины
    3228: 656,  # Изделия из мрамора->Мозаика из мрамора
    3229: 657,  # Изделия из мрамора->Плитка для пола и стен
    3230: 658,  # Изделия из мрамора->Подоконники
    3232: 659,  # Изделия из мрамора->Скульптура и вазы из мрамора
    3233: 660,  # Изделия из мрамора->Столы и столешницы
    3234: 661,  # Изделия из мрамора->Фонтаны из мрамора
    16061: 662,  # Изделия из мрамора->Цоколи, плинтуса, молдинги, бордюры
    3226: 663,  # Изделия из мрамора->Ванны, раковины и душевые поддоны
    3231: 110,  # Изделия из мрамора->Порталы из мрамора
    3235: 294,  # Изоляционный материал. Негорючая изоляция.
    31941: 107,
    3262: 107,
    3236: 107,
    3237: 151,  # Камины (облицовки)->Встроенные, рамки, фасады
    3238: 150,  # Камины (облицовки)->Двусторонние
    3240: 153,  # Камины (облицовки)->Пристенно-угловые
    3241: 147,  # Камины (облицовки)->Пристенные (фронтальные)
    3243: 148,  # Камины (облицовки)->Угловые
    3244: 149,  # Камины (облицовки)->Центральные (островные)
    27215: 637,  # Комплектующие, запасные части->Комплектующие для каминов (облицовок)
    11908: 638,  # Комплектующие, запасные части->Комплектующие для печей
    11440: 639,  # Комплектующие, запасные части->Комплектующие для топок
    3245: 238,
    3252: 238,
    3246: 113,
    3247: 113,  # Печи, печи-камины->Отопительно-варочные->Из стеатита
    3249: 113,  # Печи, печи-камины->Отопительно-варочные->Керамические
    3250: 113,  # Печи, печи-камины->Отопительно-варочные->Металлические
    3251: 113,  # Печи, печи-камины->Отопительно-варочные->Чугунные
    3253: 238,  # Печи, печи-камины->Отопительные (каминофены)->Из стеатита
    3254: 238,  # Печи, печи-камины->Отопительные (каминофены)->Изразцовые
    3255: 238,  # Печи, печи-камины->Отопительные (каминофены)->Керамические
    3256: 238,  # Печи, печи-камины->Отопительные (каминофены)->Металлические
    3257: 238,  # Печи, печи-камины->Отопительные (каминофены)->Чугунные
    3258: 238,  # Печи, печи-камины->Пеллетные
    3289: 554,  # Печи, печи-камины->Печи для сада
    3259: 238,  # Печи, печи-камины->Печи-камины
    3261: 243,  # Печи, печи-камины->С водяным контуром
    3263: 151,  # Современные камины (Hi-Tech)->Встроенные
    3265: 176,  # Современные камины (Hi-Tech)->Подвесные, пристенные
    3269: 148,  # Современные камины (Hi-Tech)->Угловые
    3270: 149,  # Современные камины (Hi-Tech)->Центральные (островные)
    3271: 108,
    3272: 633,  # Топки->Вертикально-вытянутые
    3273: 192,  # Топки->Встраиваемые (инсерты)
    3274: 195,  # Топки->Двусторонние, Г-образное стекло
    3275: 197,  # Топки->Двусторонние, сквозные (double face)
    3276: 192,  # Топки->Односторонние, плоское стекло
    3277: 191,  # Топки->Открытые
    3278: 604,  # Топки->Панорамные, широкоформатные, 16:9, 22:9
    11441: 194,  # Топки->Полукруглое стекло
    3280: 632,  # Топки->С водяным контуром
    3281: 193,  # Топки->С призматическим стеклом
    3282: 196,  # Топки->Трехсторонние, П-образное стекло
    13961: 651,  # Уход за каминами и дымоходами->Уход за дымоходами
    13962: 652,  # Уход за каминами и дымоходами->Уход за каминами
    3283: 640,  # Электрокамины
    3285: 648,  # Элементы ландшафтного дизайна->Декоративные элементы
    17579: 642,  # Элементы ландшафтного дизайна->Ландшафтные камины
    3287: 645,  # Элементы ландшафтного дизайна->Отделочные камни для дома и пешеходных дорожек->Искусственный камень
    3288: 644,  # Элементы ландшафтного дизайна->Отделочные камни для дома и пешеходных дорожек->Натуральный камень
    3291: 646,  # Элементы ландшафтного дизайна->Садовые пуфы, банкетки, столики, скамейки
    3290: 647,  # Элементы ландшафтного дизайна->Садовые родники (фонтаны)
    3195: 112,
    26291: 635,  # Баня, сауна->Парогенераторы
}

catalogue_mapper = {
    '107': [107, {'FireplaceType': 0, 'Sub_Class_ID': 48}],  # Камины
    '147': [107, {'FireplaceType': 1, 'Sub_Class_ID': 48}],  # Пристенные (фронтальные)
    '149': [107, {'FireplaceType': 3, 'Sub_Class_ID': 48}],  # Центральные (островные)
    '153': [107, {'FireplaceType': 7, 'Sub_Class_ID': 48}],  # Пристенно-угловые
    '148': [107, {'FireplaceType': 2, 'Sub_Class_ID': 48}],  # Угловые
    '150': [107, {'FireplaceType': 8, 'Sub_Class_ID': 48}],  # Двусторонние
    '151': [107, {'FireplaceType': 4, 'Sub_Class_ID': 48}],  # Встроенные
    '176': [107, {'FireplaceType': 6, 'Sub_Class_ID': 48}],  # Подвесные
    '640': [107, {'Fuel': 2, 'Sub_Class_ID': 48}],  # Электрокамины
    '108': [108, {'topkiType': 0, 'Sub_Class_ID': 61}],  # Топки
    '192': [108, {'topkiType': 2, 'Sub_Class_ID': 61}],  # Закрытые с прямым стеклом
    '193': [108, {'topkiType': 3, 'Sub_Class_ID': 61}],  # Закрытые с призматическим стеклом
    '194': [108, {'topkiType': 4, 'Sub_Class_ID': 61}],  # Закрытые со сферическим стеклом
    '195': [108, {'topkiType': 5, 'Sub_Class_ID': 61}],  # Закрытые с Г-образным стеклом
    '196': [108, {'topkiType': 6, 'Sub_Class_ID': 61}],  # Закрытые с трехсторонним стеклом
    '197': [108, {'topkiType': 7, 'Sub_Class_ID': 61}],  # Закрытые двусторонние
    '191': [108, {'topkiType': 1, 'Sub_Class_ID': 61}],  # Открытые
    '604': [108, {'topkiType': 8, 'Sub_Class_ID': 61}],  # Панорамные
    '632': [108, {'watercontour': 1, 'Sub_Class_ID': 61}],  # С водяным контуром
    '633': [108, {'topkiType': 10, 'Sub_Class_ID': 61}],  # С водяным контуром
    '110': [110, {'Sub_Class_ID': 127}],  # Мраморные порталы
    '217': [217, {'Sub_Class_ID': 415}],  # Дымоходы
    '328': [328, {'typeSmoke': 0, 'Sub_Class_ID': 419}],  # Стальные Вулкан (Россия)
    '484': [328, {'typeSmoke': 3, 'Sub_Class_ID': 419}],  # Одностенные дымоходы
    '485': [328, {'typeSmoke': 2, 'Sub_Class_ID': 419}],  # Двустенные сэндвич-дымоходы
    '486': [328, {'typeSmoke': 4, 'Sub_Class_ID': 419}],  # Одностенные дымоходы овального сечения
    '487': [328, {'typeSmoke': 1, 'Sub_Class_ID': 419}],  # Коаксиальные дымоходы (80/130)
    '488': [328, {'typeSmoke': 5, 'Sub_Class_ID': 419}],  # Системы коллективных коаксиальных дымоходов
    '499': [328, {'typeSmoke': 10, 'Sub_Class_ID': 419}],  # Промышленные сендвич-дымоходы
    '489': [328, {'typeSmoke': 6, 'Sub_Class_ID': 419}],  # Система подогрева воды
    '527': [328, {'typeSmoke': 11, 'Sub_Class_ID': 419}],  # Дымоходы для бани
    '331': [331, {'typeHart': 0, 'Sub_Class_ID': 424}],  # Керамические Hart (Германия)
    '490': [331, {'typeHart': 1, 'Sub_Class_ID': 424}],  # Система Klassik
    '491': [331, {'typeHart': 2, 'Sub_Class_ID': 424}],  # Система Univers
    '492': [331, {'typeHart': 3, 'Sub_Class_ID': 424}],  # Система Multiceram
    '493': [331, {'typeHart': 4, 'Sub_Class_ID': 424}],  # Система AT
    '332': [217, {'Sub_Class_ID': 434}],  # Дымоходы из вулканической пемзы Heda, Keddy (Швеция)
    '330': [330, {'Sub_Class_ID': 431}],  # Гибкие стальные трубы Tubest TS Multinox (Франция)
    '497': [497, {'Sub_Class_ID': 449}],  # Дымоходы Hark (Германия)
    '494': [494, {'Sub_Class_ID': 437}],  # Стальные дымоходы EdilKamin (Италия)
    '333': [333, {'Sub_Class_ID': 427}],  # Стальные ALA Spa (Италия)
    '496': [496, {'Sub_Class_ID': 441}],  # Чугунные дымоходы Keddy (Швеция)
    '495': [495, {'Sub_Class_ID': 445}],  # Стальные дымоходы Thorma (Германия-Словакия)
    '238': [238, {'typePechi': 0, 'Sub_Class_ID': 182}],  # Печи
    '243': [238, {'typePechi': 1, 'Sub_Class_ID': 182}],  # С водяным контуром
    '244': [238, {'typePechi': 2, 'Sub_Class_ID': 182}],  # Без водяного контура
    '287': [287, {'Sub_Class_ID': 215}],  # Печи-камины
    '112': [112, {'typePechiBani': 0, 'Sub_Class_ID': 132}],  # Печи для бань
    '226': [112, {'typePechiBani': 1, 'Sub_Class_ID': 132}],  # Дровяные
    '227': [112, {'typePechiBani': 2, 'Sub_Class_ID': 132}],  # Электрические
    '228': [112, {'typePechiBani': 3, 'Sub_Class_ID': 132}],  # Котлы для воды
    '438': [112, {'typePechiBani': 4, 'Sub_Class_ID': 132}],  # Аксессуары для бани
    '635': [112, {'typePechiBani': 5, 'Sub_Class_ID': 132}],  # Парогенераторы
    '113': [113, {'Sub_Class_ID': 134}],  # Печи для кухни
    '115': [115, {'TypeBarbeque': 0, 'Sub_Class_ID': 138}],  # Барбекю
    '234': [115, {'TypeBarbeque': 1, 'Sub_Class_ID': 138}],  # Барбекю
    '231': [115, {'TypeBarbeque': 4, 'Sub_Class_ID': 138}],  # Коптильни
    '232': [115, {'TypeBarbeque': 3, 'Sub_Class_ID': 138}],  # Грили
    '233': [115, {'TypeBarbeque': 2, 'Sub_Class_ID': 138}],  # Печи для пиццы
    '554': [115, {'TypeBarbeque': 6, 'Sub_Class_ID': 138}],  # Печь для сада
    '437': [115, {'TypeBarbeque': 5, 'Sub_Class_ID': 138}],  # Аксессуары для барбекю
    '117': [117, {'typeFurnitura': 0, 'Sub_Class_ID': 142}],  # Печная фурнитура
    '255': [117, {'typeFurnitura': 1, 'Sub_Class_ID': 142}],  # Дверцы
    '256': [117, {'typeFurnitura': 2, 'Sub_Class_ID': 142}],  # Духовки
    '257': [117, {'typeFurnitura': 3, 'Sub_Class_ID': 142}],  # Задвижки и поворотные задвижки
    '258': [117, {'typeFurnitura': 4, 'Sub_Class_ID': 142}],  # Принадлежности
    '259': [117, {'typeFurnitura': 5, 'Sub_Class_ID': 142}],  # Колосники
    '260': [117, {'typeFurnitura': 6, 'Sub_Class_ID': 142}],  # Конфорки для приготовления пищи
    '261': [117, {'typeFurnitura': 7, 'Sub_Class_ID': 142}],  # Плиты печей
    '262': [117, {'typeFurnitura': 8, 'Sub_Class_ID': 142}],  # Предтопочные листы
    '118': [118, {'typeAkses': 0, 'Sub_Class_ID': 145}],  # Аксессуары
    '263': [118, {'typeAkses': 1, 'Sub_Class_ID': 145}],  # Каминные наборы
    '264': [118, {'typeAkses': 2, 'Sub_Class_ID': 145}],  # Корзины для дров и пелетт, дровницы
    '265': [118, {'typeAkses': 3, 'Sub_Class_ID': 145}],  # Мехи
    '266': [118, {'typeAkses': 4, 'Sub_Class_ID': 145}],  # Декорирующие элементы
    '267': [118, {'typeAkses': 5, 'Sub_Class_ID': 145}],  # Экраны-сетки и подставки для спичек
    '268': [118, {'typeAkses': 6, 'Sub_Class_ID': 145}],  # Быки, подставки и гриль-решетки
    '269': [118, {'typeAkses': 7, 'Sub_Class_ID': 145}],  # Каминные решетки
    '270': [118, {'typeAkses': 8, 'Sub_Class_ID': 145}],  # Ящики для золы, ведра для угля
    '293': [118, {'typeAkses': 9, 'Sub_Class_ID': 145}],  # Аксессуары для бани
    '294': [118, {'typeAkses': 10, 'Sub_Class_ID': 145}],  # Изоляционные материалы
    '413': [118, {'typeAkses': 11, 'Sub_Class_ID': 145}],  # Рамки для топок
    '429': [118, {'typeAkses': 12, 'Sub_Class_ID': 145}],  # Аксессуары к барбекю и духовкам
    '582': [118, {'typeAkses': 13, 'Sub_Class_ID': 145}],  # Аксессуары к столам-каминамкопировать раздел
    '636': [636, {'Sub_Class_ID': 608}],  # Комплектующие, запасные части
    '637': [637, {'Sub_Class_ID': 609}],  # Комплектующие для каминов (облицовок)
    '638': [638, {'Sub_Class_ID': 610}],  # Комплектующие для печей
    '639': [639, {'Sub_Class_ID': 611}],  # Комплектующие для топок
    '641': [641, {'Sub_Class_ID': 595}],  # . Элементы ландшафтного дизайна
    '642': [649, {'Sub_Class_ID': 600}],  # . Ландшафтные камины
    '643': [643, {'Sub_Class_ID': 605}],  # . Отделочные камни для дома и пешеходных дорожек
    '644': [644, {'Sub_Class_ID': 606}],  # . Натуральный камень
    '645': [645, {'Sub_Class_ID': 607}],  # . Искусственный камень
    '646': [646, {'Sub_Class_ID': 604}],  # . Садовые пуфы, банкетки, столики, скамейки
    '647': [647, {'Sub_Class_ID': 603}],  # . Садовые родники (фонтаны)
    '648': [648, {'Sub_Class_ID': 602}],  # . Декоративные элементы
    '246': [246],  # . Изделия из  мрамора
    '651': [651, {'Sub_Class_ID': 613}],  # Уход за дымоходами
    '652': [652, {'Sub_Class_ID': 614}],  # Уход за каминами
    '653': [653, {'Sub_Class_ID': 616}],  # # Изделия из мрамора
    '654': [654, {'Sub_Class_ID': 617}],  # # Изделия из мрамора->Колонны и капители
    '655': [655, {'Sub_Class_ID': 618}],  # # Изделия из мрамора->Лестницы, балясины
    '656': [656, {'Sub_Class_ID': 619}],  # # Изделия из мрамора->Мозаика из мрамора
    '657': [657, {'Sub_Class_ID': 620}],  # # Изделия из мрамора->Плитка для пола и стен
    '658': [658, {'Sub_Class_ID': 621}],  # # Изделия из мрамора->Подоконники
    '659': [659, {'Sub_Class_ID': 622}],  # # Изделия из мрамора->Скульптура и вазы из мрамора
    '660': [660, {'Sub_Class_ID': 623}],  # # Изделия из мрамора->Столы и столешницы
    '661': [661, {'Sub_Class_ID': 624}],  # # Изделия из мрамора->Фонтаны из мрамора
    '662': [662, {'Sub_Class_ID': 625}],  # # Изделия из мрамора->Цоколи, плинтуса, молдинги, бордюры
    '663': [663, {'Sub_Class_ID': 626}],  # # Изделия из мрамора->Ванны, раковины и душевые поддоны
}
