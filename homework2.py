python_course="""A python course helps learners understand the basics of
programming, including variables, data types, operators, conditions, loops, functions,
lists, dictionaries, and file handling. It is beginner-friendly because of its simple
and readable syntax."""

print(len(python_course),"\n")

print("first character:",python_course[0],"\n")
print("last character:",python_course[-1],"\n")

print("first 50 characters:",python_course[0:50],"\n")

replaced_paragraph=(python_course.replace("python", "PYTHON"))
print(replaced_paragraph,"\n")

lower_paragraph=(python_course.lower())
print(lower_paragraph,"\n")

clean_paragraph=(python_course.strip())
print(clean_paragraph,"\n")

words=python_course.split()
print(words,"\n")

check="course" in python_course
print(check,"\n")

final="The course description is {} characters long and has {} words.".format(len(python_course),len(words))
print(final,"\n")