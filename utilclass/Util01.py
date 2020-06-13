class Util01:
    pass


# Method to reverse a string by words
def reverse_string(str0):
    print('reverse of full string is : ' + str0[::-1])
    str1 = ''
    str_arr = str0.split(" ")
    print(str_arr)
    for i in range (len(str_arr)):
        str1 = str1 + str_arr[i][::-1] + " "
    return str1


# Method to count the no. of substring
def count_substring(str1, word1, word2):
    if str1.count(word1) == str1.count(word2):
        return True
    else:
        return False


# Method to convert string to uppercase and lowercase after checking
def convert_case_of_string(str2):
    if str2.isupper():
        return str2.lower()
    else:
        return str2.upper()


# Method to find the index of string
def to_find_index(str3, word):
    print(str3.find(word))


# Method to convert String to Number
def convert_to_digit(str1):
    print(type(str1))
    num = int(str1) + 45
    print(type(num))


# Method to find duplicate no. of char in string
def duplicate_char(str1):
    for i in range(0, len(str1)):
        count = 1
        for j in range(i+1, len(str1)):
            if str1[i] == str1[j]:
                count = count + 1
                str1 = str1[:j] + '0' + str1[j+1:]

        if count > 1 and str1[i] != '0':
            print('{} and {}'.format(str1[i] + " duplicate times is : ", count))







