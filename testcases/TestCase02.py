from array import array

from utilclass.Util02 import *


class TestCase02:
    pass
# Quick sorting for array taking arguments from the terminal
    arr01 = array('i', [])
    n = int(input('how many element in array'))
    for i in range(n):
        arr01.append(int(input('enter elements:')))
    quick_sorting(arr01, 0, len(arr01) - 1)
    print(arr01)


# Method to perform bubble sorting

    arr02 = array('i', [])
    n = int(input("enter the no. of elements in array"))
    for i in range(n):
        arr02.append(int(input("enter the elements: ")))
    bubble_sorting(arr02)
    print(arr02)


# Method to create Fibonacci series
    n1 = int(input('enter the no. for which fibonacci series has to create'))
    sum = print_fibonacci_series(n1)


# Method to find factorial of given no.
    n1 = int(input('enter element to find the factorial of it'))
    factorial = print_factorial(n1)
    print(factorial)


# Method to check the no. is prime
    n1 = int(input('enter the element to check prime'))
    check_prime_number(n1)

# Method to find the maximum and minimum no. present in array
    list1 = [2, 4, 7, 1, 89, 23, 12, 10]
    arr01 = array('i', [2, 4, 7, 0, 100, 23, 12, 10])
    find_max_elem(list1)
    find_max_elem(arr01)

# Method to use the generator
    dict01 = {"java": 'language', 'indore': 'city', 'banana': 'fruit'}
    output1 = new(dict01)
    print(output1)
    print(next(output1))
    print(next(output1))
    print(next(output1))
    # print(next(output1))

    output2 = my_func(6)
    print(output2)
    print(next(output2))
    print(next(output2))
    # print(next(output2))

    output3 = my_func01(5)
    print(output3)
    print(next(output3))
    print(next(output3))
    print(next(output3))














