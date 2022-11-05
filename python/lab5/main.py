import datetime
from pattern import *
i = 0

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
                 
    Product.insert([{'product': 'chocolate', 'data': datetime.date(2022,10,25), 'region': 'north', 'amount': 0, 'cost': 0, 'iprdt': Ingredient.id[0], 'idata': Data.id[0], 'iregion': Region.id[0]},
                    {'product': 'banana', 'data': datetime.date(2022,10,26), 'region': 'south', 'amount': 0, 'cost': 0   , 'iprdt': Ingredient.id[1], 'idata': Data.id[1], 'iregion': Region.id[1]},
                    {'product': 'apple', 'data': datetime.date(2022,10,27), 'region': 'west', 'amount': 0, 'cost': 0     , 'iprdt': Ingredient.id[2], 'idata': Data.id[2], 'iregion': Region.id[2]},
                    {'product': 'corn', 'data': datetime.date(2022,10,28), 'region': 'east', 'amount': 1, 'cost': 0      , 'iprdt': Ingredient.id[3], 'idata': Data.id[3], 'iregion': Region.id[3]}]).execute()

    for Product in Product.select().where((Product.id < 2) | (Product.id > 3)): #output
        print(Product.id, Product.product)