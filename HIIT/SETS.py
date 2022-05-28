# set_1 = (1, 2, 4, 6, 7)
# set_2 = (1, 4, 2, 6, 7)
# print(set_1 == set_2)
# # Sets
# # names = ["stanley", "david", "benedict", "vincent", "ruby"]
# # A set is a collection whic ic unoredered, unchangeable, and unindexed
# # Note: Set items are unchangeable but you can remove items and add new items.
# # Sets don't allow duplicate values.
# # The set() constructor

# names = set(("stanley", "david", "benedict", "vincent", "ruby"))
# print(names)

# #  add items
# #you can add an item to a set by jusing the add() method
# first_name = {"stanley","david", "benedict"}
# second_name = {"vincent","ruby","stanley"}
# print(first_name + second_name)

# # Remove set items
# # To remove an item in a set use the remove() method or discard() method,

# first_names = {"stanley","david", "benedict"}
# second_names = {"vincent","ruby","stanley"}
# first_names.remove("stanley")
# first_names.discard("stanley")# removes both vitems
# print(first_names)


# # The pop() method
# # The pop () method removes the last item but since sets are unoredered and you eventually don't
# # know what item will be poped out.

# first_names = {"stanley", "david", "benedict", "vincent", "ruby"}
# first_names.pop()
# print(first_names)

# # The clear() method
# # The clear () empties the set
# first_names = {"stanley", "david", "benedict", "vincent", "ruby"}
# first_names.clear()
# print(first_names)

# # Add and del keyword will delete the set completely
# first_names = ("stanley", "david", "benedict", "vincent", "ruby")
# del first_names
# print(first_names)

# # Loop items
# # you can loop through the set items by using a loop
# first_names = ("stanley", "david", "benedict", "vincent", "ruby")
# for x in first_names:
#     print(x)

# # Join sets
# # the union() method returns a new set with all items from both sets:
# first_names = ("stanley", "david", "benedict", "vincent", "ruby")
# second_names = ("vincent","ruby")
# all_names = first_names.union(second_names)
# print(all_names)

# # The update() method inserts the items in second_names into first_names:
# first_names.update(second_names)
# print(first_names)

# # note: Both union() and update() will exclude any duplicate items.

# # Keep only the duplicate
# # The intersection_update() method will keep only the values present in both sets.
# #first_names = {"stanley", "dangvid", "benedict"}
# #second_names = {"vincent", "ruby", "david"}
# #first_names.intersection(second_names)
# #print(first_names)# bringing out similar factors


# # difference is talks about what is in the first set that isnt in the second set
# first_names = {"stanley", "david", "benedict"}
# second_names = {"vincent", "ruby", "david"}
# first_names.difference(second_names) 