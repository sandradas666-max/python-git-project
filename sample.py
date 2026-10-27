

item_to_delete = input("Enter the item to delete: ")

f = open("items.txt", "r")
items = f.readlines()
f.close()

f = open("items.txt", "w")

for item in items:
    if item.strip() != item_to_delete:
        f.write(item)

f.close()

print("Item deleted successfully!")

f = open("items.txt", "r")
print("\nlist of items:")
print(f.read())
f.close()