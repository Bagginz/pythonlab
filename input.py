#Input FirstName MiddleName and LastName
first_name = str(input("Please Enter Your First Name: "))
middle_name = str(input("Please Enter Your Middle Name: "))
last_name = str(input("Please Enter Your Last Name: "))

first_name = first_name.capitalize()
middle_name = middle_name.capitalize()
last_name = last_name.capitalize()

format_name = "{first} {Mid} {last}"
print(format_name.format(first=first_name,Mid=middle_name,last=last_name))