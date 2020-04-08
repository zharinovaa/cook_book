def make_dict_recipies():
  with open('recipies.txt') as f:
    dict_cook_book = dict()
    line = f.readline().strip()
    while line:
      dish_name = line
      counter = int(f.readline().strip())
      list_ingredients = list(range(counter))
      for i in range(counter):
        ingredient = f.readline().strip()
        split_ingredient = ingredient.split(' | ')
        temp_dict = {'ingredient_name': split_ingredient[0], 'quantity': int(split_ingredient[1]), 'measure': split_ingredient[2]}
        list_ingredients[i-1] = temp_dict
      line = f.readline()  
      line = f.readline().strip()  
      dict_cook_book.setdefault(dish_name, list_ingredients)
  print(f'cook_book =', dict_cook_book)

def get_shop_list_by_dishes(dishes, person_count):

  with open('recipies.txt') as f:
    dict_cook_book = dict()
    line = f.readline().strip()
    while line:
      dish_name = line
      counter = int(f.readline().strip())
      list_ingredients = list(range(counter))
      for i in range(counter):
        ingredient = f.readline().strip()
        split_ingredient = ingredient.split(' | ')
        temp_dict = {'ingredient_name': split_ingredient[0], 'quantity': int(split_ingredient[1]), 'measure': split_ingredient[2]}
        list_ingredients[i-1] = temp_dict
      line = f.readline()  
      line = f.readline().strip()  
      dict_cook_book.setdefault(dish_name, list_ingredients)


  dict_products = dict()
  for dish in dishes:
    if dish in dict_cook_book.keys():
      for item in dict_cook_book[dish]:
        if item['ingredient_name'] in dict_products.keys():
          temp = dict_products[item['ingredient_name']]['quantity']
          dict_products[item['ingredient_name']] = {'measure': item['measure'], 'quantity': item['quantity']*person_count+temp}
        else:
          dict_products[item['ingredient_name']] = {'measure': item['measure'], 'quantity': item['quantity']*person_count}
  print(dict_products)


make_dict_recipies()
print('\n')
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
