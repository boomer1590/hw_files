from pprint import pprint
import os

path = os.path.join((os.getcwd()), 'food.txt')

with open(path) as file:
    cook_book = {}
    for dish in file:
        dish_name = dish.strip()
        counter = int(file.readline().strip())
        structure_list = []
        for components in range(counter):
            ingredient_name, quantity, measure = file.readline().split('|')
            structure_list.append(
                {'ingredient_name': ingredient_name.strip(), 'quantity': int(quantity.strip()), 'measure': measure.strip()}
            )
        cook_book[dish_name] = structure_list
        file.readline()
    # print('cook_book = ', end="")
    # pprint(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            help_shop_list = dict(ingredient)
            help_shop_list['quantity'] *= person_count

            if help_shop_list['ingredient_name'] not in shop_list:
                shop_list[help_shop_list['ingredient_name']] = help_shop_list
            else:
                shop_list[help_shop_list['ingredient_name']]['quantity'] += help_shop_list['quantity']

    for value_sl in shop_list.values():
        del value_sl['ingredient_name']

    return shop_list

pprint(get_shop_list_by_dishes(['Фахитос', 'Фахитос'], 1))





