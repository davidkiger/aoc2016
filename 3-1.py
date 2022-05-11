import re

rex = re.compile(r'\W+')
triangles = [rex.sub(' ', x).strip() for x in open('3-1.in').readlines()]

possible = 0
for t in triangles:
    sides = [int(x.strip()) for x in t.split(' ')]
    if (sides[0] + sides[1] > sides[2]) and (sides[1] + sides[2] > sides[0]) and (sides[2] + sides[0] > sides[1]):
        possible = possible + 1

print(possible)
