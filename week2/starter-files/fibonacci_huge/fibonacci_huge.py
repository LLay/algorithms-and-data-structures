# Uses python3
import sys

dic = {}
def calc_fib(n):
    if (n <= 1):
        return n

    if not n in dic:
        dic[n] = calc_fib(n - 1) + calc_fib(n - 2)
    return dic[n]


def get_fibonacci_huge(n, m):
    period = (m ** 2) -1
    if n < period:
        return calc_fib(n) % m
    else :
        return get_fibonacci_huge(n % period, m)



def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n, m))
