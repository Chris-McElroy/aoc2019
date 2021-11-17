import copy
f = open('input20', 'r')
m = f.readlines()
for r in range(len(m)):
    m[r] = list(m[r])


levels = 70
x = []
for l in range(levels):
    x += [copy.deepcopy(m)]
    if l > 0:
        x[l][115][43] = " "

# pos = [77,2]
round = 0
# ignoreString = "# .@\n~"
options = [[0,-1],[0,1],[-1,0],[1,0]]
poss = []
heads = [[77,2,0]]
numSteps = 0
while len(heads) > 0 and round < 8000 and numSteps == 0:
    newHeads = []
    for i in range(len(heads)):
        for o in options:
            h = heads[i]
            if x[h[2]][h[0]+o[0]][h[1]+o[1]] == '.':
                x[h[2]][h[0]+o[0]][h[1]+o[1]] = "&"
                newHeads += [[h[0]+o[0],h[1]+o[1],h[2]]]
            elif x[h[2]][h[0]+o[0]][h[1]+o[1]] >= 'A' and x[h[2]][h[0]+o[0]][h[1]+o[1]] <= 'Z':
                label = ""
                l0spot = []
                if o[0] + o[1] > 0:
                    label += x[h[2]][h[0]+o[0]][h[1]+o[1]]
                    label += x[h[2]][h[0]+2*o[0]][h[1]+2*o[1]]
                    x[h[2]][h[0]+o[0]][h[1]+o[1]] = " "
                    l0spot = [h[0]+o[0],h[1]+o[1]]
                else:
                    label += x[h[2]][h[0]+2*o[0]][h[1]+2*o[1]]
                    label += x[h[2]][h[0]+o[0]][h[1]+o[1]]
                    x[h[2]][h[0]+o[0]][h[1]+o[1]] = " "
                    l0spot = [h[0]+2*o[0],h[1]+2*o[1]]
                if label == "ZZ":
                    numSteps = round
                found = False

                l = h[2]
                if h[0] in range(16,100) and h[1] in range(16,100):
                    l += 1
                    if l == levels:
                        found = True
                else:
                    l -= 1
                    if l < 0:
                        found = True
                for r in range(len(x[0])-1):
                    if found:
                        break
                    for c in range(len(x[0][r])):
                        if found:
                            break
                        if x[l][r][c] == label[0] and [r,c] != l0spot:
                            if r < 33 or r > 85:
                                if x[l][r+1][c] == label[1]:
                                    if r < 20 or r > 50 and r < 100:
                                        x[l][r+2][c] = "&"
                                        newHeads += [[r+2,c,l]]
                                        x[l][r+1][c] = " "
                                    else:
                                        x[l][r-1][c] = "&"
                                        newHeads += [[r-1,c,l]]
                                        x[l][r][c] = " "
                                    found = True
                            else:
                                if x[l][r][c+1] == label[1]:
                                    if c < 16 or c > 50 and c < 100:
                                        x[l][r][c+2] = "&"
                                        newHeads += [[r,c+2,l]]
                                        x[l][r][c+1] = " "
                                    else:
                                        x[l][r][c-1] = "&"
                                        newHeads += [[r,c-1,l]]
                                        x[l][r][c] = " "
                                    found = True

            # if x[h[0]+o[0]][h[1]+o[1]] not in ignoreString and x[h[0]+o[0]][h[1]+o[1]] >= 'a':
            #     poss += [[x[h[0]+o[0]][h[1]+o[1]], round]]
        x[h[2]][h[0]][h[1]] = '~'
    heads = copy.deepcopy(newHeads)
    round += 1

for line in x[0]:
    print "".join(line[:-1])

for line in x[1]:
    print "".join(line[:-1])

#
# for line in x[2]:
#     print "".join(line[:-1])
print heads
print numSteps
print round
