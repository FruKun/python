import functools
import random

from typing import List

# Модифицируйте код декоратора prime_filter
def prime_filter(func):
    """Дан список целых чисел, возвращайте только простые целые числа"""
    def simple(a):
        b=[]
        for i in a:
            k = 0
            for j in range(2, i // 2 + 1):
                if (i % j == 0):
                    k = k+1
            if (k <= 0):
                b.append(i)
        return b
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return simple(func(*args, **kwargs))
    return wrapper

@prime_filter
def numbers(from_num, to_num):
    return [num for num in range(from_num, to_num)]

# вывод для примера
print(numbers(from_num=2, to_num=20)) 
