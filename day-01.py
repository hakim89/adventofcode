
# coding: utf-8


import math

inp = "R4, R5, L5, L5, L3, R2, R3, R2, L1, R5, R1, L5, R2, L2, L4, R3, L1, R4, L5, R4, R3, L5, L3, R4, R2, L5, L5, R2, R3, R5, R4, R2, R1, L1, L5, L2, L3, L4, L5, L4, L5, L1, R3, R4, R5, R3, L5, L4, L3, L1, L4, R2, R5, R5, R4, L2, L4, R3, R1, L2, R5, L5, R1, R1, L1, L5, L5, L2, L1, R5, R2, L4, L1, R4, R3, L3, R1, R5, L1, L4, R2, L3, R5, R3, R1, L3".split(",")

getDigits = lambda x: int("".join([s for s in list(x) if s.isdigit()]))

p, angle, blocks = [0,0], 0, 0

for v in inp:
    angle += 90 if 'R' in v else -90
    p[0] +=  round(math.sin(math.radians(angle % 360))) * getDigits(v)
    p[1] +=  round(math.cos(math.radians(angle % 360))) * getDigits(v)

print "You are {} blocks away ".format(int(abs(0-p[0]) + abs(0-p[1])))

