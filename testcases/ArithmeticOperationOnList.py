# Squared in list
list1 = [4, 6, 1, 2, 5, 6]
squaredList = [x**2 for x in list1]
print(squaredList)

# conversion in dict
dict_list = {x: x**2 for x in list1}
print(dict_list)

# combining multiple list in one
a = [1, 2, 3]
b = [5, 6, 7]

combined_List = [(x+y) for (x, y) in zip(a, b)]
print(combined_List)
print(a + b)

