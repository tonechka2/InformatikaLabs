from pattern import *

with db:
    Friday.delete().execute() #clear table (NOT IF EXIST)
    Students.delete().execute()
    Teachers.delete().execute()
    Another.delete().execute()
    

    db.create_tables([Friday, Students, Teachers, Another])

    Friday.insert([{'id': 0,'discipline': 'Информатика', 'audience_number': '407', 'teacher': 'Саклаков В.М.', 'number_of_students': 12.5, 'time': '8.30-10.05', 'complexity': 'middle', 'students_id': 0, 'teachers_id': 0, 'another_id': 0}, #input manual
                   {'id': 1,'discipline': 'НГ и ИГ', 'audience_number': '416', 'teacher': 'Фех А.И.', 'number_of_students': 20, 'time': '10.25-12.00', 'complexity': 'strong', 'students_id': 1, 'teachers_id': 1, 'another_id': 1},
                   {'id': 2,'discipline': 'Математика', 'audience_number': '422', 'teacher': 'Бельснер О.А.', 'number_of_students': 17.5, 'time': '12.40-14.15', 'complexity': 'weak', 'students_id': 2, 'teachers_id': 2, 'another_id': 2},
                   {'id': 3,'discipline': 'Инженерная психология', 'audience_number': '319', 'teacher': 'Панькова Н.М.', 'number_of_students': 10.5, 'time': '14.35-16.10', 'complexity': 'weak', 'students_id': 3, 'teachers_id': 3, 'another_id': 3}]).execute()

    Students.insert([{'surname': 'Колесникова', 'name': 'Вероника', 'date_of_birth': '06.12.2004', 'town': 'Тараз', 'favorite_number': '6', 'students_id': 0}, #input manual
                     {'surname': 'Иванов', 'name': 'Станислав', 'date_of_birth': '27.03.2005', 'town': 'Караганда', 'favorite_number': '17', 'students_id': 1},
                     {'surname': 'Карпенко', 'name': 'Ксения', 'date_of_birth': '10.09.2004', 'town': 'Челябинск', 'favorite_number': '13', 'students_id': 2},
                     {'surname': 'Синкина', 'name': 'Екатерина', 'date_of_birth': '22.10.2004', 'town': 'Кемерово', 'favorite_number': '10', 'students_id': 3}]).execute()

    Teachers.insert([{'mail': 'saklavas@tpu.ru', 'numbers': '+7 (3822) 701777', 'departments': 'ОМИ', 'schools': 'ИШПР', 'quotes': '- Это буллинг... - Нет, это троллинг.', 'teachers_id': 0}, #input manual
                     {'mail': 'fehai@tpu.ru', 'numbers': '5265', 'departments': 'ООД', 'schools': 'ШИП', 'quotes': '- У нас Фех! - И этим все сказано...', 'teachers_id': 1},
                     {'mail': 'belsner@tpu.ru', 'numbers': '+7 (3822) 606335', 'departments': 'ОЭФ', 'schools': 'ИЯТШ', 'quotes': '-То, что похоже на нормальное, ещё не факт, что нормальное))', 'teachers_id': 2},
                     {'mail': 'pankova_natalia@tpu.ru', 'numbers': '606441', 'departments': 'ОСГН', 'schools': 'ШБИП', 'quotes': 'Некоторые люди в раннем возрасте детей рожают... ЧТО они могут донести до своего ребенка, если они сами элементарные вещи не знают? [Не знают] что предохраняться надо...', 'teachers_id': 3}]).execute()

    Another.insert([{'university_buildings': 'Кибернетический центр', 'coffee_vending_machines': 1, 'floors': '4', 'street': 'Советская', 'number_of_the_house': '84/3', 'another_id': 0}, #input manual
                     {'university_buildings': 'Корпус №10', 'coffee_vending_machines': 4, 'floors': '5', 'street': 'пр-кт. Ленина', 'number_of_the_house': '2', 'another_id': 1},
                     {'university_buildings': 'Корпус №10', 'coffee_vending_machines': 4, 'floors': '5', 'street': 'пр-кт. Ленина', 'number_of_the_house': '2', 'another_id': 2},
                     {'university_buildings': 'Корпус №19', 'coffee_vending_machines': 3, 'floors': '6', 'street': 'Советская', 'number_of_the_house': '73/1', 'another_id': 3},]).execute()
    for row in Friday.select(Friday.discipline, Teachers.mail).join(Teachers).dicts():
        print(row)