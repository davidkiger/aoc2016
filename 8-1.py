insts = [x.strip() for x in open('8-1.in').readlines()]

screen = [list('..................................................'),
          list('..................................................'),
          list('..................................................'),
          list('..................................................'),
          list('..................................................'),
          list('..................................................')]

for inst in insts:
    tokens = inst.split(' ')
    if tokens[0] == 'rect':
        x,y = [int(x) for x in tokens[1].split('x')]
        for j in range(y):
            for i in range(x):
                screen[j][i] = '#'
    elif tokens[0] == 'rotate':
        if tokens[1] == 'row':
            row = int(tokens[2][2])
            shift = -1*int(tokens[4])
            shifted_row = screen[row][shift:] + screen[row][:shift]
            screen[row] = shifted_row
        if tokens[1] == 'column':
            column = int(tokens[2][2:])
            cache = ''
            for i in range(len(screen)):
                cache = cache + screen[i][column]
            shift = int(tokens[4])
            for i in range(len(screen)):
                screen[i][column] = cache[(i-shift)%len(cache)]

print(screen[0].count('#')+
      screen[1].count('#')+
      screen[2].count('#')+
      screen[3].count('#')+
      screen[4].count('#')+
      screen[5].count('#'))

for r in screen:
    print(''.join(r))
