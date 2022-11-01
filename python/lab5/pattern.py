from peewee import *
db = SqliteDatabase('python\\lab5\\database.db') #Подключение БД
#Базовый класс BaseModel наследуется от стандартного класса Model в модуле peewee
class BaseModel(Model):
    id = PrimaryKeyField(unique=True) #Установка уникального первичного ключа

 #Мета класс — это класс внутри класса
    class Meta:
        database = db #Отсылка на БД, с которой работает модель
        order_by = 'id' #Значение полей, по которым данные сортируются по умолчанию
# Шаблон для первой таблицы
class Vehicle(BaseModel):
#Атрибут (имя колонки) = тип данных
    name = CharField() #Символьное поле (текст)

    class Meta:
        db_table = 'vehicles' #Имя создаваемой таблицы №1

#Шаблон для второй таблицы
class Price(BaseModel):
#Атрибут (имя колонки) = тип данных
    amount = FloatField() #Вещественные(дробные) числа
    payment_date = DateField() #Дата
    expense_id = ForeignKeyField(Vehicle) #Внешний первичный ключ
    
    class Meta:
        db_table = 'prices' #Имя создаваемой таблицы №2