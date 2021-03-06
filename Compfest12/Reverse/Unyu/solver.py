from itertools import product
import string
import math

ans = [246, 56, 101, 211, 75, 28, 215, 26, 173, 48, 141, 250, 238, 6, 102, 39, 227, 26, 102, 173, 214, 102, 27, 6, 95, 241, 102, 246, 41, 250, 250, 182] 
guess = [ [] for i in range(len(ans)) ]

for i in range(len(ans)):
    for s in string.printable:
        c = int(math.pow(ord(s), 128) % 251)
        if c == ans[i]:
            guess[i].append(s)

# replace manually [] to ['F'] / format flag at index 4
guess[4] = ['F']

for s in product(*guess):
    flag = ''.join(s)
    if flag.startswith("COMPFEST12{tH3_c4T_15_v3rY_"):
        print flag
        # COMPFEST12{tH3_c4T_15_v3rY_Cute}
