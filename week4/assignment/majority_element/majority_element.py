# Uses python3
import sys
from collections import defaultdict
def get_majority_element(a, left, right):
    dic = defaultdict(lambda: 0, {})
    for i in range(len(a)):
        dic[a[i]] += 1
    for key in dic:
        if dic[key] > len(a)/2:
            return key
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
