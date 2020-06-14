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












