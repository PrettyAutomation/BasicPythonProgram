names1 = ['Amir', 'Barry', 'Chales', 'Dao']
if 'amir' in names1:
    print(1)
else:
    print(2)


names1 = ['Amir', 'Barry', 'Chales', 'Dao']
names2 = [name.lower() for name in names1]
print(names2[2][0])


num1 = 5
if num1 >= 91:
    num2 = 3
else:
    if num1 < 6:
        num2 = 4
    else:
        num2 = 2
x = num2 * num1 + 1
print(x, x % 7)




