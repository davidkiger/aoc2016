codes = [x.strip() for x in open('6-1.in').readlines()]

alpha = list('abcdefghijklmnopqrstuvwxyz')
cols = []
for x in range(8):
    counts = {}
    for l in alpha:
        counts[l] = 0
    cols.append(counts)

for c in codes:
    chars = list(c)
    for i in range(len(chars)):
        l = chars[i]
        cols[i][l] = cols[i][l] + 1

msg = ''
for x in range(8):
    check = sorted(cols[x], key=cols[x].get)
    check.reverse()
    msg = msg + check[0]

print(msg)
