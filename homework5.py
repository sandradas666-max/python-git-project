
Frontend = {"Sandra", "Soorya", "Arun", "John"}
Backend = {"Arun", "John", "Maya", "Varun"}


Backend.add("Anjali")
print("Backend students:", Backend)


Frontend.remove("Soorya")
print("Frontend students:", Frontend)


print("Students in both courses:", Frontend & Backend)


print("Only Backend students:", Backend - Frontend)


all_students = Frontend | Backend
print("Total unique students:", len(all_students))


courses = {
    "Frontend": len(Frontend),
    "Backend": len(Backend)
}
print("Course details:", courses)


for course_name, students in courses.items():
    print(f"Course: {course_name}, Students: {students}")


fullstack_courses = {
    course_name: students
    for course_name, students in courses.items()
}
fullstack_courses["Fullstack"] = courses["Frontend"] + courses["Backend"]

print("Final course details:", fullstack_courses)
