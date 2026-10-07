
receipt_header="""-------------- BOOKSTORE RECEIPT -----------
Customer Purchase Details
--------------------------"""
book1 = "Book Title: {} \t Price: {}".format("Python Basics", "₹450")
book2="Book Title: {} \t price: {}".format("Data Science Intro","₹600")

book1_price=450
book2_price=600

total_price=(book1_price + book2_price)
total = "Total Price: {}".format(total_price)

thank_you = "\nThank You for Shopping With Us!"

receipt = receipt_header + "\n" + book1 + "\n" + book2 + "\n" + total + thank_you

print(receipt.upper())


