
# coding: utf-8
import itertools
import operator
import re
from collections import defaultdict


lines = [line.rstrip('\n') for line in open('day04.txt')]


def countList(l):
    d = defaultdict(int)
    for s in l:
        d[s] += 1
    
    d = sorted(d.items())
    return [k for (k, v) in sorted(d, key=operator.itemgetter(1), reverse = True)]

def getRoomPeices(roomString):
    m = re.search("\d", roomString)
    if m:
        ss = roomString[0:m.start()].replace("-", "")
        sectorId = "".join([s for s in roomString if s.isdigit()])
        checksum = roomString[roomString.index('[')+1:roomString.index(']')]
        return ss, int(sectorId), checksum
    
sectorIdSum = 0
for room in lines:
    ss, sectorId, che = getRoomPeices(room)
    c = "".join(countList(ss)[0:5])
    if c == che:
        sectorIdSum += sectorId

print "Sum of Sector IDs for valid rooms {}".format(sectorIdSum)