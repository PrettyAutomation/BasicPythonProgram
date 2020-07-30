
str1 = 'dddmmpddyy' + 't'
count = 0
output = ''
i = 0

while i < len(str1)-1:
    ch = str1[i]
    while 'true':
        if ch is not str1[i]:
            break
        count = count + 1
        i = i+1
    i = i-1
    output = output + str1[i] + str(count)
    count = 0
    i = i + 1

print(output)





