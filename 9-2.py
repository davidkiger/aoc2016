c = [x.strip() for x in open('9-1.in').readlines()][0]

def decompress(compressed):
    next_check = 0
    total = 0
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
            
            total = total + decompress(compressed[i:i+length])*times
            next_check = i+length
        else:
            total = total + 1

    return total

total = decompress(c)

print(total)
