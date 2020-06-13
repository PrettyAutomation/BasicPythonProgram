class Util01:
    pass


# Method to reverse a string by words
def reverse_string(str0):
    print('reverse of string using in-built function' + ''.join(reversed(str0)))
    print('reverse of full string is : ' + str0[::-1])
    str1 = ''
    str_arr = str0.split(" ")
    print(str_arr)
    for i in range(len(str_arr)):
        str1 = str1 + str_arr[i][::-1] + " "
    return str1


# Method to check the no. of 2 substring are equal
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
    try:
        print(str3.find(word))
        print(str3.index(word))
        print(str3.find('pretty'))
        print(str3.index('pretty'))
    except Exception as e:
        print(format(e))
    finally:
        print('-----------------------------------------------------------------')


# Method to convert String to Number
def convert_to_digit(str1):
    print(type(str1))
    num = int(str1) + 45
    print(type(num))
    print('-----------------------------------------------------------------')


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
    print('-----------------------------------------------------------------')


# Method to find duplicate no. of words in string
def duplicate_words(str1):
    str_array = str1.split(' ')
    for i in range(0, len(str_array)):
        count = 1
        for j in range(i+1, len(str_array)):
            if str_array[i] == str_array[j]:
                count = count + 1
                str_array[j] = '0'
        if count > 1 and str_array[i] != '0':
            print('{}{}'.format(str_array[i] + " duplicate times is: ", count))
    print('-----------------------------------------------------------------')


# Method to get the id of object (memory location of object)
def get_id():
    name = 'object'
    print('{}{}'.format(id(name), ' is memory location of object'))
    print('-----------------------------------------------------------------')


# Method to check word is start with capital letter.
# also to make the string as capitalized
def startswith_capital():
    print('The Hilton'.istitle())
    print('The hilton'.istitle())
    print('the'.istitle())
    print('{}{}'.format("the original string is: " + "the hilton", " and capitalized string is: " +
                        'the hilton'.capitalize()))
    print('----------------------------------------------------------------')


# Method to check if string contains substring
def contain_word(str1, word):
    print(word in str1)
    print('----------------------------------------------------------------')


# Method to check if string contains numbers only
def check_number_string(str1):
    print(str1.isnumeric())
    print('----------------------------------------------------------------')


# Method to convert first and last character of string to uppercase
def convert_first_last_char_upper(str1):
    print(str1[0].upper() + str1[1:-1] + str1[-1].upper())
    print('----------------------------------------------------------------')


# Method to replace all in string
def use_replace_all(str1, old, new):
    print(str1.replace(old, new))
    print('----------------------------------------------------------------')


# Method to remove vowel from string
# also to print only vowel present in string
def removal_of_vowel(str1):
    vowels = ['a', 'e', 'i', 'o', 'u']
    print(''.join([c for c in str1 if c not in vowels]))
    print(''.join([c for c in str1 if c in vowels]))
    print('----------------------------------------------------------------')






