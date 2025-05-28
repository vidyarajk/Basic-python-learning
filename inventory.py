inventry=["banana","guava","apple","orange"]
inventry.append("grapes")
inventry.remove("banana")##out of sock
item="banana"
if item in inventry:
    print(f"{item} is in stock")
else: 
    print(f"{item} is out of stock")
print(f"Inventory list:{inventry}")