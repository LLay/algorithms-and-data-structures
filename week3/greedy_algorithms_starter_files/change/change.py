# Uses python3
import sys

coins = [10, 5, 1]

def get_change(m):
    count = 0
    for denomination in coins:
        while m >= denomination:
            count += 1
            m -= denomination

    return count

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
