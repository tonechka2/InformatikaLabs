import datetime
from pattern import *
with db:
    db.create_tables([Vehicle, Price]) #генерация объектов на основе классов
    helicopter = Vehicle(name='Ка-50').save()
    vehicles = Vehicle.select()
    prices = [
    {'amount': 48, 'payment_date': datetime.date(2022,10,25), 'expense_id': vehicles[0].id},
    {'amount': 35, 'payment_date': datetime.date(2022,10,24), 'expense_id': vehicles[1].id},
    {'amount': 12, 'payment_date': datetime.date(2022,10,23), 'expense_id': vehicles[1].id},
    {'amount': 66, 'payment_date': datetime.date(2022,10,20), 'expense_id': vehicles[2].id}
    ]
    Price.insert_many(prices).execute()
