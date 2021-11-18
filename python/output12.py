import math

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# mp = [[-1,0,2],[2,-10,-7],[4,-8,8],[3,5,-1]] # 1
# op = [[-1,0,2],[2,-10,-7],[4,-8,8],[3,5,-1]] # 1
# <x=-1, y=0, z=2>
# <x=2, y=-10, z=-7>
# <x=4, y=-8, z=8>
# <x=3, y=5, z=-1>

# mp = [[-8,-10,0],[5,5,10],[2,-7,3],[9,-8,-3]] # 2
# op = [[-8,-10,0],[5,5,10],[2,-7,3],[9,-8,-3]] # 2
mv = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

# <x=-8, y=-10, z=0>
# <x=5, y=5, z=10>
# <x=2, y=-7, z=3>
# <x=9, y=-8, z=-3>

mp = [[17,5,1],[-2,-8,8],[7,-6,14],[1,-10,4]] # mine
op = [[17,5,1],[-2,-8,8],[7,-6,14],[1,-10,4]] # mine
# <x=17, y=5, z=1>
# <x=-2, y=-8, z=8>
# <x=7, y=-6, z=14>
# <x=1, y=-10, z=4>

tot = 1000000
cr = [0, 0, 0]
for step in range(tot):
    for m1 in range(4):
        for m2 in range(4):
            if m1 != m2:
                for i in range(3):
                    if mp[m1][i] > mp[m2][i]:
                        mv[m1][i] -= 1
                    elif mp[m1][i] < mp[m2][i]:
                        mv[m1][i] += 1
    check = [True, True, True]
    for m1 in range(4):
        for i in range(3):
            mp[m1][i] += mv[m1][i]
            if mv[m1][i] != 0 or mp[m1][i] != op[m1][i]:
                check[i] = False
    for i in range(3):
        if check[i] and cr[i] == 0:
            print i, step
            cr[i] = step+1
            print mv
            print mp
    if step == 2772:
        print "stoinf"
        print mv
        print mp

st = cr[2]*cr[1]/gcd(cr[2],cr[1])

print st*cr[0]/gcd(st,cr[0])
print tot    
print mp
print mv
# 
# mpE = [0,0,0,0]
# mvE = [0,0,0,0]
# kE = [0,0,0,0]
# for m1 in range(4):
#     for i in range(3):
#         mpE[m1] += abs(mp[m1][i])
#         mvE[m1] += abs(mv[m1][i])
#     kE[m1] = mpE[m1]*mvE[m1]
# 
# print mpE
# print mvE
# print kE
# print sum(kE)
# 