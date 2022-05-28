# FUNCTIONS
# calling functions
#  return keyword
# parameters/arguments
#  parameters/arguments with default
# keyword parameters
# arbitrary arguments
# arbitrary keyword arguments
# lambda functions
# in built functions such as filter, map,reduce
# """

# # FUNCTIONS

# def func(): 
#     print("5")
#     print("today")
#     print("tommorow")
#     return = "gwee"


# result = func()
# print


## NORMAL METHOD
#names = ["zach","victor","vincent","victoria",]
#names_repeated = []

#for name in names:
#   names_repeated.append(name) 
  
#print(names_repeated)

# List comprehenion Approach
#another_list = [ expression loop condition:optional]
#another_list = [name for name in names]
#print(another_list)

""""
def addittion(num_1 + num_2):
    return num_1 + num_2
## DEFAULT ARGUMENT
    def greeting(name,welcomne_title ="WELCOME")
        
"""
# To define a function we use the def keyword()
#my function()
# def my_function(x,y,c):
#     return x+y, y-x, c+x-y
# print(my_function(2,3,4))


# def add(a,b): #function definition
#     print(a+b)
#
#add(6,7)#calling the function

#A function is a block of code which only runs when it is called. It is meant to perform a particular task
#You can pass data, known as parameters, into a function
#A function can return data as a result

#Creating a Function
#In Python a function is defined using the def keyword:
#Example

# def add(a,b):
#     return a+b
#
# print(add(9,10))

#calling a function
#to call a function, use the function name followed by parenthesis:
#Example
#add(9,10)

#Arguments
#Information can be passed into functions as arguments
#Example:

# def add(a,b):
#     return a+b

#a and b are arguments. You can add as many arguments as you want, just seperate them with a comma.
#The add function has just two arguments. When the function is called, we pass along values a and b which is used
#inside the fucntion to return addition of a and b
#Arguments are often shortened to args in python documentations

#Parameters or arguments
#The terms parameter and argument can be used for the same thing: information that are passed into a function

#From a function's perspective: A parameter is the variable listed inside the parentheses in the fucntion definition.
#An argument is the value that is sent to the function when it is called
 

#def student_names(*kids):# arbitrary arguments when you have no idea of the number of arguments you are adding
#    return("the second kid  is",kids[2]) #the return statement is used to return a value 

#print(student_names('malik,','jason','vincent','ruby'))


### KEYWOrd ARguments
# in key word arguments you pass in the key and the value:


# def person(name, /):
#     print(name)


# person("leo")# positional arguments you use forward slashg /

"""Keyword ARguments """
# def person(*,name):# keywrd argument use astyericvvs and comma

#      print(name)

# person(name = "leo")

"""function anotation"""
#def person(name:  str) ->str:#Another way of describing your code.
    # another way of making your function much more readable.
#    print(name.__annotations__)#what your function would accept and the result
#person(1)


# def add(a,b): # we define a function using def and a and b are the parameter
#     return a+b  # we use the return statement in function to return any expression
# print(add(3,a=9))# 4 and 9 are the arguments for the parameter a and b 

# def add(*s):
#     return 

# names = ['emma','victor','joseph']
# def myfunction(names): # function definition as parameter
#     for z in names:
#      print (z)
# myfunction(names) # function call as argument the aarguments are each values in list 
# #called name

# def add(a,b):
#    print(a+b) # the return also solves the issue but doesnt print on your console
#    # so we have to use print
# add(9,10)

# def myfunction(fname,lnmae): # parameters
#    print(fname + "   " +lnmae) #
# myfunction("emil" ,"refsness") # passed arguments


# Arbitrary arguments (*) when u dnt knw the amnt of arguments 
# that would be passed in ur function
# def viko(*rubi): #as you can see 1 parameter
#     print(viko[2])# remember to print ur function name here
# viko("vvvv","lll",'hhh')#three active arguments

""" Keyword Arguments:"""

#they are used to assign a parameter to the arguments 
# using the '=' 



# def lamido():
#     x = int(input("what is x: "))
#     if x == 3:
#         print("jason")
#     else:
#         return lamido()#the rturn keywrd returns back to square 1 untill the condition is met
#         # i.e until 3 is inserted it keeps returning what is x?
# lamido()


# def kids(child1,child2,child3):
#      print(child2)
     
# kids(child1 = "rubakat",child3 = "king" , child2 = "lolly")#
# # whenever youre using a keyword args when u call ur function
# # always equate each parma to an argument(value)


"""SCOPES"""
# local and global scope

# def add()
#   value = 2 # this value is local scope because it cnt be recognzed outside ur func
#     return value
# print (value)

"""How to make a local scope global"""
# x = 400 
# def myfunc():
#     global x 
#     x = 200
#     return x
# print(myfunc())
# print(x)


# def greet():#function defined
#     print("Hello")
#     print("Good afternoon")

#greet()#funcrion call

# def add_sub(x,y):
#      c = x + y
#      d = x-y 
#      return c,d# doesnt return any value 
#      #print(c)#   returns value
# result1,result2 = add_sub(5,4)# when returning two values you accept two values.
# print(result1,result2)


def update(x):
    x = 8
    print("x",x)
a = 10
update(a)
print("a",a)

