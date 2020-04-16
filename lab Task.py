import numpy as np
from random import randint
import timeit
def bubble1(a):
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
def bubble2(a):
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
def selection1(a):
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
def selection2(a):
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
def insertion(a):
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
def insertion2(a):
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
        try:
            flag = input("If you are lazy and want to make as in common settings press 1, otherwise press any button")
            if flag == '1':
                a = np.random.randint(-100, 100,100)
            else:
                n = int(input('Enter length of array: '))
                a = np.zeros(n, dtype=int)
                for i in range(n):
                    a[i] = randint(-100, 100)

            break
        except ValueError:
            print("Input an integer!")
print(f'Your array{a}')
check=int(input('Choose which one:\n1)Buble\n2)Selection\n3)Insertion'))
if check==1:
    order=int(input('Choose in which order \n1)Increasing\n2)Decreasing'))
    if order==1:
        compare,swap=bubble1(a)
        type='Buble.Increasing'
    elif order==2:
        compare,swap=bubble2(a)
        type='Buble decreasing'
elif check==2:
    order = int(input('Choose in which order \n1)Increasing\n2)Decreasing'))
    if order ==1:
        compare,swap=selection1(a)
        type='Selection increasing'
    elif order==2:
        compare,swap=selection2(a)
        type='Selection decreasing'
elif check==3:
    order = int(input('Choose in which order \n1)Increasing\n2)Decreasing'))
    if order==1:
        compare,swap=insertion(a)
        type='Insertion increasing'
    elif order==2:
        compare,swap=insertion2(a)
        type='Insertion decreasing'
len_arr = len(a)
print(f'Sorted array: \n {a}')
print(type)
print(f'Comparisons were done {compare} times')
print(f'Swaps were done {swap} times')
t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(f'Program worked {t} seconds')