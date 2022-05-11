ips = [x.strip() for x in open('7-1.in').readlines()]

ssl_count = 0
for ip in ips:
    in_bracket = False
    aba = []
    bab = []
    for i in range(len(ip)-2):
        if ip[i] == '[':
            in_bracket = True
        elif ip[i] == ']':
            in_bracket = False
        else:
            if ip[i] == ip[i+2] and ip[i] != ip[i+1]:
                if not in_bracket:
                    aba.append(ip[i:i+3])
                else:
                    bab.append(ip[i:i+3])

    for check in aba:
        l = list(check)
        if l[1] + l[0] + l[1] in bab:
            ssl_count = ssl_count + 1
            break

print(ssl_count)
