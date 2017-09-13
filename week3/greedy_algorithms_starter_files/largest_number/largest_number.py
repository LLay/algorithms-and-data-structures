#Uses python3
import sys

def flatmap(l):
    result = []
    for elem in l:
        if not isinstance(elem, list):
            result.append(elem)
        else:
            result.extend(flatmap(elem))
    return result

def groupByithDigit(l, i):
    if len(l) <= 1:
        return l

    result = [[],[],[],[],[],[],[],[],[],[]]

    # n
    for digit in l:
        result[int(str(digit)[i])].append(digit)


    for index in range(len(result)):
        if len(result[index]) > 1:
            result[index] = groupByithDigit(result[index], i+1)

    result.reverse()
    return result

def largest_number(a):
    return ''.join(str(x) for x in flatmap(groupByithDigit(a,0)))

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
