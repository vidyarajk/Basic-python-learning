my_list=[1,2,3,4,5]
iterator=iter(my_list)
#print(next(iterator))
    ### or
for i in iterator:
    print(i)

my_string="hello"
string_iterator=iter(my_string)
try:
    print(next(string_iterator))
    print(next(string_iterator))
    print(next(string_iterator))
    print(next(string_iterator))
    print(next(string_iterator))
    print(next(string_iterator))
except StopIteration:
    print("no elements for iteration")
