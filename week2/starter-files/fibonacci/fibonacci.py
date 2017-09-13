# Uses python3
dic = {}

def calc_fib(n):
    if (n <= 1):
        return n

    if not n in dic:
        dic[n] = calc_fib(n - 1) + calc_fib(n - 2)
    return dic[n]

n = int(input())
print(calc_fib(n))
