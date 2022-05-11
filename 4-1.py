codes = [x.strip() for x in open('4-1.in').readlines()]

alpha = list('abcdefghijklmnopqrstuvwxyz')
alpha.reverse()

sector_sum = 0
for c in codes:
    code, checksum = c.split('[')
    
    checksum = checksum[0:-1]
    fragments = code.split('-')
    sector = int(fragments[-1])
    fragments = fragments[0:-1]

    counts = {}
    for l in alpha:
        counts[l] = 0

    for f in fragments:
        for l in list(f):
            counts[l] = counts[l] + 1

    check = sorted(counts, key=counts.get)
    check.reverse()

    if checksum == ''.join(check[0:5]):
        sector_sum = sector_sum + sector

print(sector_sum)
