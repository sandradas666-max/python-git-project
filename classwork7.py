
grocery_list = ["milk", "bread", "eggs"]

def add_item(item):
    grocery_list.append(item)

def remove_last_item():
    grocery_list.pop()

display_item = lambda item: print(f"Item: {item}")

def count_characters(items):
    if len(items) == 0:
        return 0
    return len(items[0]) + count_characters(items[1:])


add_item("apple")
print(grocery_list)


remove_last_item()
print(grocery_list)


for item in grocery_list:
    display_item(item)


print("Total characters:", count_characters(grocery_list))

    