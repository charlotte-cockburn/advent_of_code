import numpy as np

elfsum = []
count = 0
with open('day1_input.txt') as f:
    for line in f:
        data = [int(e) for e in line.split()]
        if len(data) == 0:
            count = count +1
        else:
            if(len(elfsum)==count+1):
                elfsum[count] = elfsum[count] + data[0]
            else:
                elfsum.append(data[0])

print(np.max(elfsum))
elfsum = np.array(elfsum)
sorted_indices = np.argsort(elfsum)
sorted_array = elfsum[sorted_indices]
print(sum(sorted_array[-3 : ]))





#input_file.read()

#test = input_file.split("\n\n")

