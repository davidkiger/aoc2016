dirs = [x.strip() for x in open('1-1.in').readlines()[0].split(',')]

pos = {'x': 0, 'y': 0}
nesw = [(0,-1), (1,0), (0,1), (-1,0)]
index = 0

for d in dirs:
    if d[0] == 'L': index = (index - 1) % 4
    elif d[0] == 'R': index = (index + 1) % 4
    
    val = int(d[1:])

    pos['x'] = pos['x'] + (val * nesw[index][0])
    pos['y'] = pos['y'] + (val * nesw[index][1])

print(sum([abs(pos['x']), abs(pos['y'])]))
