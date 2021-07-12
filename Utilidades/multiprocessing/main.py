import multiprocessing as mp
import math
import time

result_a = []
result_b = []
result_c = []


def make_calculation_one(numbers):
    for number in numbers:
        result_a.append(math.sqrt(number ** 3))


def make_calculation_two(numbers):
    for number in numbers:
        result_b.append(math.sqrt(number ** 4))


def make_calculation_three(numbers):
    for number in numbers:
        result_c.append(math.sqrt(number ** 5))


if __name__ == '__main__':

    number_list = list(range(5000000))

    p1 = mp.Process(target=make_calculation_one, args=(number_list,))
    p2 = mp.Process(target=make_calculation_two, args=(number_list,))
    p3 = mp.Process(target=make_calculation_three, args=(number_list,))

    start = time.time()
    p1.start()
    p2.start()
    p3.start()
    end = time.time()

    time_a = result_a
    time_b = result_b
    time_c = result_c

    print('Com multi-processamento:', end-start)

    start = time.time()
    make_calculation_one(number_list)
    make_calculation_two(number_list)
    make_calculation_three(number_list)
    end = time.time()

    print('Sem multi-processamento:', end-start)

    print(result_a == time_a)
    print(result_b == time_b)
    print(result_c == time_c)
