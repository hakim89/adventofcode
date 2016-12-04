
# coding: utf-8

# In[77]:

def move(direction, position):
    return {
        'R': 1 if position not in  (3, 6, 9) else 0,
        'U': -3 if position not in  (1, 2, 3) else 0,
        'L': -1 if position not in  (1, 4, 7) else 0,
        'D': 3 if position not in  (7, 8, 9) else 0,
    }[direction]


# In[78]:

lines = [line.rstrip('\n') for line in open('input-day02.txt')]


# In[79]:

def getPositionFromLine(start, line):
    for s in line:
        start += move(s, start)
    return start


# In[80]:

p = 5
code = ''
for line in lines:
    p = getPositionFromLine(p, line)
    code += str(p)
    
print "Your bathroom access code is {}".format(code)

