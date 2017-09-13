# Uses python3
import sys

dic = {}

def pre_calc_fib(n):
    if (n <= 1):
        return n

    for i in range(n):
        calc_fib(i, False)

def calc_fib(n, pre):
    if (n <= 1):
        return n

    if pre:
        pre_calc_fib(n - 1)

    if not n in dic:
        dic[n] = calc_fib(n - 1, False) + calc_fib(n - 2, False)

    return dic[n]

def fibonacci_partial_sum(n, m):
    sum = 0
    for i in range(n, m+1):
        sum = (sum + calc_fib(i, True)) % 10

    return sum

if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum(from_, to))
