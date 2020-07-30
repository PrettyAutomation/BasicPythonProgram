confusion = {}
confusion[1] = 1
confusion['1'] = 2
confusion[1] += 1
sum1 = 0
for k in confusion:
    sum1 += confusion[k]
print(sum1)


names1 = ['Amir', 'Barry', 'Chales', 'Dao']
names2 = names1
names3 = names1[:]
names2[0] = 'Alice'
names3[1] = 'Bob'
sum2 = 0
for ls in (names1, names2, names3):
    if ls[0] == 'Alice':
        sum2 += 1
    if ls[1] == 'Bob':
        sum2 += 10
print(sum2)


names1 = ['Amir', 'Barry', 'Chales', 'Dao']
loc = names1.index("Edward")
print(loc)

