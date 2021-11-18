import string

def nestedIn(a, this):
    for subList in this:
        if type(subList) is list:
            if nestedIn(a, subList):
                return True
        else:
            if subList == a:
                return True
    return False
    
def addTo(a, b, orbits):
    if orbits[0] == a:
        orbits += [b]
        return True
    for subOrbit in orbits:
        if type(subOrbit) is list:
            if addTo(a, b, subOrbit):
                return True
    return False
    
def getScore(objects, depth):
    score = 0
    for obj in objects:
        if type(obj) is list:
            score += getScore(obj,depth+1)
        else:
            score += depth
    return score

f = open('input6', 'r')
x = f.readlines()
objects = []
scores = {}
o = 0
score = 0
for objs in x:
    obj1 = ""
    i = 0
    c = objs[i]
    while c != ")":
        obj1 += c
        i += 1
        c = objs[i]
    i += 1 # skip )
    c = objs[i]
    obj2 = ""
    while c != "\n" and i < len(objs):
        obj2 += c
        i += 1
        if i < len(objs):
            c = objs[i]
    
    if not nestedIn(obj1, objects):
        objects += [[obj1]]
    
    added = False
    for poss in objects:
        if obj2 == poss[0]:
            objects.remove(poss)
            addTo(obj1, poss, objects)
            added = True
            break
            
    if not added and nestedIn(obj2, objects):
        print "wat"
    
    if not added:
        addTo(obj1, [obj2], objects)
    
# print getScore(objects[0],0)

sharedOrbit = objects
minimized = False
while not minimized:
    for poss in sharedOrbit:
        if type(poss) is list:
            if nestedIn('YOU', poss):
                if nestedIn('SAN', poss):
                    sharedOrbit = poss
                    break
                else:
                    minimized = True
                    break
        elif poss == 'YOU':
            minimized = True
            break

sanOrbit = sharedOrbit
sanDist = 0 if (sanOrbit[0] == 'SAN') else -1
while sanOrbit[0] != 'SAN':
    sanDist += 1
    for poss in sanOrbit:
        if type(poss) is list:
            if nestedIn('SAN', poss):
                sanOrbit = poss
                break

youOrbit = sharedOrbit
youDist = 0 if (youOrbit[0] == 'YOU') else -1
while youOrbit[0] != 'YOU':
    youDist += 1
    for poss in youOrbit:
        if type(poss) is list:
            if nestedIn('YOU', poss):
                youOrbit = poss
                break


print youDist + sanDist
# print x
# print score
# print scores
print objects