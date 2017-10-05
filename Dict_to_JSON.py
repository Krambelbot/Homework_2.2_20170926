import json
from pprint import pprint

cook_book = {
    'шарлотка': [
        {'ingridient_name': 'яйцо', 'quantity': 1, 'measure': 'шт.'},
        {'ingridient_name': 'мука', 'quantity': 50, 'measure': 'гр.'},
        {'ingridient_name': 'сахар', 'quantity': 40, 'measure': 'гр.'},
        {'ingridient_name': 'яблоки', 'quantity': 50, 'measure': 'гр.'}
    ],
    'курица в духовке': [
        {'ingridient_name': 'курица', 'quantity': 200, 'measure': 'гр.'},
        {'ingridient_name': 'картофель', 'quantity': 400, 'measure': 'гр.'},
        {'ingridient_name': 'масло', 'quantity': 50, 'measure': 'мл.'},
        {'ingridient_name': 'майонез', 'quantity': 20, 'measure': 'гр.'}
    ],
    'цезарь': [
        {'ingridient_name': 'салат', 'quantity': 20, 'measure': 'гр.'},
        {'ingridient_name': 'батон', 'quantity': 20, 'measure': 'гр.'},
        {'ingridient_name': 'масло', 'quantity': 50, 'measure': 'мл.'},
        {'ingridient_name': 'чеснок', 'quantity': 10, 'measure': 'гр.'},
        {'ingridient_name': 'курица', 'quantity': 100, 'measure': 'гр.'}
    ]
}

with open('Recipes.json', 'w') as f:
    json.dump(cook_book, f, ensure_ascii=False)