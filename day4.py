import pandas as pd
import numpy as np
import re

df = pd.read_fwf('day4_input.txt', header = None)
count =0
for index,row in df.iterrows():
    split_string = re.split('-|,',row[0])
    if((int(split_string[0])<=int(split_string[2]) and int(split_string[1]) >= int(split_string[3])) or (int(split_string[0])>=int(split_string[2]) and int(split_string[1]) <= int(split_string[3]))):
        print(row[0])
        print(split_string)
        count +=1

print(count)
