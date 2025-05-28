age=int(input("Enter the age"))

if age <=5:
    print("Ticket rate is free")
elif age ==17:
    is_student=input("Are you a student?yes/no").lower()
    if is_student=='yes':
        print("Ticket rate is 10/-")
    else:
        print("Ticket rate is 15/-")
elif age<=65:
    print("Ticket rate is 18")
else:
    print("Ticket rate is 20")
