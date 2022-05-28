
# QUESTION 1
#A company decided to give bonus of 1%  if his/her year of service
# is more than 5 years,Ask user for their salary and year of service
# and print the net bonus amount.


##  MARWADIS COMPANY  BONUS ELIGIBILITY



#years_of_service = int(input('How many years have you served for?\n'))
#Salary = int(input('enter your salary income\n'))

#if years_of_service >4:



3#  bonus = Salary*(5/100)
 # reward = Salary + bonus
 # print(reward)
#else:
# print("you are not eligible")

#PYTHON LOOP
# Python has two primitive loop commands
# the while loop and for loop

# The While Loop

# With the while loop we can execute a set of statements as long as
# condition is true.
#EXAMPLE
# print i as long as i less than 6:
#i = 1
#while i < 6:
 #   print(i)
 #   i = i + 1 #i += 1  INCREMENT

#names = ['patience','joy','oma','stanley']
#i = 0
#while i < 4:
#    print(names[i])
#    i = i + 1


## note: remeber to increment i, or else the loop will continue
# forever
# the while loop requires many



# The break statement, we can stop the loop even if the while condition is true
# Example:
# Exit the loop when i is 3:

#i = 1
#while i < 6:
#    print(i)
#    if i == 3:
#         break
#    i = i + 1


#x = 4 
#while x < 20:
#    x +=3
#    if  x == 7:
#        continue       
#print(x)


'''FOR LOOP'''
#A for loop is used for iterating over a sequence that iss either a list, a tuple, 
#a dictionary, a set, or a string)

# tuple, set etc.
#Example

#print each name in nmaes list:
#names = ['leo','bennedict','stanley','oma']
# for name in names:
#    print(names) 


#  the for loop does not require an indexing variable to set beforehand

'''Looping through a string'''
# Even strings are iterable objects, they contain a sequence of characters:
# Example:
# Loop through the letters in the word 'stanley'

# for x in "vincent"
#    print(x)



"""THE BREAK STATEMENT"""
# with the break statement we can stop the loop before it has looped through all the items:
# Example
# Exit the loop when we get to letter 'c':
#for x in 'vincent':
#    if x == 'c':
#        break
#    print(x)


# The continue statement
# with the continue statement we can stop the currrent iteration of the loop
#  and continue to the next:

#for x in 'vincent':
#     if x == 'c':
#         continue
#     print(x)



"""""THE RANGE FUNCTION ()"""
# to through a set of code a specified number of times,we can use the range()
# tghe range function returns a sequence of numbers, starting from 0 by default,
# increment by 1 (by default),and ends atr a specific number

# Example:
# using the range() function:
# for x in range(6):
#   print(x)

# The range() function defaults to 0 as a starting value, however it is possible to specify
# The starting value by adding a parameter: range(2,6), which means values from 2 to 6 (not including 6)

# Example:
# using the start parameter:
#for x in range(4,6):
#    print(x)

# The range() function  defaults to  increment the by 1, however it is posible to 
# specify the increment value by  adding a third parameter, range(2,30,3).
# Example:
# Increment the sequence with 3(default is 1)
#for x  in range(2,31,2):
#    print(x)
# Else in for Loop
# The else keywoard in a for loop specifies a block of code to be executed when the loop
# is finished

# Example
# print all numbers frm 0 to 5, and print a message when the loop has ended:
# for x in range(6):
#    print(x)
# if x == 4:
#   break
# else: ## the else statement would not work if it has a break statement.
#    print("finally finished")

"""""NESTED LOOP"""
# A nested loop is a loop inside a loop
# The 'inner loop' will be executed on the time for each iteration of the 'outer loop':
# Example

#firstgroupofnames = ['leo','bennedict','oma','stanley','vincent']
#secondgroupofnames = ['jason','david','lamido','patience','praise']

#for name in firstgroupofnames:
#    for nam in secondgroupofnames:
#        print(name,nam)

#name = input('please enter your name:')
#for x in name:
#    if 'b' in name:
#        print('you have b in your name, why?')
#        break
#    else:
#        print('nice job')
#        break

## Century Assignment  and Leap year
year = int(input("Enter a year of your choice:"))
century = year // 100
if (year %100 != 0):
    century = year + 1
print(century) 