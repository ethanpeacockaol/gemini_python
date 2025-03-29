move_character = '!'
blank_state = '*'

import os

rows, columns = os.popen('stty size', 'r').read().split()
rows = int(rows)
cols = int(columns)


print(rows)
print(cols)