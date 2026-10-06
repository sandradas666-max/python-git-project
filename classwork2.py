book1=""" The Book Title is "Python Basics" 
and the book price is ₹450   """
book2=""" The Book Title is "Data Science Intro"
 and the book price is  ₹600    """
print(book1)
print(book2)

print("The first book title is {a} and the book price is {b}.\n The second book title is {c} and the book price is {d}".format(a='Python Basics',b='₹450',c='Data Science Intro',d='₹600'))

book1_price=450
book2_price=600

total_price=(book1_price + book2_price)
print("total book price is",total_price)

message1="Thank"
message2="You"
print(message1 + message2)

print(message1,message2,book1,book2.upper())
