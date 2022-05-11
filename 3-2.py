import re

rex = re.compile(r'\W+')
triangles = [rex.sub(' ', x).strip() for x in open('3-1.in').readlines()]

corrected = []
for i in range(0, len(triangles), 3):
    sides_a = [int(x.strip()) for x in triangles[i].split(' ')]
    sides_b = [int(x.strip()) for x in triangles[i+1].split(' ')]
    sides_c = [int(x.strip()) for x in triangles[i+2].split(' ')]

    corrected.append( [sides_a[0], sides_b[0], sides_c[0]] )
    corrected.append( [sides_a[1], sides_b[1], sides_c[1]] )
    corrected.append( [sides_a[2], sides_b[2], sides_c[2]] )

possible = 0
for sides in corrected:
    if (sides[0] + sides[1] > sides[2]) and (sides[1] + sides[2] > sides[0]) and (sides[2] + sides[0] > sides[1]):
        possible = possible + 1

print(possible)
