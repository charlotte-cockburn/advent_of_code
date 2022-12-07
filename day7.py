import re
import numpy as np
import sys

input = 'day7_input.txt'

#initialize dictionary
filedir = {
    'home/' : {'subdir' : [],
              'size': [],
              'filename': [],
              'parentdir': 'home',
              'dirchain': []
              }
}

with open(input) as lines:
    for l in lines:
        #if the command is a cd, rearrange where we are in the structure
        if '$ cd' in l:
            movement = l.replace('$ cd ', '').replace('\n','')
            if(movement == '/'):
                cdir = 'home/'
            elif(movement == '..'):
                backdir = filedir[cdir]['parentdir']
                cdir = backdir
            else:
                #if the current directory is not already a key, add it as a key with empty attributes
                new_dir_chain = filedir[cdir]['dirchain'].copy()
                movement = cdir+movement+'/' #MAKE IT AS A PATH THANK YOU TRISTAN
                if movement not in filedir: filedir[movement] = {'subdir': [], 'size': [], 'filename': [], 'parentdir' : cdir, 'dirchain' : new_dir_chain}
                filedir[movement]['dirchain'].append(cdir)
                cdir = movement
        #if it's a list command, ignore
        if '$ ls' not in l and '$ cd' not in l:
            #if it lists a directory, strip everything except the letter name.
            if 'dir' in l:
                directory = l.replace('dir ', '').replace('\n','')
                if directory not in filedir[cdir]['subdir']: filedir[cdir]['subdir'].append(directory) #add it as a subdirectory under the current dir if not already
            else:
                size = re.findall(r'\d+', l) #strip letters to get size
                filename = " ".join(re.findall("[a-zA-Z]+", l)) #strip numbers to get filename
                filedir[cdir]['size'].append(size) #add size to current directory
                filedir[cdir]['filename'].append(filename) #add filename to current directory

def finding_size(dict, key):
    these_sizes = dict[key]['size']
    size_sum = 0
    for i in range(0, len(these_sizes)):
        size_sum = size_sum + int(these_sizes[i][0])
    # if(len(dict[key]['subdir'])!= 0):
    #     for j in range(0, len(dict[key]['subdir'])):
    #         size_sum = size_sum + finding_size(dict, dict[key]['subdir'][j])

    return size_sum

size_sum =0
each_size = []
for key in filedir:
    size = finding_size(filedir,key)
    for key2 in filedir:
        if key == key2: continue
        dir_chain = filedir[key2]['dirchain']
        if(len(dir_chain)>0):
            for i in range(0, len(dir_chain)):
                if key == dir_chain[i]:
                    size = size + finding_size(filedir, key2)
    each_size.append(size)
    if(size<=100000): size_sum = size_sum + size #part 1

#part 2
print('total size:', max(each_size))
free_space = 70000000-max(each_size)
print('free:', free_space)
space_needed = 30000000 - free_space
print('needed:', space_needed)

prev_diff = max(each_size)
for i in range(0, len(each_size)):
    diff = each_size[i] - space_needed
    if diff < prev_diff and diff >0:
        prev_diff = diff
        winner = each_size[i]

print('size to del:', winner)