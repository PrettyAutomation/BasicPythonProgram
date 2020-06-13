from array import array

from utilclass.Util02 import *


class TestCase02:
    pass

    arr01 = array('i', [])
    n = int(input('how many element in array'))
    for i in range(n):
        arr01.append(int(input('enter elements:')))
    quick_sorting(arr01, 0, len(arr01) - 1)
    print(arr01)






