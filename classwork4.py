fruits=["apple","mango","banana"]
vegetables=["carrot","cucumber","tomato"]
beverages=["tea","coffee","mango juice"]

fruits.append("orange")
print(fruits)

vegetables.insert(1,"onion")
print(vegetables)

beverages.pop()
print(beverages)

inventory=[fruits,vegetables,beverages]
print(inventory)

print(fruits[:2])
print(vegetables[-1])

fruits_len=[len(fruit) for fruit in fruits]
print(fruits_len)

print("Water" in beverages)

first_item=(fruits[0],vegetables[0],beverages[0])
print(first_item)

