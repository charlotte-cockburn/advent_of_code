#goal: read in data frame. go through line-by-line. x=rock (1 pt), y = paper (2 pt), z = scissors (3pt). a = rock, b= paper, c= scissors
#new goal: X = lose, Y = draw, Z = win
#win = 6 pt, draw = 3, lose = 0
#loop through
#if A & X -> I need to pick scissors and lose -> 3 pts
#if A & Y -> I need to pick rock and draw -> 4 pts
#if A & Z -> I need to pick paper and win -> 8 pts
#if B & X -> I need to pick rock and lose -> 1 pt
#if B & Y -> I need to pick paper and draw -> 5 pts
#if B & Z -> I need to pick scissors and win -> 9 pts
#if C & X -> I need to pick paper and lose -> 2 pts
#if C & Y -> I need to pick scissors and draw -> 6 pts
#if C & Z -> I need to pick rock and win -> 7 pts

import pandas as pd
import numpy as np

df = pd.read_fwf('day2_input.txt', header = None)
score = np.empty(len(df), dtype = object)
for index,row in df.iterrows():
    enemy = row[0]
    mine = row[1]
    if ((enemy == 'A') and (mine == 'X')):
        score[index] = 3
    elif ((enemy == 'A') and (mine == 'Y')):
        score[index] = 4
    elif ((enemy == 'A') and (mine == 'Z')):
        score[index] = 8
    elif ((enemy == 'B') and (mine == 'X')):
        score[index] = 1
    elif ((enemy == 'B') and (mine == 'Y')):
        score[index] = 5
    elif ((enemy == 'B') and (mine == 'Z')):
        score[index] = 9
    elif ((enemy == 'C') and (mine == 'X')):
        score[index] = 2
    elif ((enemy == 'C') and (mine == 'Y')):
        score[index] = 6
    elif ((enemy == 'C') and (mine == 'Z')):
        score[index] = 7

print(sum(score))










