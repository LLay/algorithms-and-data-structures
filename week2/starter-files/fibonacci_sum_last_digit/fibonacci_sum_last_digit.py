# Uses python3
import sys
dic = {}

def calc_fib(n):
    if (n <= 1):
        return n

    if not n in dic:
        dic[n] = calc_fib(n - 1) + calc_fib(n - 2)
    return dic[n]

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10

def fibonacci_sum(n):
    if n <= 1:
        return n
        
    sum = 1
    for i in range(n-1):
        sum = (sum + calc_fib(i)) % 10
    return sum

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum(n))
