import string

def caesar(plaintext, shift):
    shift = shift%26
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)

codes = [x.strip() for x in open('4-1.in').readlines()]

alpha = list(string.ascii_lowercase)
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

    room_name = ''
    for f in fragments:
        for l in list(f):
            counts[l] = counts[l] + 1
            room_name = room_name + caesar(l, sector)
        room_name = room_name + ' '

    check = sorted(counts, key=counts.get)
    check.reverse()

    if checksum == ''.join(check[0:5]):
        print(room_name + ' ' + str(sector))
        sector_sum = sector_sum + sector

print(sector_sum)
