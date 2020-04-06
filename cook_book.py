def make_dict_recipies():
  with open('recipies.txt') as f:
      dict_cook_book = dict()
      for line in f:
          dish_name = f.readline()
          counter = int(f.readline())
          list_ingredients = list(range(counter))
          for i in range(counter):
            ingredient = f.readline()
            split_ingredient = ingredient.split(' | ')
            temp_dict = {'ingredient_name': split_ingredient[0], 'quantity': int(split_ingredient[1]), 'measure': split_ingredient[2]}
            list_ingredients[i-1] = temp_dict
          dict_cook_book.setdefault(dish_name, list_ingredients)
      print(f'cook_book =', dict_cook_book)

def get_shop_list_by_dishes(dishes, person_count):

  with open('recipies.txt') as f:
      dict_cook_book = dict()
      for line in f:
          dish_name = f.readline()
          counter = int(f.readline())
          list_ingredients = list(range(counter))
          for i in range(counter):
            ingredient = f.readline()
            split_ingredient = ingredient.split(' | ')
            temp_dict = {'ingredient_name': split_ingredient[0], 'quantity': int(split_ingredient[1]), 'measure': split_ingredient[2]}
            list_ingredients[i-1] = temp_dict
          dict_cook_book.setdefault(dish_name, list_ingredients)

  counter = 6
  i = 0
  list_products = list(range(counter))
  for dish in dishes:
    if dish in dict_cook_book.keys():
      for item in dict_cook_book[dish]:
        temp_dict_1 = {item['ingredient_name']: {'measure': item['measure'], 'quantity': item['quantity']*person_count}}
        list_products[i] = temp_dict_1
        i += 1
  print(list_products)


make_dict_recipies()
print('\n')
get_shop_list_by_dishes(['Запеченный картофель\n', 'Омлет\n'], 2)