# import os

# item = input("Enter the name of the item: ")
# if os.path.exists("items.txt"):
#     f = open("items.txt", "a")
# else:
#     f = open("items.txt", "w")
# f.write(item + "\n")
# f.close()
# f = open("items.txt", "r")
# print("\nlist of items:")
# print(f.read())
# f.close()




import random
print("Random integer is", random.randint(0, 9))
