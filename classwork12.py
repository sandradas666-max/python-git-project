import re
try:
    title=input("enter book title:")
    year=input("enter year of publication:")
#only alphabets and spaces
    if not re.fullmatch(r"[A-Za-z ]+", title):
        raise ValueError("Title must contain only alphabets and spaces.")
#year must be a 4-digit number starting with “19” or “20”
    if not re.fullmatch(r"(19|20)\d{2}", year):
        raise ValueError("Year must be a 4-digit number starting with '19' or '20'.")
    print("Book title:",title)
    print("'Year of publication:",year)
except ValueError as e:
    print("Error:", e)
finally:
    print("Program execution completed.")