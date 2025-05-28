""" student={"name":"krish","age":32,"grade":"A"}
print(student)
print(student["grade"])
print(student.get("name"))
student["age"]=33
student["address"]="India"
print(student)
del student["grade"]
print(student)
print(student.keys())
print(student.values())
print(student.items()) """


###copy
student={"name":"krish","age":32,"grade":"A"}
"""student_copy=student
print(student_copy)
student["name"]="krish1"
print(student)
print(student_copy)"""

###shallow copy

"""student_copy1=student.copy()
student["age"]=33
print(student_copy1)
print(student)"""

##iteration

"""for keys in student.keys():
    print(keys)
for values in student.values():
    print(values)
for key,value in student.items():
    print(f"{key}:{value}")
"""
###nested dictionaries

students={
    "student1":{"name":"vidya","age":33},
    "student2":{"name":"roshin","age":35}
}
#print(students)

###access the data
"""print(students["student1"]["name"])
print(students["student1"]["age"])"""

##access using for loop

for student_id,student_info in students.items():
    print(f"{student_id}:{student_info}")
    for key,value in student_info.items():
        print(f"{key}:{value}")