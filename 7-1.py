ips = [x.strip() for x in open('7-1.in').readlines()]

tls_count = 0
for ip in ips:
    in_bracket = False
    found = False
    for i in range(len(ip)-4):
        if ip[i] == '[':
            in_bracket = True
        elif ip[i] == ']':
            in_bracket = False
        else:
            if ip[i] == ip[i+3] and ip[i+1] == ip[i+2]:
                if not in_bracket:
                    found = True
                else:
                    found = False
                    break
    if found:
        tls_count = tls_count + 1

print(tls_count)
