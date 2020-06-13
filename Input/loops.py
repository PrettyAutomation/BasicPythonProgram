# while loop
count = 0
while count<3:
    print('hello pretty')
    count = count + 1
print('--------------------------------------')

# while loop with else condition
num = 0
while num <3:
    print('hello python')
    num = num+1
else:
    print('bye python')

print('--------------------------------------')

# for loop
name = ['pretty', 'madhu', 'sudan', 'gt', 'sushil']
for i in name:
    print(i)

print('--------------------------------------')

str01 = "i love my india"
for i in str01:
    print(i)
print('--------------------------------------')


# for loop with range function
list01 = ["i", "am", "learning", "python"]
for i in range(len(list01)-1):
    print(list01[i])
print('--------------------------------------')

# for loop with else
city_list = ['banglore', 'newyork', 'london', 'paris']
for i in range(len(city_list)-2):
    print(city_list[i])
else:
    print('city list is over')
print('--------------------------------------')


# Nested for loop
for i in range(5):
    for j in range(i):
        print(i, end=' ')
    print()
















