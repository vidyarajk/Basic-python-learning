import sqlite3
connection=sqlite3.connect('sales_data.db')
cursor=connection.cursor()
cursor.execute("drop table if exists sales")
#create table
cursor.execute('''
    create table if not exists sales(
        id integer primary key,
        date text not null,
        product text not null,
        sales integer,
        region text
    )
''')
#insert data
sales_data=[
        ("2024-06-01", "Laptop", 10, "North"),
        ("2024-06-01", "Phone", 25, "South"),
        ("2024-06-02", "Tablet", 12, "East"),
        ("2024-06-02", "Laptop", 8, "West"),
        ("2024-06-03", "Phone", 30, "North"),
        ("2024-06-03", "Tablet", 7, "South"),
        ("2024-06-04", "Laptop", 15, "East"),
        ("2024-06-04", "Phone", 20, "West"),
        ("2024-06-05", "Tablet", 14, "North"),
        ("2024-06-05", "Laptop", 6, "South")
]
cursor.executemany('''insert into sales(date,product,sales,region)
                   values(?, ?, ?, ?)''',sales_data)
                   
connection.commit()
cursor.execute("select * from sales")
rows=cursor.fetchall()
for row in rows:
    print(row)

connection.close()
