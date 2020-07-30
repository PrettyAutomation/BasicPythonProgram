import os
import copy
str1 = 'pretty beware sanwale'

for i in range(0, len(str1)):
    count = 1
    for j in range(i+1, len(str1)):
        if str1[i] == str1[j]:
            count = count + 1
            str1 = str1[:j] + '0' + str1[j+1:]

    if count > 1 and str1[i] != '0':
        print('{} and {}'.format(str1[i] + ' duplicate times is ',  count))


tuple1 = (1, 2, 4, [5, 6, 8])
tuple1[3][2] = 4

old_list = [1, 2, 3, 4, [2,3]]
new_list = copy.deepcopy(old_list)
new_list[4][1] = 'b'
print(old_list)
print(new_list)

print(tuple1)

stream = os.popen('pwd')
output = stream.readlines()
print(output)

list1 = [2, 3, 4]


def foo(item):
    print(item*3)


def my_func(fun, list1):
    for item in list1:
        fun(item)


my_func(foo, list)








