import datetime
from pattern import *

with db:
    Vehicle.delete().execute()
    Price.delete().execute()
    db.create_tables([Vehicle, Price]) #генерация объектов на основе классов
    Vehicle.insert([{'name': '3-qaswed', 'type': 'ergwg', 'amount': 0},
                    {'name': '4-yhnbgt', 'type': 'sdgha', 'amount': 1}]).execute()
    Price.insert([{'amount': 0, 'payment_date': datetime.date(2022,10,25), 'expense_id': 1},
                  {'amount': 100, 'payment_date': datetime.date(2022,10,25), 'expense_id': 2}]).execute()  
