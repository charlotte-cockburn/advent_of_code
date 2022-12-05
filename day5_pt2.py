import pandas as pd
import numpy as np
import re

#

#crates = {
#     1: ["Z", "N"],
#     2: ["M", "C", "D"],
#     3: ["P"]
#}

crates = {
    1: ["B", "L", "D", "T", "W", "C", "F", "M"],
    2: ["N", "B", "L"],
    3: ["J", "C", "H", "T", "L", "V"],
    4: ["S", "P", "J", "W"],
    5: ["Z", "S", "C", "F", "T", "L", "R"],
    6: ["W", "D", "G", "B", "H", "N", "Z"],
    7: ["F", "M", "S", "P", "V", "G", "C", "N"],
    8: ["W", "Q", "R", "J", "F", "V", "C", "Z"],
    9: ["R", "P", "M", "L", "H"]
}


#MOVING SOME ELFISH BOXES
with open('day5_input.txt') as lines:
    for line in lines:
        spling = re.split('\s|\n', line)
        num_to_move = int(spling[1])
        these_crates = crates[int(spling[3])]
        moving_crates = these_crates[-int(spling[1]):]
        remaining_crates = these_crates[0:-int(spling[1])]
        crates[int(spling[3])] = remaining_crates
        crates[int(spling[5])] = crates[int(spling[5])] + list(moving_crates)


#Get last item
top_boxes = []
for key in crates:
    this_stack = crates[key]
    top = this_stack[-1]
    top_boxes.append(top)

print(''.join(top_boxes))


