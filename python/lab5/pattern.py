from peewee import *
db = SqliteDatabase('python\\lab5\\database.db')

class BaseModel(Model):
    id = PrimaryKeyField(unique=True)

    class Meta:
        database = db
        order_by = 'id'

class Ingredient(BaseModel):
    proteins = DateField(null = True)
    fats = CharField(null = True)
    carbohydrates = CharField(null = True)
    hydration = IntegerField(null = True)
    class Meta:
        db_table = 'ingredients'

class Region(BaseModel):
    temp = FloatField(null = True)
    wind = CharField(null = True)
    numer = IntegerField(null = True)
    word = CharField(null = True)

    class Meta:
        db_table = 'region'

class Data(BaseModel):
    count = IntegerField(null = True)
    people = IntegerField(null = True)
    animal = IntegerField(null = True)

    class Meta:
        db_table = 'data'

class Product(BaseModel):
    data = DateField(null = True)
    region = CharField(null = True)
    product = CharField(null = True)
    amount = IntegerField(null = True)
    cost = FloatField(null = True)
    iprdt = ForeignKeyField(Ingredient, null = True)
    idata = ForeignKeyField(Region, null = True)
    iregion = ForeignKeyField(Data, null = True)

    class Meta:
        db_table = 'product'