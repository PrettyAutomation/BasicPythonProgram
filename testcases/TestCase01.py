from utilclass.Util01 import *
# Note : If any function does not return any value then by default it will return None in python if we print it.


class TestCase01:
    def __init__(self):
        pass
    data = reverse_string("pretty beware sanwale")
    print(data)
    print('-----------------------------------------------------------------')

    flag = count_substring('get***set**get**', "get", "set")
    print(flag)
    print('-----------------------------------------------------------------')

    print(convert_case_of_string("pretty"))
    print('-----------------------------------------------------------------')

    print(to_find_index('On the other hand, you have different fingers.', 'hand'))

    convert_to_digit("56")

    duplicate_char('I am learning python')

    duplicate_words('get all get up and set them up set')

    get_id()

    startswith_capital()

    contain_word("I am learning python", 'python')

    check_number_string('12234')

    convert_first_last_char_upper('fish')

    use_replace_all('Sally sells sea shells by the sea shore', 'sea', 'pretty')

    removal_of_vowel('hello world')





