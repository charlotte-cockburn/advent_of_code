import pandas as pd
import numpy as np
import re
input = 'day8_input.txt'
#Get data into a "matrix" of sorts- I wish I were using Matlab right about now
treespace = []
with open(input) as f:
    for line in f:
        treespace.append([int(x) for x in str(line).strip()])
#print(np.array(treespace))
treespace = np.array(treespace)
#Loop through "matrix"
width =len(treespace[0,:])
height= len(treespace[:,0])
winning_score = 0
for i in range(0, width):
    for j in range(0, height):
        #print(i, ',', j)
        this_tree = treespace[i,j]
        #print("this tree: ", this_tree)
        top_score = 0
        bot_score = 0
        right_score = 0
        left_score = 0
        top_trees = treespace[0:i, j]
        bot_trees = treespace[i+1:width,j]
        left_trees = treespace[i, 0:j]
        right_trees = treespace[i, j+1:height]
        for k in reversed(top_trees):
            top_score += 1
            if(k>=this_tree): break
        for k in (bot_trees):
            bot_score += 1
            if(k >=this_tree): break
        for k in reversed(left_trees):
            left_score += 1
            if(k >=this_tree): break
        for k in right_trees:
            right_score += 1
            if(k >=this_tree): break
        if top_score * bot_score * right_score * left_score > winning_score: winning_score = top_score*bot_score*right_score*left_score


print(winning_score)
