import pandas as pd
import numpy as np
import re

df = pd.read_fwf('day4_input.txt', header = None)
count =0
for index,row in df.iterrows():
    split_string = re.split('-|,',row[0])
    range1 = list(range(int(split_string[0]), int(split_string[1])+1))
    if(range1== []): range1 = [int(split_string[0])] #cause for some reason it won't do 6:6 range booooooo tomatoes
    range2 = list(range(int(split_string[2]), int(split_string[3])+1))
    if(range2== []): range2 = [int(split_string[2])]
    if(bool(set(range1) & set(range2))):
        count += 1

print(count)
