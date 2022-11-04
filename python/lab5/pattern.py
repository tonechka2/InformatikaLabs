from peewee import *
db = SqliteDatabase('python\\lab5\\database.db')

class BaseModel(Model):
    id = PrimaryKeyField(unique=True)

    class Meta:
        database = db
        order_by = 'id'

class Vehicle(BaseModel):
    name = CharField()
    type = CharField()
    amount = FloatField()

    class Meta:
        db_table = 'vehicles'


class Price(BaseModel):
    amount = FloatField()
    payment_date = DateField()
    expense_id = ForeignKeyField(Vehicle)
    
    class Meta:
        db_table = 'prices'