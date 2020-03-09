print('hello world')

value = input('enter the number: ')
print(value)
print(value.isnumeric()) #False
value = input('enter the number: ')
print(int(value))
print(value.isnumeric())   #True

x, y = input('Enter two integer value: ').split()
print(x,y)
