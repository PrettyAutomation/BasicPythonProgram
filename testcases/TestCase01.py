from utilclass.Util01 import *
# Note : If any function does not return any value then by default it will return None in python if we print it.


class TestCase01:
    def __init__(self):
        pass
    data = reverse_string("pretty beware sanwale")
    print(data)

    flag = count_substring('get***set**get**', "get", "set")
    print(flag)

    print(convert_case_of_string("pretty"))

    print(to_find_index('On the other hand, you have different fingers.', 'hand'))

    convert_to_digit("56")

    duplicate_char('I am learning java')


