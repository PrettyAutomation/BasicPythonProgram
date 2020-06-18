
class Unit02:
    pass


def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        while low <= high and array[high] >= pivot:
            high = high-1
        while low <= high and array[low] <= pivot:
            low = low + 1

        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high


def quick_sorting(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sorting(array, start, p-1)
    quick_sorting(array, p+1, end)


def bubble_sorting(arr):
    if len(arr) == 0:
        print('array is empty')
    else:
        for i in range(len(arr)):
            for j in range(len(arr)-1):
                if arr[j] < arr[j+1]:
                    temp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = temp
                else:
                    continue


def print_fibonacci_series(n):
    n1 = 0
    n2 = 1
    for i in range(n):
        print('{}{}'.format(n1, " "))
        sum01 = n1 + n2
        n1 = n2
        n2 = sum01


def print_factorial(n):
    n1 = 1;
    for i in range(1, n + 1):
        n1 = n1 * i
    return n1


def check_prime_number(n):
    count = 0
    for i in range(2, n):
        if n % i != 0:
            pass
        else:
            count = count + 1
    if count > 1:
        print('no is not prime')
    else:
        print('no is prime')


def find_max_elem(arr):
    print(max(arr))
    print(min(arr))


def new(dict01):
    for x, y in dict01.items():
        yield x, y


def my_func(n):
    while n <= 7:
        yield n
        n += 1


def my_func01(n):
    yield n*1
    yield n*2




























