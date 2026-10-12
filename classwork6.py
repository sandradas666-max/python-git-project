attendances = [18, 20, 19, 15, 21]
full_days=0
total=0
for attendance in attendances:
    total=total + attendance
    print(attendance) 
    
    if attendance >= 20:
        print("The class was full")
        full_days +=1
    else:
        print("The class was not full")
        
print("Full days:", full_days)


print("total attendace is:",total)
    
    
    