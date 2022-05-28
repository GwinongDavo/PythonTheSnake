# Iteration is the repeated executions of a set of statements... we can iterate through list, tuples and strings.
# In python we have the (1).For loop and, (2).while loop

# while loop - it executes a set of commands continuously as long as the condition is true
# it requires boolean condition in order to function
# the break keyword is used to stop the continuous command from running even if its true
# i.e 1
i = 1
while i  < 6:   # As long as this condition is true it will continue to execute.
    print(i)
    i = i + 1  # i+=1 ...always increment i or else the loop will continue forever.
# i.e 2
names = ['patience', 'leo', 'vincent', 'emeka', 'ruby']
i = 0
while i < len(names):
    print(names[i])
    i+=1
# The break statement is used to stop the loop even though the condition is true
#i.e
i = 1
while i < 6:
    print(i)
    if i == 3: # therefore it exists the loop when i = 3
        break
    i+=1
i = 0
while i < 6:
    i += 1
    if i == 4:
        continue  # basically to skip when it has gotten it's continue
    print(i)

# FOR LOOP
# A for loop is used for iterating over a sequence(that is either a list, a tuple, a dictionary, a set, or a string).
# with a for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
# print each name in the list:
names = ['leo', 'benedict', 'stanley', 'oma']
for name in names:
    print(name)

# the for loop doesn't require an indexing variable to set beforehand.
# looping through a string
# even strings are iterable objects, they contain a sequence of characters:
# loop through the letters in the word 'vincent':
for x in 'vincent':
    print(x)

# Loop through the letter in the word "Vincent"
for x in 'vincent':
    print (x)


# The break statement
# with the break statement we can stop the loop before it has looped through all the items:
# Exit the loop when we get to letter 'c':
# with the break statement we can stop the loop before it can loop through all the letters in vincent
for x in 'vincent':
    if x == 'c':   # to stop the loop whenit reaches letter 'c' in 'vincent'
        break
    print(x)


# The continue statement
# with the continue statement we can stop the current iteration of the loop, and continue with the next:
# with the continue statement we can skip the letter in the if condition before looping out
for x in 'vincent':
    if x == 'c':  # to skip letter 'c' in 'vincent' but continue looping through the rest of the letters
        continue
    print(x)

# the range() function
# to loop through a set of code a specified number of times, we can use the range() function.
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default)
# and ends at a specified number
# using the range() function:
for x in range(6):
    print(x)

# using the start parameter:
for x in range(2, 6):
    print(x)

# The range() function defaults to increment the sequence by 1, however it is possible to specify the increment
# value by adding a third parameter: range(2, 30, 3).
# increment the sequence with 3(default is 1)
for x in range(2, 30, 2):
    print(x)

# Else in for loop
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished.
# print all number from 0 to 5, and print a message when the loop has ended.
for x in range(6):
    print(x)
else:
    print('finally finished')



# note te else block will not be executed if the loop is stopped by a break statement
for x in range(6):
    if x == 4:
        break
    print(x)
else:
    print('finally finished')


# nested loop - is a loop inside a loop.The 'inner loop' will be executed one time for each iteration of the 'outer loop'
# print each first grop of name for every second group of names
first_group = ['leo', 'vincent', 'obinna', 'oma','stanley']
second_group = ['jason', 'david', 'lamido','praise']
for name in first_group:
    for nam in second_group:
        print(name,nam)

# Example 2
# A program to check each letter of an input of a name entered  
name = input('please enter your name\n')
for x in name:
    if 'b' in name :
        print('why')
        break
    else:
        print('Nice job')
        break
   


