
# coding: utf-8

# In[27]:

import itertools
lines = [line.strip() for line in open('day3.txt')]


# In[16]:

def chunks(l, n):
    n = max(1, n)
    return (l[i:i+n] for i in xrange(0, len(l), n))


# In[17]:

def is_not_triangle(a, b, c):
    return (a >= (b+c)) or (b >= (a+c)) or (c >= (a+b))


# In[38]:

impossibles = 0
rows = [[int(s) for s in l.split(' ') if s] for l in lines]

#part1
triangles = rows

#part 2

#columns = itertools.chain(*zip(*rows))
#triangles = list(chunks(list (columns), 3))

for tri in triangles:
    impossibles += 1 if is_not_triangle(tri[0], tri[1], tri[2]) else 0

print "Your list had {} valid triangles and {} impossible triabgles".format(len(triangles)-impossibles, impossibles)



