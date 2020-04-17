import numpy as np
from random import randint
'''Підключення потрібних модулів'''
import timeit
def bubble1(a):#Створення сортування бульбашкою у зростаючому порядку
    swap=0
    compare=0
    lena=len(a)
    for i in range(1, lena):
        for j in range(lena - 1, i - 1, -1):
            compare+=1
            if (a[j - 1] > a[j]):
                a[j], a[j - 1] = a[j - 1], a[j]
                swap+=1
    return compare,swap
def bubble2(a):#Створення сортування бульбашкою у спадаючому порядку
    swap=0
    compare=0
    lena = len(a)
    for i in range(1, lena):
        for j in range(lena - 1, i - 1, -1):
            compare+=1
            if (a[j - 1] < a[j]):
                a[j], a[j - 1] = a[j - 1], a[j]
                swap+=1
    return compare, swap
def selection1(a):#Створення сортування вибіркою у зростаючому порядку
    swap = 0
    compare = 0
    lena = len(a)
    for i in range(lena - 1):
        min = i
        for j in range(i + 1, lena):
            compare += 1
            if a[j] < a[min]:
                min = j
        swap += 1
        a[i], a[min] = a[min], a[i]
    return compare, swap
def selection2(a):#створення сортування вибіркою у спадаючому порядку
    swap = 0
    compare = 0
    lena = len(a)
    for i in range(lena - 1):
        min = i
        for j in range(i + 1, lena):
            compare += 1
            if a[j] < a[min]:
                min = j
        swap += 1
        a[i], a[min] = a[min], a[i]
    return compare, swap
def insertion(a):#Створення сортування вставками у зростаючому порядку
    swap = 0
    compare = 0
    lena = len(a)
    for i in range(1, lena):
        j = i - 1
        key = a[i]
        compare+=1
        while j >= 0 and a[j] > key:
            swap+=1
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return compare, swap
def insertion2(a):#створення сортування вставками у спадаючому порядку
    swap = 0
    compare = 0
    lena = len(a)
    for i in range(1, lena):
        compare += 1
        j = i - 1
        key = a[i]
        while j >= 0 and a[j] < key:
            swap += 1
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return compare, swap

while True:
    while True:#створення масиву та вибір
        try:
            flag = input("If you are lazy and want to make as in common settings press 1, otherwise press any button")
            if flag == '1':
                a = np.random.randint(-10000, 10000, 100000)
            else:
                n = int(input('Enter length of array in range of 1 to 30 or programm wouldn`t work: '))
                a = np.zeros(0, dtype=int)
                if n <= 30:
                    a = np.zeros(n, dtype=int)
                    for i in range(n):
                        a[i] = randint(-100, 100)
                    print(f'Your array{a}')

                else:
                    print('You are above of limit')
                    break
            break

        except ValueError:
            print("Input an integer!")
    len_arr = len(a)
    if 1<=len_arr<=30 or len_arr==100000:
        check = int(input('Choose which one:\n1)Buble\n2)Selection\n3)Insertion'))  # вибір яке сортування застосувати
        if check == 1:
            order = int(input('Choose in which order \n1)Increasing\n2)Decreasing'))
            if order == 1:
                compare, swap = bubble1(a)
                type = 'Buble.Increasing'
            elif order == 2:
                compare, swap = bubble2(a)
                type = 'Buble decreasing'
        elif check == 2:
            order = int(input('Choose in which order \n1)Increasing\n2)Decreasing'))
            if order == 1:
                compare, swap = selection1(a)
                type = 'Selection increasing'
            elif order == 2:
                compare, swap = selection2(a)
                type = 'Selection decreasing'
        elif check == 3:
            order = int(input('Choose in which order \n1)Increasing\n2)Decreasing'))
            if order == 1:
                compare, swap = insertion(a)
                type = 'Insertion increasing'
            elif order == 2:
                compare, swap = insertion2(a)
                type = 'Insertion decreasing'

        print(f'Sorted array: \n {a}')  # вивід усіх тестових даниї
        print(type)
        print(f'Comparisons were done {compare} times')
        print(f'Swaps were done {swap} times')
        t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
        print(f'Program worked {t} seconds')
        result = input('Do you want to retry.If yes enter 1 if no something else')
        if result == '1':
            continue
        else:
            break

