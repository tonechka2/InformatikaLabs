from peewee import *
db = SqliteDatabase('database.db')

class BaseModel(Model):
    id = PrimaryKeyField(unique=True)

    class Meta:
        database = db
        order_by = 'id'

class Friday(BaseModel):
    id = CharField()
    discipline = CharField()
    audience_number = CharField()
    teacher = CharField()
    number_of_students = CharField()
    time = CharField()
    complexity = CharField()
    students_id = CharField()
    teachers_id = CharField()
    another_id = CharField()

    class Meta:
        db_table = 'Friday'


class Students(BaseModel):
    surname = CharField()
    name = CharField()
    date_of_birth = CharField()
    town = CharField()
    favorite_number = CharField()
    students_id = ForeignKeyField(Friday)
    
    class Meta:
        db_table = 'Students'

class Teachers(BaseModel):
    mail = CharField()
    numbers = CharField()
    departments = CharField()
    schools = CharField()
    quotes = CharField()
    teachers_id = ForeignKeyField(Friday)
    
    class Meta:
        db_table = 'Teachers'

class Another(BaseModel):
    university_buildings = CharField()
    coffee_vending_machines = CharField()
    floors = CharField()
    street = CharField()
    number_of_the_house = CharField()
    another_id = ForeignKeyField(Friday)
    
    class Meta:
        db_table = 'Another'