str01 = 'I own iphone and samsung'
output = 'I own i_Phone and Sam_Sung'

str_array = str01.split(' ')
str_array1 = []
str1 = ''

for i in range(len(str_array)):
    if str_array[i] == 'iphone':
        str_array1.append('iphone'[0] + '_' + 'iphone'[1:].capitalize())

    elif str_array[i] == 'samsung':
            index = 'samsung'.find('s')
            str_array1.append(
                'samsung'[index].upper() + 'samsung'[1:3] + '_' + 'samsung'[index].upper() + 'samsung'[4:])
    else:
        str_array1.append(str_array[i])


print(str1.join(' ' + str(str_array1)))

