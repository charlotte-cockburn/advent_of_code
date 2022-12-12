input = 'day9_input.txt'

def dot_mover(headpos, tailpos):
    diff1 = headpos[0] - tailpos[0]
    diff2 = headpos[1] - tailpos[1]
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
    elif (diff1 ==-2 and diff2 == 2):
        tailpos[0] -=1
        tailpos[1] +=1
    elif (diff1 ==2 and diff2 == 2):
        tailpos[0] +=1
        tailpos[1] +=1
    elif (diff1 ==2 and diff2 == -2):
        tailpos[0] +=1
        tailpos[1] -=1
    elif (diff1 ==-2 and diff2 == -2):
        tailpos[0] -=1
        tailpos[1] -=1
    return tailpos

snakepos = [[0,0], [0,0], [0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
tailposvec = [[0,0]]
with open(input) as lines:
    for l in lines:
        (dir, move) = l.strip().split(' ')
        move = int(move)
        for i in range(0, move):
            if dir == 'R':
                snakepos[0][0] += 1
            elif dir == 'L':
                snakepos[0][0] -= 1
            elif dir == 'U':
                snakepos[0][1] += 1
            elif dir == 'D':
                snakepos[0][1] -= 1
            for j in range(1, len(snakepos)):
                snakepos[j] = dot_mover(snakepos[j-1], snakepos[j])
            tailposvec.append([snakepos[9][0], snakepos[9][1]])

res = list(set(tuple((sub)) for sub in tailposvec))
print((len(res)))
