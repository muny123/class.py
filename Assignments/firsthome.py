from datetime import date
 
firstname = str(input('Enter your firstname: '))
lastname = str(input("Enter your lastname: "))

# askfor year of birth
yearofbirth = abs(int(input('Enter yor year of birth: ')))

#how to get the current year
currentyear = date.today().year


# calculate the age  
age = currentyear - yearofbirth


print("Hello", firstname, lastname, "you are", age, "year old.") 
