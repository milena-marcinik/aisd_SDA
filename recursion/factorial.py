from typing import List


def factorial(n: int):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)


def factorial_iterative(n: int):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


def sum_list_recursively(values: List[int]):
    if values:
        return 0
    else:
        return values[0] + sum_list_recursively(values[1:])


if __name__ == '__main__':
    print(factorial(0))
    print(factorial(1))
    print(factorial(2))
    print(factorial(5))
    print(factorial(6))