import sqlite3
# connect to a sqlite database
connection=sqlite3.connect("example.db")
print(connection)
# create cursor object
cursor=connection.cursor()

cursor.execute('DROP TABLE IF EXISTS employee')
# create table
cursor.execute('''
    create table if not exists employee(
        id integer primary key,
        name text not null,
        age integer,
        department text
    )
''')
# commit changes
connection.commit()


#insert data into employee
cursor.execute('''
    insert into employee(name,age,department)
               values("vidya",34,"data science"),
               ("roshin",36,"engr"),
               ("yuvram",5,"kg")
''')
#commit the change
connection.commit()

#update the table
cursor.execute('''
    UPDATE employee 
    set age=33
    where name="vidya"
''')
connection.commit()

cursor.execute('''
    select * from employee
''')
rows=cursor.fetchall()
for row in rows:
    print(row)

#delate data from table
cursor.execute('''
    delete from employee
               where name="yuvram"
''')
connection.commit()
cursor.execute('''
    select * from employee
''')
rows=cursor.fetchall()
for row in rows:
    print(row)
