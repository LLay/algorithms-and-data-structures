# Uses python3
import sys

def optimal_summands(n):
    summands = []
    for i in range(1, n):
        if n <= 2*i:
            summands.append(n)
            break
        summands.append(i)
        n -= i

    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
