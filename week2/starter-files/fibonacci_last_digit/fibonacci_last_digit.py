# Uses python3
import sys

# dic = {}
# def calc_fib(n):
#     if (n <= 1):
#         return n
#
#     if not n in dic:
#         dic[n] = (calc_fib(n - 1) + calc_fib(n - 2)) % 10
#     return dic[n]


def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current) % 10

    return current


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
