input = 'day6_input.txt'
with open(input) as lines:
    for l in lines:
        print(l)
        for i in range(3, len(l)): #change 3 to 13 for part 1
            subset = l[i-3:i+1] #change 3 to 13 for part 1
            if(len(set(subset))==len(subset)):
                sop = i+1
                break
print(sop)



