import copy
f = open('input18', 'r')
m = f.readlines()
for r in range(len(m)):
    m[r] = list(m[r])

x = copy.deepcopy(m)
pos = [40,40]
changes = 1
round = 0
ignoreString = "#.@\n~"
foundString = ""
options = [[0,-1],[0,1],[-1,0],[1,0]]
poss = []
heads = [[40,40]]
while len(heads) > 0 and round < 6000:
    newHeads = []
    found = False
    for h in heads:
        for o in options:
            p = x[h[0]+o[0]][h[1]+o[1]]
            if p == '.' or p in foundString:
                x[h[0]+o[0]][h[1]+o[1]] = '@'
                newHeads += [[h[0]+o[0],h[1]+o[1]]]
            if p not in ignoreString and p >= 'a':
                x = copy.deepcopy(m)
                x[40][40] = '.'
                door = chr(ord(p)-ord('a')+ord('A'))
                ignoreString += p
                foundString += p
                foundString += door
                x[h[0]+o[0]][h[1]+o[1]] = '@'
                newHeads = [[h[0]+o[0],h[1]+o[1]]]
                found = True
                break
                # poss += [[x[h[0]+o[0]][h[1]+o[1]], round]]
        if found:
            break
        x[h[0]][h[1]] = '~'

    if len(foundString) == 52:
        break
    heads = copy.deepcopy(newHeads)
    round += 1

for line in x:
    print "".join(line[:-1])

print round
print poss
print ignoreString

# bestPoss = []
# bestSteps = 500
# for p in poss:
#     if p[1] < bestSteps:
#         bestPoss = p
#         bestSteps = p[1]
#
#
# x = copy.deepcopy(m)
# x[pos[0]][pos[1]] = '.'
# pos = [bestPoss[2],bestPoss[3]]
# x[pos[0]][pos[1]] = '@'
# changes = 1
# round = 0
# poss = []
# while changes > 0 and round < 500:
#     changes = 0
#     y = copy.deepcopy(x)
#     for r in range(1,len(x)-1):
#         for c in range(1,len(x[0])-2):
#             if x[r][c] == '@':
#                 for o in options:
#                     if x[r+o[0]][c+o[1]] == '.':
#                         y[r+o[0]][c+o[1]] = '@'
#                         changes += 1
#                     if x[r+o[0]][c+o[1]] not in ignoreString and x[r+o[0]][c+o[1]] >= 'a':
#                         poss += [[x[r+o[0]][c+o[1]], round, r, c]]
#                 y[r][c] = '~'
#     x = copy.deepcopy(y)
#     round += 1
# print round
# for line in x:
#     print "".join(line[:-1])
