""" TUPLES"""
# tuples is one of the collection data type of python. it is ordered,
# unchangeable and allow duplicate values

#names = ('Stanley', 'jason','vincent','david','benedict',)
#print(names[1][4])#to print out letter by letter index [1][4] 
#collection_of_names = (('Stanley', 'jason','vincent'), ('david','benedict'))
#print(collection_of_names[1][0]) # to print out David[0] under tuple 1

## Other ways to print tuples
# names = tuples('Stanley', 'jason','vincent','david','benedict',)

""" Negative Indexing"""
#print(names[-3])
# names = ('Stanley', 'jason','vincent','david','benedict',)
# print(names[1:4])
# print(names[-1])


# """CHECK IF ITEM EXISTS"""
# #names = ('Stanley', 'jason','vincent','david','benedict',)
# #if 'david'in names:
# #    print('david exists')
# #else:
# #   print('no existence')

# """To change Tuples Values"""
# # To update values in tuples: You will convert the tuples to a list, do your changes
# #then convert back to tuples

# names = ('Stanley', 'jason','vincent','david','benedict',)
# y = list(names)
# #y[1] = "Goliath"
# y.append('oma') # Append Method
# names = tuple(y)
# print(names)

# """Adding Tuples to Tuples"""
# names = ('Stanley', 'jason','vincent','david','benedict',)
# y = ('oma',) # adding names to a Tuples (',')
# names = names + y
# print(names)

# """DELETE TUPLES"""
# #names = ('Stanley', 'jason','vincent','david','benedict',)
# # del names
# # print(names)

# """UNPACK TUPLES"""
# # packing Tuples simply means the normal assigning of values into a tuple
# # Example:
# #names = ('Stanley', 'jason','vincent','david','benedict',)
# #(first,second,third,fourth,fifth) = names # You could use alphabets too!
# #(a,*b) = names
# #print(b)

# # USSING A WHILE LOOP
# #names = ('Stanley', 'jason','vincent','david','benedict',)
# #i = 0 # countyer
# #while i < len(names):
# #    print(names[i])
# #    i = i + 1 # increment also i=+1

# ## MULTIPLY TUPLES
# names = ('Stanley', 'jason','vincent','david','benedict',)

# """EXERCISE"""
# # Loop through this tuple, then if any value is having the letter 'O", store in a newlist

# names = ('oma','owa','ondo','lime','mike')
# names_with_o = []
# for x in names:
#     if 'o' in x:# x is every item in the tuple
#         names_with_o.append(x)# assigning values to the new list
# print(names_with_o)


# X AND O
board = [[0,0,0],
        [0,0,0],
        [0,0,0]]
#print(board)
for  row in board:
    for col in row:
        print(col,end='')
    print('')

