import random
import math
names=input("Enter guest names seperated by commas:")
#split the names
name_list=names.split(",")
#remove extra spaces and duplicates
unique_names = list(set(name.strip() for name in name_list))
#select a random name
selected_name = random.choice(unique_names)
#reverse the selected name
reversed_name = selected_name[::-1]
#count the unique names
total_names = len(unique_names)
#calculate and round the sqaure root
result = round(math.sqrt(total_names))

print("name list:-",name_list)
print("unique names:-",unique_names)
print("selected name:-",selected_name)
print("reversed name:-",reversed_name)
print("total names:-",total_names)
print("result is:-",result)


