from random import randint
from time import perf_counter

a = [randint(-10**3, 10**3) for _ in range(2*10**3+1)]

# предложенный преподавателем
def classic_simple_inserts_sort(numbers: list):
    n = len(numbers)
    for i in range(1, n):
        elem = numbers[i]  # первый элемент из неотсортированной части списка
        j = i
        while j >= 1 and numbers[j - 1] > elem:
            numbers[j] = numbers[j - 1]
            j -= 1
        numbers[j] = elem

# дополнено проверками границ отсортированной части
def if_simple_inserts_sort(numbers: list):
    n = len(numbers)
    for i in range(1, n):
        elem = numbers[i]           # первый элемент из неотсортированной части списка
        if elem < numbers[0]:       # если он меньше первого элемента в отсортированной части
            del numbers[i]          #   то удаляем из неотсортированной части
            numbers.insert(elem, 0) #   и добавляем в начало отсортированной части
        elif elem > numbers[i - 1]: # если больше последнего элемента в отсортированной части
            continue                #   то не делаем ничего, он уже на своём месте
        else:                       # и только в этом случае начинаем перебирать отсортированную часть
            j = i
            while j >= 1 and numbers[j - 1] > elem:
                numbers[j] = numbers[j - 1]
                j -= 1
            numbers[j] = elem


t1_start = perf_counter()
classic_simple_inserts_sort(a)
t1_stop = perf_counter()
print(f"Время выполнения classic_simple_inserts_sort(): {t1_stop-t1_start:.4f} c")

t2_start = perf_counter()
if_simple_inserts_sort(a)
t2_stop = perf_counter()
print(f"Время выполнения if_simple_inserts_sort(): {t2_stop-t2_start:.4f} c")