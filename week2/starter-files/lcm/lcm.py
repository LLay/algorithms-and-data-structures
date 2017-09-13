# Uses python3
import sys

def lcm_naive(a, b):
    multiple = b
    while multiple % a != 0:
        multiple += b
    return multiple

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))
