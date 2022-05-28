"""Dictionaries"""

#Exercise
# write a program to enter names of Hiit python students and their schools as input
#and store them in a dictionary


# Python Dictionaries
# Dictionaries are used to store data values in key: value pairs. A dictionary is a collection
# which is ordered, changeable and do not allow duplicates.

#details = {
#   "names": "stanley",
#   "phone": 8011,
#   "city": "abuja",
#   "city": "lagos",
#}
#print(details)

# To get the value key from a dictionary, you are to use the get() method.
#city = details.get("city")
#print(city)

# To get all keys in a dictionary, you use the keys() method.
#print(details.keys())

#To get a list of all the values in a dictionary, you use the values() method.
#print(details.values())

# To get each item in a dictionary, as tuple in a list, you use the items() method. 
#print(details.items())

# Check if key exists
# To determine if a specified key is present in a dictionary use the "in" keyword

#details = {
#   "names": "stanley",
#   "phone": 8011,
#   "city": "abuja",
#}
#if "phone" in details:
#    print("Yes phone is present")
#else:
#    print("phone is not present")
    
    # Change values
#    details["city"] = "lagos"
#    print("details")
    
    # To update dictionary
#    details.update({"phone:9011"})
#print(details)

# Adding Items
#details["career"] = "software engineer"
#print(details)

#Loop dictionary
#details =  {
#   "names": "stanley",
#   "phone": 8011,
#   "city": "abuja",
#}
#print all the key names in the dictionary
#for x in details:
#    print(x)
# or
#for x in details.keys():
#    print(x)

#print all the values names in the dictionary
#for x in details:
#    print(details[x])
# or
#for x in details.values():
#    print(x)
 


# details = {}
# while True:
#     name = input('what is the student name?\n')
#     school = input('what is the student school?\n')
#     details[name] = school
#     print(details)
#     val = input('enter 1 to continue or 2 to break out\n ')
#     if val == "1":
#         name = input('what is the student name?\n')
#         school = input('what is the student school?\n')
#         details[name] = school
#         print(details)
#     else:
#         break
# print(details)
