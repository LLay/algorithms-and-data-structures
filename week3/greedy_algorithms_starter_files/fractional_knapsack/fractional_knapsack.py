# Uses python3
import sys

# n log(n)
def sortByValue(weights, values):
    return list(map(lambda x: x[1],
        sorted(list(enumerate(weights)),
        key=lambda pair: values[pair[0]]/pair[1], reverse=True)))

# n log(n)
def getOriginalIndices(weights, values):
     return [b[0] for b in sorted(
        list(enumerate(weights)),
        key=lambda pair: values[pair[0]]/pair[1], reverse=True)]

def get_optimal_value(capacity, weights, values):
    value = 0
    origIndices = getOriginalIndices(weights, values)
    # n
    for pair in list(enumerate(sortByValue(weights, values))):
        if capacity == 0:
            break

        i = pair[0]
        item = pair[1] # weight
        if item <= capacity:
            # take all
            value += values[origIndices[i]]
            capacity -= item
        else:
            value += values[origIndices[i]] * (capacity/item)
            capacity = 0
            # take as much as will fit


    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]

    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
