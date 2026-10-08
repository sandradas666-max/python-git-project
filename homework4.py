Web_Development=["sandra","soorya","anjali"]
Data_Science=["kavya","arun","manu"]
UI_UX_Design=["akash","vishnu","sona"]

all_participants=[Web_Development,Data_Science,UI_UX_Design]
print(all_participants)

Web_Development.append("veena")
print(Web_Development)

Data_Science.insert(1,"alex")
print(Data_Science)

UI_UX_Design.pop()
print(UI_UX_Design)

new_Data_Science=Data_Science.copy()
print(new_Data_Science)

Data_Science.clear()
print(Data_Science)

print(Web_Development[:2])

name_length=[len(name) for name in new_Data_Science]
print(name_length)

check="Asha" in Web_Development or "Asha" in new_Data_Science or "Asha" in UI_UX_Design
print(check)


final_tuple=(Web_Development[0],new_Data_Science[0],UI_UX_Design[0])
print(final_tuple)







 
 