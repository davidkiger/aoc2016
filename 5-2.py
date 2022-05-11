import hashlib

inp = 'wtnhxymk'
inc = 0
password = list('________')
while True:
    door = inp + str(inc)
    h = hashlib.md5(bytes(door, 'utf-8'))
    check = h.hexdigest()
    if check[0:5] == '00000':
        try:
            if (password[int(check[5])] == '_'):
                password[int(check[5])] = check[6]
                print(''.join(password))
        except:
            pass
        if not password.count('_'):
            exit()
    inc = inc + 1
