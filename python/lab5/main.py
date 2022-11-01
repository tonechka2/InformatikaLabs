import datetime
from pattern import *
with db:
    db.create_tables([Vehicle, Price]) #генерация объектов на основе классов
    Vehicle.create(name='Ка-50')
    vehicles = Vehicle.select()
    Vehicle.insert_many([{'name': '3-qaswed'}, {'name': '4-yhnbgt'}]).execute()

