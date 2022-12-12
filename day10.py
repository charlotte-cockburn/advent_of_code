input = 'day10_input.txt'
cycle =0
x =1
strengths = []
position_vec = range(20, 1000000, 40)
with open(input) as lines:
    for l in lines:
        this_line = l.strip().split(' ')
        if(len(this_line)==1):
            cycle+=1
            if cycle in position_vec:
                print(x)
                print(cycle)
                strengths.append(cycle*x)
        else:
            cycle+=1
            if cycle in position_vec:
                print(x)
                print(cycle)
                strengths.append(cycle*x)
            cycle+=1
            if cycle in position_vec:
                print(x)
                print(cycle)
                strengths.append(cycle*x)
            x +=int(this_line[1])
print(sum(strengths))
