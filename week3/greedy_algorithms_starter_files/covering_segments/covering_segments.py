# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    if not segments:
        return []

    #write your code here

    # find the segment ending soonest
    sort = sorted(segments, key=lambda seg: seg.end)

    # mark a point at it's end
    point = sort[0].end

    # add it to our results
    points = [point]

    # remove all segments overlapping this point
    filteredSegments = list(filter(lambda seg: not seg.start <= point or not seg.end >= point, segments))

    points.extend(optimal_points(filteredSegments))
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
