
# coding: utf-8

# In[1]:

keypad = [
    [0, 0, 1, 0, 0],
    [0, 2, 3, 4, 0],
    [5, 6, 7, 8, 9],
    [0, 'A', 'B', 'C', 0],
    [0, 0, 'D', 0, 0],
]

def moveRight(direction, position):
    try:
        row = [row for row in keypad if position in row][0]
        newPos = row[row.index(position)+1]
        return newPos if newPos != 0 else position
    except:
        return position

def moveLeft(direction, position):
    try:
        row = [row for row in keypad if position in row][0]
        i = row.index(position)
        newPos = row[i-1] if i>0 else 0
        return newPos if newPos != 0 else position
    except:
        return position


def moveUp(direction, position):
    try:
        row = [row for row in keypad if position in row][0]
        i = keypad.index(row)
        newPos = keypad[i-1][row.index(position)] if i != 0 else 0
        return newPos if newPos != 0 else position
    except:
        return position
    
def moveDown(direction, position):
    try:
        row = [row for row in keypad if position in row][0]
        newPos = keypad[keypad.index(row)+1][row.index(position)]
        return newPos if newPos != 0 else position
    except:
        return position


def move(direction, position):
    return {
        'R': moveRight(direction, position),
        'U': moveUp(direction, position),
        'L': moveLeft(direction, position),
        'D': moveDown(direction, position),
    }[direction]


# In[2]:

lines = [line.rstrip('\n') for line in open('input-day02.txt')]


# In[3]:

def getPositionFromLine(position, line):
    for s in line:
        position = move(s, position)
    return position


# In[4]:

p = 5
code = ''
for line in lines:
    p = getPositionFromLine(p, line)
    code += str(p)
    
print "Your bathroom access code is {}".format(code)


# In[ ]:



