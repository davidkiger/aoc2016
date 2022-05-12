compressed = [x.strip() for x in open('9-1.in').readlines()][0]

total = 0
next_check = 0
for i in range(len(compressed)):
    if i < next_check:
        continue

    if compressed[i] == '(':
        marker = ''
        i = i+1
        while compressed[i] != ')':
            marker = marker + compressed[i]
            i = i+1
        i = i+1

        length,times = [int(x) for x in marker.split('x')]
        total = total + length*times
        next_check = i+length
    else:
        total = total + 1

print(total)
