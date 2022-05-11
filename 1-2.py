dirs = [x.strip() for x in open('1-1.in').readlines()[0].split(',')]

pos = [0,0]
nesw = [(0,-1), (1,0), (0,1), (-1,0)]
index = 0

visited = set()

for d in dirs:
    if d[0] == 'L': index = (index - 1) % 4
    elif d[0] == 'R': index = (index + 1) % 4
    
    val = int(d[1:])
    if nesw[index][0] == 0:
        for i in range(1, val+1):
            this_pos = (pos[0], pos[1]+(i*nesw[index][1]))
            if (this_pos not in visited):
                visited.add(this_pos)
            else:
                print(sum([abs(this_pos[0]), abs(this_pos[1])]))
                exit()
            
    elif nesw[index][1] == 0:
        for i in range(1, val+1):
            this_pos = (pos[0]+(i*nesw[index][0]), pos[1])
            if (this_pos not in visited):
                visited.add(this_pos)
            else:
                print(sum([abs(this_pos[0]), abs(this_pos[1])]))
                exit()

    pos = list(this_pos)
