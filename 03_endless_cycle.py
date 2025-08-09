from random import randint


def division(divident, divisor):
    if divident != 0 and divisor != 0:
        return divident/divisor


if __name__ == '__main__':
    while True:
        a = randint(-100, 100)
        b = randint(-10, 10)
        result = division(a, b)
        print(result)
