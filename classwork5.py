python={"sandra","soorya","arun","john"}
Data_Science={"maya","john","varun"}

python.add("anjali")
print(python)

Data_Science.remove("maya")
print(Data_Science)

print(python & Data_Science)

print(python -Data_Science)

print(python | Data_Science)

courses={
    "python":3,
    "Data_Science":5,
    "web_development":2
}

for course_name, students in courses.items():
    print(f"Course: {course_name}, Students: {students}")
    
doubled_courses = {course: students * 2 for course, students in courses.items()}

print(doubled_courses)