import pandas as pd
import numpy as np

alphabet_string = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

df = pd.read_fwf('day3_input.txt', header = None)
score = []
for index,row in df.iterrows():
    this_bag = row[0]
    print(len(row[0]))

    comp1 = this_bag[0:(int(len(this_bag)/2))]
    comp2 = this_bag[int((len(this_bag)/2)):int((len(this_bag)))]
    overlap = ''.join(set(comp1).intersection(comp2)) #thanks stackexchange

    print(overlap)
    score.append(alphabet_string.rfind(overlap) +1)

print(sum(score))