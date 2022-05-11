buttons = [x.strip() for x in open('2-1.in').readlines()]

grid = [['1','2','3'],
        ['4','5','6'],
        ['7','8','9']]

code = ''
spot = [1,1]
for b in buttons:
    dirs = list(b)
    for d in dirs:
        if d == 'U':   spot[0] = max(spot[0]-1, 0)
        elif d == 'D': spot[0] = min(spot[0]+1, 2)
        elif d == 'L': spot[1] = max(spot[1]-1, 0)
        elif d == 'R': spot[1] = min(spot[1]+1, 2)
    code += grid[spot[0]][spot[1]]

print(code)
