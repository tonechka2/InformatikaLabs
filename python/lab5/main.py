import datetime
from pattern import *

with db:
    Product.delete().execute() #clear table (NOT IF EXIST)
    Ingredient.delete().execute()
    Region.delete().execute()
    Data.delete().execute()

    db.create_tables([Product, Ingredient, Region, Data])

    Ingredient.insert([{'proteins': 0, 'fats': 0, 'carbohydrates': 0, 'hydration': 0},
                        {'proteins': 0, 'fats': 0, 'carbohydrates': 0, 'hydration': 0},
                        {'proteins': 0, 'fats': 0, 'carbohydrates': 0, 'hydration': 0},
                        {'proteins': 0, 'fats': 0, 'carbohydrates': 0, 'hydration': 0}]).execute()

    Region.insert([{'temp': 'north', 'wind': 'up', 'numer': 0, 'word': 'fxgjh',},
                    {'temp': 'south', 'wind': 'down', 'numer': 1, 'word': 'sghsfg',},
                    {'temp': 'west', 'wind': 'left', 'numer': 0, 'word': 'dh',},
                    {'temp': 'east', 'wind': 'right', 'numer': 1, 'word': 'adgn',}]).execute()

    Data.insert([{'count': 0},
                 {'count': 1},
                 {'count': 2},
                 {'count': 3}]).execute()

    Product.insert([{'product': 'chocolate', 'data': datetime.date(2022,10,25), 'region': 'north', 'amount': 0, 'cost': 0, 'iprdt': (Ingredient.select())[0].id, 'idata': (Data.select())[0].id, 'iregion': (Region.select())[0].id},
                    {'product': 'banana', 'data': datetime.date(2022,10,26), 'region': 'south', 'amount': 0, 'cost': 0   , 'iprdt': (Ingredient.select())[1].id, 'idata': (Data.select())[1].id, 'iregion': (Region.select())[1].id},
                    {'product': 'apple', 'data': datetime.date(2022,10,27), 'region': 'west', 'amount': 0, 'cost': 0     , 'iprdt': (Ingredient.select())[2].id, 'idata': (Data.select())[2].id, 'iregion': (Region.select())[2].id},
                    {'product': 'corn', 'data': datetime.date(2022,10,28), 'region': 'east', 'amount': 1, 'cost': 0      , 'iprdt': (Ingredient.select())[3].id, 'idata': (Data.select())[3].id, 'iregion': (Region.select())[3].id}]).execute()

    for Product in Product.select().where((Product.id < 2) | (Product.id > 3)): #output
        print(Product.id, Product.product)