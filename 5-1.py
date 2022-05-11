import hashlib

inp = 'wtnhxymk'
inc = 0
password = ''
while True:
    door = inp + str(inc)
    h = hashlib.md5(bytes(door, 'utf-8'))
    check = h.hexdigest()
    if check[0:5] == '00000':
        password = password + check[5]
        print(password)
        if len(password) == 8:
            print(password)
            exit()
    inc = inc + 1
