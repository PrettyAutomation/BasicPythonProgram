from array import array

from fact import fact


# Program to check whether no. is palindrome or not
number = '122'
number1 = number[::-1]
if number1 == number:
    print('palindrome')
else:
    print('is not palindrome')
print('-----------------------------------------------')

# Program to get the factorial using library function
num = 5
if num == 1:
    print(num)
else:
    fact_num = num * fact(num-1)
    print(fact_num)
print('-----------------------------------------------')

# Program to check the no is armstrong number
num = int(input('enter the number'))
s = 0
temp = num
while temp > 0:
    c = temp % 10
    s += c**3
    temp //= 10
if num == s:
    print('armstrong')
else:
    print('not armstrong')
print('-----------------------------------------------')

# program to use array and perform operation

a = array('i', [2, 3, 4, 5, 6, 1])
print(a)
a.pop(1)
print(a)
a.append(45)
print(a)
a.remove(6)
print(a)
a.insert(7, 33)
print(a)











