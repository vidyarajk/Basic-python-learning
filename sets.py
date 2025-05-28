text="we are counting unique words in sets"
new=set(text.split())
print(new)
print(len(new))
packed_tuple=1,'vidya',2.15
print(packed_tuple)
a,b,c=packed_tuple
print(a)
print(b)
print(c)
tpl=((1,2,3),(4,5,6),("a","b"),(True,False))
for tuple in tpl:
    for x in tuple:
        print(x,end=" ")
    print()    