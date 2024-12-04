from sortfunc import *


data_1 = list(map(int, input('Введите числа через пробел: ').split()))
data_2 = list(map(int, input('Введите числа через пробел: ').split()))

bubble_sort (data_1)
selection_sort (data_2)
print()
print('Пузырьковая сортировка', data_1)
print('Сортировка выбором', data_2)
