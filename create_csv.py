import csv
with open("Example.csv",mode='w',newline='')as file:
    writer=csv.writer(file)
    writer.writerow(["name","age"])
    writer.writerow(["vidya",33])
with open("Example.csv",mode='r')as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)