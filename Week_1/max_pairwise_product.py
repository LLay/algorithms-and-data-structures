# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

largest = max(a)
a.remove(largest)
second = max(a)

print(largest * second)
