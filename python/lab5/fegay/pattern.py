from peewee import *
db = SqliteDatabase('python\\lab5\\database.db')

class BaseModel(Model):
    id = PrimaryKeyField(unique=True)

    class Meta:
        database = db
        order_by = 'id'

class Vehicle(BaseModel):
    name = CharField(null = True)
    type = CharField(null = True)
    amount = FloatField()
    number = CharField(null = True)
    elephant = CharField(null = True)
    banana = CharField(null = True)

    class Meta:
        db_table = 'vehicles'


class Price(BaseModel):
    amount = FloatField()
    payment_date = DateField(null = True)
    bitter = CharField(null = True)
    coffee = CharField(null = True)
    apple = CharField(null = True)
    expense_id = ForeignKeyField(Vehicle, null = True)
    
    class Meta:
        db_table = 'prices'

class Underground(BaseModel):
    amount = FloatField()
    payment_date = DateField(null = True)
    bitter = CharField(null = True)
    coffee = CharField(null = True)
    apple = CharField(null = True)
    expense_id = ForeignKeyField(Vehicle, null = True)
    
    class Meta:
        db_table = 'underground'

class Aqua(BaseModel):
    amount = FloatField()
    payment_date = DateField(null = True)
    bitter = CharField(null = True)
    coffee = CharField(null = True)
    apple = CharField(null = True)
    expense_id = ForeignKeyField(Vehicle, null = True)
    
    class Meta:
        db_table = 'aqua'