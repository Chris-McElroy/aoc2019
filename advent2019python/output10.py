import string
import math

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def getXY(a,b):
    div = abs(gcd(a,b))
    if div != 0:
        a /= div
        b /= div
    return (a,b)
f = open('input10', 'r')
asts = f.readlines()
for i in range(len(asts)):
    asts[i] = asts[i][:-1]

rowL = len(asts[0])
colL = len(asts)

bestNum = 0
bestCoords = [0,0]
bestDict = {}

for c1 in range(colL):
    for r1 in range(rowL):
        if asts[c1][r1] == '#':
            sightDict = {}
            currentNum = 0
            for c2 in range(colL):
                for r2 in range(rowL):
                    if [c2, r2] != [c1, r1]:
                        if asts[c2][r2] == '#':
                            (x,y) = getXY(c1-c2,r1-r2)
                            if (x,y) not in sightDict:
                                sightDict[(x,y)] = 1
                                currentNum += 1
            if currentNum > bestNum:
                bestNum = currentNum
                bestCoords = [c1,r1]
                bestDict = sightDict

print bestNum
print bestCoords

# 102 hit, first hit is 103
preHits = 0
hits = 102
scores = [0,100]
coords = [(0,0),(0,0)]
for entry in bestDict:
    if entry[0] >= 0 and entry[1] > 0:
        score = entry[0]*1.0/entry[1]
        place = 0
        while score > scores[place]:
            place += 1
        scores = scores[:place] + [score] + scores[place:]
        coords = coords[:place] + [entry] + coords[place:]
    else:
        preHits += 1

print (-(coords[199-preHits][0] - bestCoords[0]),-(coords[199-preHits][1] - bestCoords[1]))
print (-(coords[200-preHits][0] - bestCoords[0]),-(coords[200-preHits][1] - bestCoords[1]))
print (-(coords[201-preHits][0] - bestCoords[0]),-(coords[201-preHits][1] - bestCoords[1]))
print scores
print coords





