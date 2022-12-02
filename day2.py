#goal: read in data frame. go through line-by-line. x=rock (1 pt), y = paper (2 pt), z = scissors (3pt). a = rock, b= paper, c= scissors
#win = 6 pt, draw = 3, lose = 0
#loop through
#if A & X -> 4
#if A & Y -> 8
#if A & Z -> 3
#if B & X -> 1
#if B & Y -> 5
#if B & Z -> 9
#if C & X -> 7
#if C & Y -> 2
#if C & Z -> 6

import pandas as pd
import numpy as np

df = pd.read_fwf('day2_input.txt', header = None)
score = np.empty(len(df), dtype = object)
for index,row in df.iterrows():
    enemy = row[0]
    mine = row[1]
    if ((enemy == 'A') and (mine == 'X')):
        score[index] = 4
    elif ((enemy == 'A') and (mine == 'Y')):
        score[index] = 8
    elif ((enemy == 'A') and (mine == 'Z')):
        score[index] = 3
    elif ((enemy == 'B') and (mine == 'X')):
        score[index] = 1
    elif ((enemy == 'B') and (mine == 'Y')):
        score[index] = 5
    elif ((enemy == 'B') and (mine == 'Z')):
        score[index] = 9
    elif ((enemy == 'C') and (mine == 'X')):
        score[index] = 7
    elif ((enemy == 'C') and (mine == 'Y')):
        score[index] = 2
    elif ((enemy == 'C') and (mine == 'Z')):
        score[index] = 6

print(sum(score))










