"""LIST"""
#names = ['David','malik','oma','stanley','jason','Patience','Dennis']
#print(names[:6])
#Range of negative indexes
#print(names[-4:-1])

#if 'oma' in names:
#    print('oma')
#else:
   # print('she is not in your list')

#if 'victor' in names:
   # print('yeah he is in!')
#else:
#    print("nah g")

""" Inserting Items"""
#names.insert(4,'heero')
#print(names)

"""Loop list"""
#for name in names:
#    print(name)

"""loop through the index numbers"""
#for i in range(7):
#    print(i)

"""LOOP through index elements"""
#for i in range(7):
#    print(names[i])


"""LIST COMPREHENSION"""
#new_list = []
#for name in names: 
#     new_list.append(names)

#
# #for x in names:
  #  if 'e' in x:
   #     new_list.append(x)

#print(new_list)        




#new_list = [x for x in names if 'e' in x]
#print(new_list)

# SYNTAX FOR LIST COMPREHENSION
# newlist = [expression for item in iterable if condition == True]


""" SORT A LIST"""
# sort is case sensitive by default()
#names.sort(reverse = False) 
#print(names)
# if you want a case insensitive sort funciton, str.lowerr as a key func.
#names.sort(key = str.lower)
#print(names)


""" To Reverse The Order Of List"""
#names.reverse()
#print(names)
# To copy a list
#namez = names.copy
#print(namez)
#namez = list(names)
#print(namez)


""" How to Join a list"""
#Firstlist = ['pati','mati','big batty','leti']
#secondlist = ['joy','dennis','vincent']
#all_namez = Firstlist+secondlist
#print

#for x in secondlist:
#   Firstlist.append(x)

#  print(First)
   
""" EXAMPLE COMPLEX SORTING"""
#values = [2,3,4,5,6,7,8,90,100,101,7,13]
#even = []
#odd =[]
#outliers = []
#for value in values:
#   if value % 2 == 0: 
#     even.append(value)
#   elif value >= 90:
#      outliers.append(value)  
#   else:
#      odd.append(value)
#print('even are:', even)
#print('outliers are:',odd)
#print('outliers are:',outliers)

""" EXERCISE"""
# Create a single registration system, you will accept the users surname password
# print yoy are welcome to the platfrm
# and passwrd woould be stored in a mini data base or list
          
#username = input('enter your surname\n')
#password = input('enter your password\n')
#loginpasswrd = []
#loginname = []
#loginpasswrd.append(password)
#loginname.append(username)
#print('you are welcome billy the goat!\n')
#print(loginname)
#print(loginpasswrd)r


#class_members = ['Vincent','Stanley','Emeka','David','Patience','Praise','Oma','Jason']
#name = input('what is your name\n')
#if name in class_members:
#   print('you are eligible for the class')
#else:
#   print('not found')



""" [ Expression for elements in iterable if condition]"""
#num = [ 2,4,5,6,8,9]
#even = []
#odd = []
#for x in num:
#   if x % 2 == 0:
#      even.append(x)
 #  else:
#      odd.append(x)
#print(odd,even)

      
















