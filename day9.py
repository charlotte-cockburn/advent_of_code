input = 'day9_input.txt'
headpos = [0,0]
tailpos = [0,0]
tailposvec = [[0,0]]
with open(input) as lines:
    for l in lines:
        (dir, move) = l.strip().split(' ')
        print(dir, move)
        move = int(move)
        for i in range(0, move):
            if dir == 'R':
                headpos[0] += 1
            elif dir == 'L':
                headpos[0] -= 1
            elif dir == 'U':
                headpos[1] += 1
            elif dir == 'D':
                headpos[1] -= 1

            diff1 = headpos[0] - tailpos[0]
            diff2 = headpos[1] - tailpos[1]

            if abs(diff1) <= 1 and abs(diff2) <= 1:
                continue
            else:
                if (diff1 == -1 and diff2 == 2):
                    tailpos[0] -= 1
                    tailpos[1] += 1
                elif (diff1 == 0 and diff2 == 2):
                    tailpos[1] += 1
                elif (diff1 == 1 and diff2 == 2):
                    tailpos[0] += 1
                    tailpos[1] += 1
                elif (diff1 == 2 and diff2 == 1):
                    tailpos[0] += 1
                    tailpos[1] += 1
                elif (diff1 == 2 and diff2 == 0):
                    tailpos[0] += 1
                elif (diff1 == 2 and diff2 == -1):
                    tailpos[0] += 1
                    tailpos[1] -= 1
                elif (diff1 == 1 and diff2 == -2):
                    tailpos[0] += 1
                    tailpos[1] -= 1
                elif (diff1 == 0 and diff2 == -2):
                    tailpos[1] -= 1
                elif (diff1 == -1 and diff2 == -2):
                    tailpos[0] -= 1
                    tailpos[1] -= 1
                elif (diff1 == -2 and diff2 == -1):
                    tailpos[0] -= 1
                    tailpos[1] -= 1
                elif (diff1 == -2 and diff2 == 0):
                    tailpos[0] -= 1
                elif (diff1 == -2 and diff2 == 1):
                    tailpos[0] -= 1
                    tailpos[1] += 1
                tailposvec.append([tailpos[0], tailpos[1]])
res = list(set(tuple((sub)) for sub in tailposvec))
print((len(res)))
