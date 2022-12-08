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
vistrees = 0
count = 0
width =len(treespace[0,:])
height= len(treespace[:,0])
for i in range(0, width):
    for j in range(0, height):
        #print(i, ',', j)
        this_tree = treespace[i,j]
        #print("this tree: ", this_tree)
        if(i ==0 or j ==0 or i == width-1 or j == height-1):
            vistrees = vistrees+1
        else:
            top_trees = treespace[0:i, j]
            bot_trees = treespace[i+1:width,j]
            left_trees = treespace[i, 0:j]
            right_trees = treespace[i, j+1:height]
            #print('top: ', top_trees, ' bot: ', bot_trees, ' left: ', left_trees, ' right: ', right_trees)
            #print('top :', sum(top_trees<this_tree)==0, ' bot : ',sum(bot_trees<this_tree)==0, ' left : ', sum(left_trees<this_tree)==0, ' right : ', sum(right_trees<this_tree)==0)
            if(sum(right_trees>=this_tree)==0 or sum(left_trees>=this_tree)==0 or sum(top_trees>=this_tree)==0 or sum(bot_trees>=this_tree)==0):
                vistrees = vistrees+1


print(vistrees)
#print(count)
"""
df = pd.read_fwf('day8_test.txt', header = None)
count =0


treespace = pd.DataFrame()
test = pd.DataFrame()
#pd.concat(treespace,test)
for index,row in df.iterrows():
    #row = str(row[0])
    row = ([int(a) for a in str(row[0])])
    print(row)
    pd.concat([treespace, row])
    #print(row)


print(treespace)

"""