squares={}
for x in range(5):
    squares[x]=x**2
print(squares)


square={x:x**2 for x in range(5)}
print(square)


even={x:x**2 for x in range(10) if x%2==0}
print(even)

numbers=[1,2,2,3,4,4,4,5,5]
frequency={}
for x in numbers:
    frequency[x]=numbers.count(x)
print(frequency)

frequencies={x:numbers.count(x) for x in numbers}
print(frequencies)

#merged dictionaries
dict1={"a":1,"b":2}
dict2={"b":3,"c":4,"d":3}
merged_dict={**dict1,**dict2}
print(merged_dict)