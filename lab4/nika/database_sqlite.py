import sqlite3

with sqlite3.connect('python\\lab4\\nika\\database.db') as db:
    cursor = db.cursor()
    cursor.execute(""" DROP TABLE IF EXISTS table_of_nf1 """)
    cursor.execute(""" DROP TABLE IF EXISTS table_of_nf2_1 """)
    cursor.execute(""" DROP TABLE IF EXISTS table_of_nf2_2 """)
    cursor.execute(""" DROP TABLE IF EXISTS table_of_nf2_3 """)
    cursor.execute(""" DROP TABLE IF EXISTS table_of_nf3_1 """)
    cursor.execute(""" DROP TABLE IF EXISTS table_of_nf3_2 """)
    cursor.execute(""" DROP TABLE IF EXISTS table_of_nf4_1 """)
    cursor.execute(""" DROP TABLE IF EXISTS table_of_nf4_2 """)
    # создаем первую таблицу
    cursor.execute(""" CREATE TABLE IF NOT EXISTS table_of_nf1 (id INTEGER, brend TEXT, model TEXT, year TEXT, cost TEXT, fuel TEXT, volume REAL) """)
    cursor.executescript("""
    INSERT INTO table_of_nf1(id, brend, model, year, cost, fuel, volume) VALUES('1', 'Toyota','Mark II','2021','1 799 000', 'гибрид', 4.0);
    INSERT INTO table_of_nf1(id, brend, model, year, cost, fuel, volume) VALUES('2', 'Mazda','Volkswagen','1994','395 000', 'бензин', 2.5);
    INSERT INTO table_of_nf1(id, brend, model, year, cost, fuel, volume) VALUES('3', 'Mercedes-Benz','G-Класс 500','2022','17 600 000', 'бензин', 2.0);
    INSERT INTO table_of_nf1(id, brend, model, year, cost, fuel, volume) VALUES('4', 'BMW','LX 500d IV','2022','32 000 000', 'дизель', 3.4);
    INSERT INTO table_of_nf1(id, brend, model, year, cost, fuel, volume) VALUES('2', 'Toyota','Honda Civic','2000','750 000', 'бензин', 3.0);
    INSERT INTO table_of_nf1(id, brend, model, year, cost, fuel, volume) VALUES('5', 'Lexus','X5 40d IV','2022','13 586 000', 'дизель', 3.0);
    INSERT INTO table_of_nf1(id, brend, model, year, cost, fuel, volume) VALUES('4', 'Volkswagen','450d III','2020','12 500 000', 'дизель', 2.5);
    INSERT INTO table_of_nf1(id, brend, model, year, cost, fuel, volume) VALUES('1', 'Honda Civic','3 III','1991','2 250 000', 'дизель', 3.5);
    INSERT INTO table_of_nf1(id, brend, model, year, cost, fuel, volume) VALUES('4', 'Lexus', 'GS 550h IV','2012','3 750 000', 'гибрид', 1.5);
    """)
    # создаем вторую таблицу 1
    cursor.execute(""" CREATE TABLE IF NOT EXISTS table_of_nf2_1 (id_number INTEGER, discipline TEXT, audience_number TEXT, teacher TEXT, date TEXT, number_of_students REAL, time TEXT) """)
    cursor.executescript("""
    INSERT INTO table_of_nf2_1(id_number, discipline, audience_number, teacher, date, number_of_students, time) VALUES('1', 'Математика','207','Бельснер О.А.','10.10.2022', 15.5, '14.35-16.10');
    INSERT INTO table_of_nf2_1(id_number, discipline, audience_number, teacher, date, number_of_students, time) VALUES('2', 'НГ и ИГ','417','Фех А.И.','12.10.2022', 10, '10.25-12.00');
    INSERT INTO table_of_nf2_1(id_number, discipline, audience_number, teacher, date, number_of_students, time) VALUES('3', 'Физика','322','Кузнецов В.М.','20.10.2022', 17.5, '12.40-14.15');
    INSERT INTO table_of_nf2_1(id_number, discipline, audience_number, teacher, date, number_of_students, time) VALUES('4', 'Введение в инженерную деятельность','119','Елифеева Г.И','10.10.2022', 11.5, '18.25-20.00');
    INSERT INTO table_of_nf2_1(id_number, discipline, audience_number, teacher, date, number_of_students, time) VALUES('5', 'Физкультура','206','Коломеец С.Б.','10.10.2022', 23, '16.30-18.05');
    INSERT INTO table_of_nf2_1(id_number, discipline, audience_number, teacher, date, number_of_students, time) VALUES('6', 'Оказание первой помощи','123','Романов И.И.','20.10.2022', 7.5, '14.35-16.10');
    INSERT INTO table_of_nf2_1(id_number, discipline, audience_number, teacher, date, number_of_students, time) VALUES('7', '-----','-----','-----','10.10.2022', 0, '20.20-21.55');
    INSERT INTO table_of_nf2_1(id_number, discipline, audience_number, teacher, date, number_of_students, time) VALUES('8', '-----','-----','-----','10.10.2022', 0, '-----');
    """)
    # создаем вторую таблицу 2
    cursor.execute(""" CREATE TABLE IF NOT EXISTS table_of_nf2_2 (id_c INTEGER, complexity) """)
    cursor.executescript("""
    INSERT INTO table_of_nf2_2(id_c, complexity) VALUES('1', 'easy');
    INSERT INTO table_of_nf2_2(id_c, complexity) VALUES('2', 'strong');
    INSERT INTO table_of_nf2_2(id_c, complexity) VALUES('3', 'weakly');
    INSERT INTO table_of_nf2_2(id_c, complexity) VALUES('4', 'middle');
    """)
     # создаем вторую таблицу 3
    cursor.execute(""" CREATE TABLE IF NOT EXISTS table_of_nf2_3 (id_number INTEGER, id_c INTEGER) """)
    cursor.executescript("""
    INSERT INTO table_of_nf2_3(id_number, id_c) VALUES('1', '8');
    INSERT INTO table_of_nf2_3(id_number, id_c) VALUES('2', '4');
    INSERT INTO table_of_nf2_3(id_number, id_c) VALUES('3', '2');
    INSERT INTO table_of_nf2_3(id_number, id_c) VALUES('4', '2');
    INSERT INTO table_of_nf2_3(id_number, id_c) VALUES('5', '2');
    INSERT INTO table_of_nf2_3(id_number, id_c) VALUES('6', '6');
    INSERT INTO table_of_nf2_3(id_number, id_c) VALUES('7', '7');
    INSERT INTO table_of_nf2_3(id_number, id_c) VALUES('8', '6');
    """)
    # создаем третью таблицу 1
    cursor.execute(""" CREATE TABLE IF NOT EXISTS table_of_nf3_1 (ministry_id INTEGER PRIMARY KEY, name TEXT, discription TEXT) """)
    cursor.executescript("""
    INSERT INTO table_of_nf3_1(name, discription) VALUES('Министерство образования и науки РФ', 'орган власти, осуществляющим руководство в сферах образования, науки, защиты прав детей и молодёжной политики.');
    INSERT INTO table_of_nf3_1(name, discription) VALUES('Министерство внутренних дел РФ', 'орган власти, осуществляющий руководство системой органов внутренних дел Республики Казахстан в области предупреждения и ликвидации чрезвычайных ситуаций природного и техногенного характера.');
    INSERT INTO table_of_nf3_1(name, discription) VALUES('Министерство обороны РФ', 'орган власти, осуществляющим государственную политику в сфере обороны, а также руководство Вооружёнными Силами Республики Казахстан.');
    INSERT INTO table_of_nf3_1(name, discription) VALUES('Министерство по чрезвычайным ситуациям РФ', 'орган власти, осуществляющий формирование государственной политики в области предупреждения и ликвидации чрезвычайных ситуаций природного и техногенного характера, гражданской обороны и т.д.');
    INSERT INTO table_of_nf3_1(name, discription) VALUES('Министерство иностранных дел РФ', 'орган власти, осуществляющий внешнеполитическую деятельность и возглавляющий единую систему органов дипломатической службы Республики Казахстан. ');
    INSERT INTO table_of_nf3_1(name, discription) VALUES('Министерство здравоохранения РФ', 'орган власти, осуществляющий руководство, а также в пределах, предусмотренных законодательством, межотраслевую координацию в сфере охраны здоровья граждан, медицинского и фармацевтического образования.');
    INSERT INTO table_of_nf3_1(name, discription) VALUES('Министерство культуры и спорта РФ', 'орган власти, осуществляющим руководство в сферах культуры, внутриполитической стабильности, межэтнического согласия, развития языков, государственных символов, государственного социального заказа, архивного дела и документации, религиозной деятельности, физической культуры и спорта, игорного бизнеса, а также в пределах, предусмотренных законодательством, - межотраслевую координацию и государственное регулирование.');
    INSERT INTO table_of_nf3_1(name, discription) VALUES('Министерство энергетики РФ', 'орган власти, осуществляющий государственное управление в области энергетики');
    """)
     # создаем третью таблицу 2
    cursor.execute(""" CREATE TABLE IF NOT EXISTS table_of_nf3_2 (id INTEGER PRIMARY KEY, date_of_foundation TEXT, guide TEXT, site TEXT) """)
    cursor.executescript("""
    INSERT INTO table_of_nf3_2(date_of_foundation, guide, site) VALUES('02.10.1998', 'Алексеев Руслан', 'edu.gov.kz/ru');
    INSERT INTO table_of_nf3_2(date_of_foundation, guide, site) VALUES('03.06.1992', 'Ромашенко Адрей', 'mvd.gov.kz');
    INSERT INTO table_of_nf3_2(date_of_foundation, guide, site) VALUES('08.05.1993', 'Курпатов Сергей', 'mod.gov.kz');
    INSERT INTO table_of_nf3_2(date_of_foundation, guide, site) VALUES('25.11.1996', 'Собченко Юрий', '-----');
    INSERT INTO table_of_nf3_2(date_of_foundation, guide, site) VALUES('16.11.2000', 'Смелов Роман', 'mfa.gov.kz');
    INSERT INTO table_of_nf3_2(date_of_foundation, guide, site) VALUES('15.10.1993', 'Доскалиев Жаксылык', 'dsm.gov.kz');
    INSERT INTO table_of_nf3_2(date_of_foundation, guide, site) VALUES('15.01.2011', 'Рыбаков Александр', 'mk.gov.kz');
    INSERT INTO table_of_nf3_2(date_of_foundation, guide, site) VALUES('05.09.2013', 'Акчулаков Болат', 'energo.gov.kz');
    """)
    db.commit()
    # вывод результата
    cursor.execute("""SELECT * FROM table_of_nf2_1""")
    for row in cursor.fetchall(): 
        print("id_number", row[0], "discipline", row[1], "audience_number", row[2], "teacher", row[3], "date", row[4], "number_of_students", row[5], "time", row[6])

    
    