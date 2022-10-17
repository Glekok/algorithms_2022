"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы Python

На каждый скрипт нужно два решения - исходное и оптимизированное.

Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler

Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler

Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.


ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.

Это файл для первого скрипта
"""
from memory_profiler import profile
from numpy import array
from pympler.asizeof import asizeof
from sys import getsizeof


@profile()
def add_dict(n):
    my_dict = {}
    for el in range(n):
        my_dict[el] = el
    return my_dict


@profile()
def add_dict_optimized(n):
    my_tuple = tuple(el for el in range(n))
    return my_tuple


print(f"Размер словаря >>> {getsizeof(add_dict(100500))}")
# Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#     39     31.2 MiB     31.2 MiB           1   @profile()
#     40                                         def add_dict(n):
#     41     31.2 MiB      0.0 MiB           1       my_dict = {}
#     42     39.2 MiB      0.1 MiB      100501       for el in range(n):
#     43     39.2 MiB      8.0 MiB      100500           my_dict[el] = el
#     44     39.2 MiB      0.0 MiB           1       return my_dict
#
#
# Размер словаря >>> 5242976

print(f"Размер кортежа >>> {getsizeof(add_dict_optimized(100500))}")

# Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#     47     31.3 MiB     31.3 MiB           1   @profile()
#     48                                         def add_dict_optimized(n):
#     49     35.4 MiB      4.1 MiB      201003       my_tuple = tuple(el for el in range(n))
#     50     35.4 MiB      0.0 MiB           1       return my_tuple
#
#
# Размер кортежа >>> 804048

"""
В данном задании произвёл оптимизацию скрипта заполняющего словарь значениями, путём 
размещения данных в кортеж, который сам по себе имеет меньший размер на выходе + само 
заполнение расходует меньшее количество памяти. Эффект заметен при достаточно больших вводных
данных!
"""
