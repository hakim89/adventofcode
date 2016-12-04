
# coding: utf-8

# In[1]:

lines = [line.strip() for line in open('day3.txt')]


# In[2]:

def is_not_triangle(a, b, c):
    return (a >= (b+c)) or (b >= (a+c)) or (c >= (a+b))


# In[4]:

impossibles = 0
triangles = [[int(s) for s in l.split(' ') if s] for l in lines]
for tri in triangles:
    impossibles += 1 if is_not_triangle(tri[0], tri[1], tri[2]) else 0

print "Your list had {} valid triangles and {} impossible triabgles".format(len(triangles)-impossibles, impossibles)


# In[ ]:



