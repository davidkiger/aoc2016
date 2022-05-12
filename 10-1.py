insts = [x.strip() for x in open('10-1.in').readlines()]

bots = {}
outputs = {}
for inst in insts:
    tokens = inst.split(' ')
    if tokens[0] == 'value':
        try:
            bots[tokens[-1]].append(int(tokens[1]))
            bots[tokens[-1]].sort()
        except:
            bots[tokens[-1]] = [int(tokens[1])]

found = False
while not found:
    for inst in insts:
        tokens = inst.split(' ')
        if tokens[0] == 'bot':
            giver = tokens[1]
            if giver in bots.keys() and len(bots[giver]) == 2:
                chips = bots[giver]
                bots[giver] = []

                # low
                dest = tokens[5]
                num = tokens[6]
                if dest == 'output':
                    try:
                        outputs[num].append(chips[0])
                    except:
                        outputs[num] = [chips[0]]
                elif dest == 'bot':
                    try:
                        bots[num].append(chips[0])
                        bots[num].sort()
                        if bots[num][0] == 17 and bots[num][1] == 61:
                            print(num)
                            found = True
                    except:
                        bots[num] = [chips[0]]

                # high
                dest = tokens[-2]
                num = tokens[-1]
                if dest == 'output':
                    try:
                        outputs[num].append(chips[1])
                    except:
                        outputs[num] = [chips[1]]
                elif dest == 'bot':
                    try:
                        bots[num].append(chips[1])
                        bots[num].sort()
                        if bots[num][0] == 17 and bots[num][1] == 61:
                            print(num)
                            found = True
                    except:
                            bots[num] = [chips[1]]
