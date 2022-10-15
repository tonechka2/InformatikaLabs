import sqlite3

with sqlite3.connect('database.db') as db:
    cursor = db.cursor()
    cursor.execute(""" DROP TABLE IF EXISTS table_of_nf1 """)
    cursor.execute(""" DROP TABLE IF EXISTS table_of_nf2_1 """)
    cursor.execute(""" DROP TABLE IF EXISTS table_of_nf2_2 """)
    cursor.execute(""" DROP TABLE IF EXISTS table_of_nf3 """)
    # создаем первую таблицу
    cursor.execute(""" CREATE TABLE IF NOT EXISTS table_of_nf1 (id INTEGER PRIMARY KEY, shipper TEXT, grade TEXT, quality TEXT, amount REAL, сost REAL) """)
    cursor.executescript(""" 
    INSERT INTO table_of_nf1(shipper, grade, quality, amount, сost) VALUES('Омск', 'Зерно черное', 'Хорошее', 1.1, 18.5);
    INSERT INTO table_of_nf1(shipper, grade, quality, amount, сost) VALUES('Новосибирск', 'Зерно серое', 'Плохое', '2.1', 10.5);
    INSERT INTO table_of_nf1(shipper, grade, quality, amount, сost) VALUES('Томск', 'Зерно коричневое', 'Плохое', '3.1', 10.5);
    INSERT INTO table_of_nf1(shipper, grade, quality, amount, сost) VALUES('Новосибирск', 'Зерно белое', 'Хорошее', '1.4', 18.5);
    INSERT INTO table_of_nf1(shipper, grade, quality, amount, сost) VALUES('Томск', 'Зерно серое', 'Плохое', '2.8', 10.5);
    INSERT INTO table_of_nf1(shipper, grade, quality, amount, сost) VALUES('Омск', 'Зерно коричневое', 'Плохое', '2.9', 10.5);
    INSERT INTO table_of_nf1(shipper, grade, quality, amount, сost) VALUES('Омск', 'Зерно черное', 'Плохое', '1.5', 10.5);
    INSERT INTO table_of_nf1(shipper, grade, quality, amount, сost) VALUES('Томск', 'Зерно белое', 'Хорошее', '3.4', 18.5);
    """)
    # создаем вторую таблицу
    cursor.execute(""" CREATE TABLE IF NOT EXISTS table_of_nf2_1 (id INTEGER PRIMARY KEY, shipper TEXT, grade TEXT, amount REAL) """)
    cursor.executescript("""
    INSERT INTO table_of_nf2_1(shipper, grade, amount) VALUES('Омск', 'Зерно черное', 1.1);
    INSERT INTO table_of_nf2_1(shipper, grade, amount) VALUES('Омск', 'Зерно черное', 1.1);
    INSERT INTO table_of_nf2_1(shipper, grade, amount) VALUES('Омск', 'Зерно черное', 1.1);
    INSERT INTO table_of_nf2_1(shipper, grade, amount) VALUES('Омск', 'Зерно черное', 1.1);
    INSERT INTO table_of_nf2_1(shipper, grade, amount) VALUES('Омск', 'Зерно черное', 1.1);
    INSERT INTO table_of_nf2_1(shipper, grade, amount) VALUES('Омск', 'Зерно черное', 1.1);
    INSERT INTO table_of_nf2_1(shipper, grade, amount) VALUES('Омск', 'Зерно черное', 1.1);
    INSERT INTO table_of_nf2_1(shipper, grade, amount) VALUES('Омск', 'Зерно черное', 1.1);
    """)
    db.commit()
    pass