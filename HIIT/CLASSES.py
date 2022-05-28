"""""CLASSES"""
# a function inside of a class is called a method.
# a class is a blue print of an actual method.
# methid is da behaviour
# attributes are the properties of the class

# class HumanBeing:

#          height = 6
#          weight = 120
#          gender = "Male"
# def walk(self):


# class Mygee:
#  x = input("enter your age:")

# p1= Mygee()
# print("your age is",p1.x
# ort turtle

# class Polygon:
#     def __init__(self,sides,name,size = 100,color = "blue"):
#         self.sides = sides
#         self.name = name
#         self.size = size
#         self.color = color
#         self.interior_angles = (self.sides - 2)*180
#         self.angle = self.interior_angles/self.sides
#     def draw(self):# passed in self to access the parrameters(sides,name)
#      for i in range(self.sides):
#          turtle.color(self.color)
#          turtle.forward(self.size)
#          turtle.right(180 -self.angle)
#          turtle.done()

# def draw_function(sides,color,size,angle):

#  turtle.color(color)
#  turtle.forward(size)
#  turtle.right(180 -angle)
#  turtle.done()


# square = Polygon(4,"square")
# pentagon = Polygon(5,"pentagon")
# hexagon = Polygon(6,"hexagon")
# print(square.sides)
# print(square.name)
# print(square.interior_angles)
# print(square.angle)

# print(pentagon.sides)
# print(pentagon.name)      
# hexagon.draw()

# Object Oriented Programing.
# Object oriented programming is a programming paradign that provides a means
# Of structuring programming so that properties and behaviours are bundled
# into individual objects.
# Many developers use OOP because it makes your code reusable and logical.
# Methods are functions
# Classes and Objects
# A class is a blueprint of objects defining their common attributes
# and behaviour

# Inheritance
#Example:

# class Humanbeing:# first the "class" keyword  and the class name:
#   def __init__(self,height,weight,name):# for initialization a method
#       print("Hello World")
#       self.height = height
#       self.weigt = weight
#       self.name = name

# # methods are behaviours your object can peform
# # properties are the attributes/characteristics of an object.

# def walk(self):
#     print(self.name,"can walk!")

# def eat(self):
#   print(self.name, "can eat")

# jason = Humanbeing(6,7,"jason")
# jason.walk()

# praise = Humanbeing(5,6,"praise")
# praise.walk()



# class Calculator:
#     def __init__(self,firstnum,secondnum):
#         self.firstnum = firstnum
#         self.secondnum =  secondnum

#     def addittion(self):
#        return self.firstnum + self.secondnum 
    
#     def subtraction(self):
        
#      return self.firstnum-self.secondnum

# firstnum = int(input("enter your number :"))
# secondnum = int(input("enter your second num :"))    
# casio = Calculator(firstnum,secondnum)
# print(casio.subtraction())



# create a storekeeper class, the storekeeper class should have a method
# that would enable it add product to an attribute products
# class Storekeeper:
#  def add_products(self,*my_products):
#     self.products = my_products

#     self.products.append(my_products)

#     return self.products


# jason = Storekeeper()
# print(jason.add_products("spags","sugar","salt","beans"))
# # create a student class with properties total_amount, it will also 
# have a method to subtract school_fees from the total amount.
# class Student:
#    def __init__(self, schoolfees,total_amount): 

#        self.schoolfees = schoolfees
#        self.total_amount = total_amount

#    def total_sum(self):
#        return self.schoolfees - self.total_amount

# schoolfees = int(input(" how much is your school fees?:"))
# total_amount = int(input("how much is tour total amount? :"))

# fees = Student(schoolfees, total_amount)
# print(fees.total_sum())
           
# Instance Variables:
# contain data that is un ique to each instance
# class Employee:
#  def __init__(self,first,last,pay):#arguments
#    self.first = first # setting all the instance variables
#    self.last = last
#    self.pay = pay
#    self.email = first +  '.' + last + '@company.com'


#  def fullname(self):# each method within our class takes the  instance as the first argument.
#    return '{} {}'.format(self.first,self.last)


# emp1 = Employee("Jason", "Davo", 9999999999999)
# emp2 = Employee("Immanuel","Davo",1900000000000)

# print(emp1.email)
# print(emp2.email)
# # print(emp1.fullname())# Note we use parenthis here because it is a method not an attribute
# print(Employee.fullname(emp1,emp2)) # using the class name itself

# CLASS VARIABLES
# class varaibles are variables shared among all instances of a class

# class Employee:
#    numofemps = 0
#    raise_amount = 1.04

# def __init__(self,first,last,pay):#arguments
#     self.first = first # setting all the instance variables
#     self.last = last
#     self.pay = pay
#     self.email = first +  '.' + last + '@company.com'
#     Employee.numofemps +=1

# def fullname(self):# each method within our class takes the  instance as the first argument.
# #     return '{} {}'.format(self.first,self.last)

# pply_raise(self):
#     self.pay = int(self.pay *  self.raise_amount)# Calling my class variable through Instance
# # of the class ("self.raise_amount") or through the class itself.
  

# emp1 = Employee("gggg", "hehehe", 90000)

# print(Employee.numofemps)
# print(Employee.__dict__)
# print(Employee.raise_amount)
# print(emp1.raise_amount)#instances
# print(emp1.pay)
# emp1.apply_raise()
# print(emp1.pay)


# AFter creating class you creae an object 

# class Human:

#     ears = 2
#     eyes = 2
#     cars = 2
#     houses = 3

#     def walk(self):
#      print("you can walk")



# jason = Human()
# print(jason.cars)

#def init# to make your objects have its own properties.

# def __init__(self,ears,eyes,cars,houses):# u can make multiple objects using self
#       self.eyes = eyes
#       self.ears = ears
#       self.cars = cars
#       self.houses = houses



# jason = Human(2,2,2,2,)
# print(jason.cars)


# class Calculator:


#     def __init__(self,num1,num2):
#         self.num1 = num1
#         self.num2 = num2


#     def add(self):
#         return self.num1+ self.num2


#     def sub(self):
#         return self.num1 - self.num2

# ## Making an object of the class

# casio = Calculator(5,2)
# print(casio.add)       









