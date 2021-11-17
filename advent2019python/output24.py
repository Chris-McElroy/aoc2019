import string
import copy

bugString = ".#.##\n..##.\n##...\n#...#\n..###"

bugs = string.split(bugString,"\n")
for b in bugs:
    print b
print

offs = [[-1,0],[0,-1],[1,0],[0,1]]

oldBugs = []

for m in range(70):
    newBugs = []
    for r in range(5):
        newBugs += [""]
        for c in range(5):
            adj = 0
            for i in range(4):
                r2 = r + offs[i][0]
                c2 = c + offs[i][1]
                if r2 in range(5) and c2 in range(5):
                    if bugs[r2][c2] == "#":
                        adj += 1
            if (bugs[r][c] == "#" and adj == 1) or (bugs[r][c] == "." and adj in range(1,3)):
                newBugs[r] += "#"
            else:
                newBugs[r] += "."

    oldBugs += [copy.deepcopy(bugs)]
    for i in range(5):
        bugs[i] = newBugs[i]
        # print bugs[i]
    # print

    for i in oldBugs:
        matches = True
        for r in range(5):
            if i[r] != bugs[r]:
                matches = False
        if matches:
            print "matches", bugs
            sum = 0
            for r in range(5):
                for c in range(5):
                    if bugs[r][c] == "#":
                        sum += 2**(r*5+c)
            print sum


# print oldBugs
