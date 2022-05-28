""" A program that will store 
"""
# values=[]
values = [2, 3, 4, 5, 6, 7, 8, 91, 90,  103, 101, 7, 12]
even = []
odd = []
outlier = []
for i in values:
    if i % 2 == 0 :
        even.append(i)
        print(even)
    elif i >= 90 :
        outlier.append(i)
    elif i % 2 == 1:
        odd.append(i)
        print(odd) 
print(even)
print(odd) 
print(outlier) # values greater than 90

"""create a simple registration system, you will accept the user's username, password and print you are welcome to 
our platform.The user's username and password will be stored in a mini database or list that would be shown to you.
"""
# using if else with a constant username and password
database = []
username = "leovin"
password = "leo669"
name = input("enter your username\n")
code = (input('enter your password\n'))
if name == username:
    if code== password:
        print("you are welcome to our platform")
        database.append(name)
        database.append(code)
    else:
        print(" wrong authentication")
else:
    print("wrong authentication")

# straight forward to add both input to a single list
database = []
name = input("enter your username\n")
code = (input('enter your password\n'))
print("you are welcome to our platform")
database.append(name)
database.append(code)
print(database)

#storing each data on two separate list
password_list = []
username_list = []
name = input("enter your username\n")
code = (input('enter your password\n'))
print("you are welcome to our platform")
username_list.append(name)
password_list.append(code)
print(username_list)
print(password_list)

# """ create a system where you allow a user to access the system if the user is registered for the class."""
class_user = ["vincent", "david", "stanley", "emeka", "oma", "jason", "patience", "praise" ]
name = input("what is your name?\n")
if name in class_user:
    print('you are eligible for this course')
else:
    print("you are not a member")

"""
"""
# [expression for element in  iterables if condition]
num = [2, 4, 5, 6, 8, 9]
multiples_of_two = [x for x in num if x % 2 == 0]
print(multiples_of_two)

# normal way of expressing this
multiples_of_two = []
num = [2, 4, 5, 6, 8, 9]
for x in num:
    if x % 2 == 0:
        multiples_of_two.append(x)
print(multiples_of_two)

# to get a list of tuples and store the values of each tuples in a new list
number = [(1,2), (3,4), (5,6)]
num = [ num for tup in number for num in tup]
print(num)
# In the list num input those values that are multiples of two and greater than 4 in the empty list
number = [2, 4, 6, 8, 3, 1, 10, 12, 13, 15]
num = [x for x in number if  x % 2 == 0 and x > 4]
print(num)


