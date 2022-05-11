buttons = [x.strip() for x in open('2-1.in').readlines()]

grid = [['X','X','1','X','X'],
        ['X','2','3','4','X'],
        ['5','6','7','8','9'],
        ['X','A','B','C','X'],
        ['X','X','D','X','X']]

code = ''
spot = [1,1]
for b in buttons:
    dirs = list(b)
    for d in dirs:
        if d == 'U' and spot[0] > 0 and grid[spot[0]-1][spot[1]] != 'X':   spot[0] = spot[0]-1
        elif d == 'D' and spot[0] < 4 and grid[spot[0]+1][spot[1]] != 'X': spot[0] = spot[0]+1
        elif d == 'L' and spot[1] > 0 and grid[spot[0]][spot[1]-1] != 'X': spot[1] = spot[1]-1
        elif d == 'R' and spot[1] < 4 and grid[spot[0]][spot[1]+1] != 'X': spot[1] = spot[1]+1
    code += grid[spot[0]][spot[1]]

print(code)
