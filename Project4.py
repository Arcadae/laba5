"""
Задана рекуррентная функция. Область определения функции – натуральные числа. Написать программу сравнительного вычисления данной функции рекурсивно и итерационно. 
Результаты сравнительного исследования времени вычисления представить в табличной и графической форме.
ВАРИАНТ 20: F(1) = 1, F(2) = 1, F(n) = (-1)n*(F(n-2)/(2n)!), при n > 2
"""

import timeit
from functools import lru_cache
import matplotlib.pyplot as plt

@lru_cache(maxsize = 1000)
def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

def recursive_F(n):
    if n == 1 or n == 2:
        return 1
    else:
        return ((-1)**n) * (recursive_F(n - 2) / factorial(2 * n))

def iterative_F(n):
    if n == 1 or n == 2:
        return 1
    else:
        f_prev_prev = 1
        f_prev = 1
        for i in range(3, n + 1):
            f_curr = (f_prev_prev / factorial(2 * i))*(-1)
            f_prev_prev = f_prev*(-1)
            f_prev = f_curr
        return f_curr

def compare_ex_time(list):
    
    recursive_times = []
    iterative_times = []

    for n in list:
        start_time = timeit.default_timer()
        recursive_result = recursive_F(n)
        recursive_times.append(timeit.default_timer() - start_time)

        start_time = timeit.default_timer()
        iterative_result = iterative_F(n)
        iterative_times.append(timeit.default_timer() - start_time)

        print(f"n = {n}: Recursive F(n) = {recursive_result}, Iterative F(n) = {iterative_result}")

    print("\nСравнение времени выполнения (в секундах):")
    print(" n   | Рекурсивно | Итерационно")
    print("--------------------------------")
    for i in range(len(list)):
        print(f"{list[i]:3}  | {recursive_times[i]:10f} | {iterative_times[i]:11f}")

    import matplotlib.pyplot as plt

    plt.plot(list, recursive_times, label='Рекурсивно')
    plt.plot(list, iterative_times, label='Итерационно')
    plt.xlabel('Значение n')
    plt.ylabel('Время выполнения (секунды)')
    plt.title('Сравнение времени выполнения рекурсивного и итерационного подходов')
    plt.legend()
    plt.show()

def main():
    n_values = [int(input(f'Введите 3 натуральных чисел : {_+1}')) for _ in range(3)]
    compare_ex_time(n_values)
    
if __name__ == '__main__':
    main()
