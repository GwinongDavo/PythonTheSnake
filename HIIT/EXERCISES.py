


#write a python program to check the validity of Password 
#input by users 
#validation: minimum lenght 5 characters 
#maximum length 10 characters 
#at least 1 number between [0-9]
#at least 1 letter between [a-z]
#and 1 letter between [A-Z]

#Multiplication Code
# 1

#num = int(input("Enter your number:"))

#print("Multiplication Table of",num)
#for i in range(1, 11):
 #print(num,"x",i,"=",num*i)



## REgex Method
#import re # using re.search to check validation of alphabets,digits or specil characters
#p = (input("Enter your password:"))
#x = True
#while x:
#     if(len(p)<5 or len(p)>10):
#         break#  the external condition triggering the loops termination
#     elif not re.search("[a-z]",p):# else if
#         break
#     elif not re.search ("[A-Z]",p):
#         break
#     elif not re.search  ("[0-9]",p):
#         break

#     else:
#         print("Valid password")
#         x = False
#         break
#if x: 
#    print("Not a valid Password")



#print("you are welcome to your login platform".upper())

#username = input("enter your username:\n")


## Exercise 
# define a function that accepts roll numbers and returns 
# wether the student is present or not
# define a function which counts vowels and consonants in a word
# define a function to find the average of a list
# what is the difference between a parameter and an argument
# write a simple lambda function that takes three parameters and calculates 
# their products.
# 
 
## DAVIDS EXERCISE

# number 1
# list = [1, 2, 3, 4, 5]
# user = int(input('Enter your roll number: '))
#
#
# def roll_number():
#     for x in list:
#         if user in list:
#             print('Present')
#         else:
#             print('Absent')
#         return x
#
# roll_number()


# Number 2
# def average():
#     list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     for x in list:
#         add = sum(list)
#         avg = add / x
#     return avg
#
# print(average())


# # Number 3
# word = input('Enter your word: ')
# vowel = ['a', 'e', 'i', 'o', 'u']
# def words():
#     count1 = 0
#     count2 = 0
#     for x in vowel:
#         if x in word:
#             count1 += 1
#
#         else:
#             count2 += 1
#
#     print('vowel in word is', count1, 'and consonant in word is', count2)
# words()

# Number 4
# parameters are variables listed inside a function
# def par(a, b):
#    print(a,b)
# par(3, 2)
# arguments are values that are sent to the values when called


# # Number 5
# par = lambda x, y, z: x * y * z
# def par(x,y,z):
#     return x*y*z
#
# print(par(4,5,6))
#


 


### i didnt use functions yet as i am still having questions on it




# 2 
#number2 = input("Please enter any word as you wish:")
#vowels = 0
#consonants = 0

#for x in number2:
#        if(x == 'a'or x =='e'or x == 'i'or x == 'o'or x== 'u'
#        or x=='A'or x=='E'or x=='I'or x== 'O'or x=='U'):
#          vowels = vowels+1
#else:
#       consonants = consonants+1# counters

#print("the number of vowels:",vowels)
#print("\n the number of consonants:",consonants)          


# 3
#list = [1,2,3,4,5]
#sum1=0
#avg=0
#n = len(list) # total length of the list
#for i in list: # calculating sum of elements in list
#   sum1 = sum1 +i
#   avg = sum1/n # Average is sum1/lenght of the list
#print("average of list:",avg)



# parameters are varaibles we can define in the function declaration
# the arguments are the variables to the function for the execution


#x = lambda a,b,c: a*b*c
#print(x(5,6,2))

## Exercise2
# define a function called cube that takes an argument called number
# make that function return the cube of that number i.e (that number
# multiplied by itself once again)
# define a second function called by_three
#that takes an argument called number. if that number is divisible by 3.
# the function by_three should call cube(number) and return its results
# otherwise by_three should return False.




# accepts a value from a user then the function would multiply the value by 2
# then make the value a global scope

# x = int(input( "enter a number:"))

# def func():
#     global x# whenever you go outside the function it woukd always be accesible
#     x = x*2
#     return x

# func()# because if you dnt call the fnction ur fnction wont run
# print(x)#   


"""CODING STYLE"""
# your function name should be descriptive
#joining two names use the underscore
# print(add.__doc__)m for documentation
#print( # function _name.__doc__)
# theres a package for organizing ur code it is called black


# def add(num1,num2):


#1
#write a function to tell user if he/she is able to vote or not
#consider age of voting to be 18


# #voting system
# age = int(input("enter yyour age:"))
# def voting(*,name):
#     print(name)
# if (age >= 18):
#           print("You are eligible to vote:")

# else:
#       print("You are not eligible.") 
# voting(name = age)#

#2
#build a stock keeping program for your mum to get the list of products and price 
# use the function to calculate and return the sum

# def stock_keep():

#    product_name = []
#    price_list = []
#    number = int(input("how many products would you like to add to the list:"))
#    if number <= 0:
#        print("sorry", number, 'is not a valid number\n')
#        return stock_keep()
#    else:
#        i = 1#
#        while i <= number:#
#         product = input("what products do you want to buy?\n")
#         price = int(input("input price of the product\n"))
#         product_name.append(product)
#         price_list.append(price)
#         i = i+1# increment must always be used in a loop
#         a = 0# a represents 0 in our sum
#         for x in range(0,len(price_list)):# this represents all the items in the list
#             a = a + price_list[x]#
#         print('this is your product list',product_name)
#         print('this is the price of each product',price_list)
#         print('this is the sum of your price list',a)
# stock_keep()

# write a python function to find the max of three numbrs:





n1 = int(input("enter first number:"))
n2 = int(input("enter second number:"))
n3 = int(input("enter third number:"))
largest_num = []
n1 = []
n2 = []
n3 = []
def f():
     
    if(n1>=n2) and (n1>=n3):
     n1 =largest_num

    elif(n2>=n1)and(n2>=n3):
     n2 = largest_num
    else:
     n3=largest_num

     

print(f(largest_num))

   










# def alphabets():
    # well1 =[]
    # well2 = []
    # p1 = input("enter first word:")
    # p2 = input("enter second word:")
    # if p1 == p2:
    #   print(p1 and p2)

    # else:
    #    index = string.find(p1)
    



#  An enumeration is a collection of objects that can be retrieved one object at a time
# You can enumerate classes, class names, instances, instance names,
      


# str1 = input("please enter the first word:")
# str2 = input("enter second word:")
# for index, char in enumerate(str1):
#      print("Current character", char, "position at\n", index )
# for index, char in enumerate(str2):
#        print("Current character", char, "position at", index )
# else:

#  if str1 == str2:
