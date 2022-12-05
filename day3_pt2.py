import pandas as pd
import numpy as np

alphabet_string = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

df = pd.read_fwf('day3_input.txt', header = None)
score = []
groupsack = []
count = 1
for index,row in df.iterrows():
    this_bag = row[0]
    if count == 1 or count == 2:
        groupsack.append(this_bag)
        count += 1
    elif count == 3:
        groupsack.append(this_bag)
        #find common character, then find score
        overlap = set(groupsack[0]) & set(groupsack[1]) & set(groupsack[2])
        score.append(alphabet_string.rfind(list(overlap)[0]) + 1)
        groupsack = []
        count = 1


print(sum(score))