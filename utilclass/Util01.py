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
