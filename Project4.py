#Задана рекуррентная функция. Область определения функции – натуральные числа. Написать программу сравнительного вычисления данной функции рекурсивно и итерационно. 
#Результаты сравнительного исследования времени вычисления представить в табличной и графической форме.
#ВАРИАНТ 20: F(1) = 1, F(2) = 1, F(n) = (-1)n*(F(n-2)/(2n)!), при n > 2

import time
import math

def recursive_F(n):
    if n == 1 or n == 2:
        return 1
    else:
        return ((-1)**n) * (recursive_F(n - 2) / math.factorial(2 * n))

def iterative_F(n):
    if n == 1 or n == 2:
        return 1
    else:
        f_prev_prev = 1
        f_prev = 1
        for i in range(3, n + 1):
            f_curr = ((-1)**i) * (f_prev_prev / math.factorial(2 * i))
            f_prev_prev = f_prev
            f_prev = f_curr
        return f_curr

def compare_ex_time():
    n_values = [int(input(f'Введите 5 натуральных чисел : {_+1}')) for _ in range(5)]  

    recursive_times = []
    iterative_times = []

    for n in n_values:
        start_time = time.time()
        recursive_result = recursive_F(n)
        end_time = time.time()
        recursive_times.append(end_time - start_time)

        start_time = time.time()
        iterative_result = iterative_F(n)
        end_time = time.time()
        iterative_times.append(end_time - start_time)

        print(f"n = {n}: Recursive F(n) = {recursive_result}, Iterative F(n) = {iterative_result}")

    print("\nСравнение времени выполнения (в секундах):")
    print(" n   | Рекурсивно | Итерационно")
    print("--------------------------------")
    for i in range(len(n_values)):
        print(f"{n_values[i]:3}  | {recursive_times[i]:10f} | {iterative_times[i]:11f}")

    import matplotlib.pyplot as plt

    plt.plot(n_values, recursive_times, label='Рекурсивно')
    plt.plot(n_values, iterative_times, label='Итерационно')
    plt.xlabel('Значение n')
    plt.ylabel('Время выполнения (секунды)')
    plt.title('Сравнение времени выполнения рекурсивного и итерационного подходов')
    plt.legend()
    plt.show()

compare_ex_time()
