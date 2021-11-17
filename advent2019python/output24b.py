import string
import copy

bugString = ".#.##\n..##.\n##...\n#...#\n..###"
emptyBugString = ".....\n.....\n..?..\n.....\n....."

bugs = string.split(bugString,"\n")
for b in bugs:
    print b
print

noBugs = string.split(emptyBugString,"\n")

offs = [[-1,0],[0,-1],[1,0],[0,1]]
time = 100

allBugs = {}
for d in range(-time,time+1):
    allBugs[d] = noBugs
allBugs[0] = bugs

for i in range(-time,time+1):
    print allBugs[i]
print

for m in range(2*time):
    newBugs = {}
    for d in range(-time,time+1):
        newBugs[d] = []
        for r in range(5):
            newBugs[d] += [""]
            for c in range(5):
                if (r,c) == (2,2):
                    newBugs[d][r] += "?"
                else:
                    adj = 0
                    for i in range(4):
                        r2 = r + offs[i][0]
                        c2 = c + offs[i][1]
                        if r2 in range(5) and c2 in range(5):
                            if (r2,c2) == (2,2):
                                if d < time:
                                    for x in range(5):
                                        if i == 0:
                                            if allBugs[d+1][4][x] == "#":
                                                    adj += 1
                                        if i == 1:
                                            if allBugs[d+1][x][4] == "#":
                                                    adj += 1
                                        if i == 2:
                                            if allBugs[d+1][0][x] == "#":
                                                    adj += 1
                                        if i == 3:
                                            if allBugs[d+1][x][0] == "#":
                                                    adj += 1

                            elif allBugs[d][r2][c2] == "#":
                                adj += 1
                        else:
                            if d > -time:
                                if r2 == 5:
                                    r2 = 3
                                    c2 = 2
                                elif r2 == -1:
                                    r2 = 1
                                    c2 = 2
                                elif c2 == 5:
                                    c2 = 3
                                    r2 = 2
                                else:
                                    c2 = 1
                                    r2 = 2
                                if allBugs[d-1][r2][c2] == "#":
                                    adj += 1
                    if (allBugs[d][r][c] == "#" and adj == 1) or (allBugs[d][r][c] == "." and adj in range(1,3)):
                        newBugs[d][r] += "#"
                    else:
                        newBugs[d][r] += "."

    allBugs = copy.deepcopy(newBugs)


for i in range(-time,time+1):
    print allBugs[i]

sum = 0
for i in range(-time,time+1):
    for r in range(5):
        for c in range(5):
            if allBugs[i][r][c] == "#":
                sum += 1
print sum
# print oldBugs
