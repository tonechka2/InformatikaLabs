import datetime
from pattern import *
i = 0

with db:
    Vehicle.delete().execute()
    Price.delete().execute()
    Underground.delete().execute()
    Aqua.delete().execute()

    db.create_tables([Vehicle, Price, Underground, Aqua])

    Vehicle.insert([{'name': 'qaswed', 'type': 'ergwg', 'amount': 0},
                    {'name': '4-yhnbgt', 'type': 'sdgha', 'amount': 1}]).execute()

    while i < 5:
        i += 1
        Vehicle.create(name = 'vzuh' * i, type = 'vzuh', amount = i)
        Underground.create(name = 'vzuh' * i, type = 'vzuh', amount = i)
        Aqua.create(name = 'vzuh' * i, type = 'vzuh', amount = i)

    Price.insert([{'amount': 0, 'payment_date': datetime.date(2022,10,25), 'expense_id': 1},
                  {'amount': 100, 'payment_date': datetime.date(2022,10,25), 'expense_id': 2}]).execute()

    for Vehicle in Vehicle.select().where((Vehicle.id < 3) | (Vehicle.id > 5)):
        print(Vehicle.id, Vehicle.name)