#while loop

count=0
while (count<3):
    print('hello pretty')
    count = count + 1
print('--------------------------------------')

# while loop with else condition
num = 0
while(num <3):
    print('hello python')
    num = num+1
else:
    print('bye python')

print('--------------------------------------')

#for loop
name = ['pretty', 'madhu','sudan','gt','sushil']
for i in name:
    print (i)

print('--------------------------------------')

str = "i love my india"
for i in str:
    print(i)
print('--------------------------------------')

#for loop with range function

list = ["i", "am", "learning", "python"]
for i in range(len(list)-1):
    print (list[i])
print('--------------------------------------')

#for loop with else
citylist = ['banglore','newyork','london', 'paris']
for i in range (len(citylist)-2):
    print (citylist[i])
else:
    print ('citylist is over')
print('--------------------------------------')

#Nested for loop

for i in range (5):
    for j in range(i):
        print(i, end='')
    print()
















