import math

f = open('d13.in', 'r')


def findFirstBus(start_time, bus):
    delta = [id*math.ceil(start_time/id) - start_time for id in bus]
    index = delta.index(min(delta))
    return bus[index] * delta[index]


start_time = int(f.readline())
bus = [int(id) for id in f.readline().strip().split(',') if id != 'x']
print("Puzzle 1: ", findFirstBus(start_time, bus))
