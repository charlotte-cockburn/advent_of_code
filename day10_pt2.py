#if the current cycle(-1) is contained in x +-1, then it's lit up, otherwise not

input = 'day10_input.txt'

def get_pixel(cycle):
    if(cycle>40):
        cycle = cycle-40
        cycle = get_pixel(cycle)
    return cycle

def add_pixel(cycle, xpos):
    cycle = get_pixel(cycle)
    if(cycle-1 in range(xpos-1,xpos+2)):
        #print(list(range(xpos-1,xpos+2)))
        return('#')
    else:
        return('.')

cycle =0
x =1
crt = []
with open(input) as lines:
    for l in lines:
        this_line = l.strip().split(' ')
        if(len(this_line)==1):
            cycle+=1
            crt.append(add_pixel(cycle,x))
        else:
            cycle+=1
            crt.append(add_pixel(cycle,x))
            cycle+=1
            crt.append(add_pixel(cycle,x))
            x +=int(this_line[1])

crt = ''.join(crt)
indices = [0,40,80,120,160,200,240]
parts = [crt[i:j] for i,j in zip(indices, indices[1:]+[None])]
#print(parts)
for i in parts:
    print(i)
