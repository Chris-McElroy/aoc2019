import string

def getBest(offs,reqs,costs):
    bestCost = -1
    bestIng = []
    for ing in reqs:
        a = 0
        for ing2 in offs:
            if ing[1] == ing2[1]:
                a = ing2[0]
        b = 0
        for ing3 in costs:
            if ing[1] == ing3[1]:
                b = ing3[0]
        cost = a*b
        if cost != 0:
            if bestCost == -1 or cost < bestCost:
                bestCost = cost
                bestIng = ing
    print bestCost, bestIng
    return bestIng

f = open('input14', 'r')
x = f.readlines()
reactions = []
for line in x:
    reactions += [[]]
    ing = line.split(', ')
    for i in range(len(ing)):
        if i < len(ing)-1:
            reactions[-1] += [[int(ing[i].split(' ')[0]),ing[i].split(' ')[1]]]
        else:
            reactions[-1] += [[int(ing[i].split(' ')[0]),ing[i].split(' ')[1]]]
            reactions[-1] += [[int(ing[i].split(' ')[-2]),ing[i].split(' ')[-1][:-1]]]

costs = [[1, 'ORE']]
changes = 1
while changes > 0 and changes < 1000:
    changes = 0
    for r in reactions:
        known = True
        for ing in r[:-1]:
            inCosts = False
            for c in costs:
                if c[1] == ing[1]:
                    inCosts = True
            if not inCosts:
                known = False
        
        new = True
        for ing in costs:
            if r[-1][1] == ing[1]:
                new = False
        if known and new:
            costs += [[0,r[-1][1]]]
            for ing in r[:-1]:
                for c in costs:
                    if c[1] == ing[1]:
                        costs[-1][0] += c[0]*ing[0]*1.0/r[-1][0]
                        changes += 1

print "costs", costs

reqs = [[1, 'FUEL']]
extra = []
repeats = 0
while (len(reqs) > 1 or reqs[-1][-1] != 'ORE') and repeats < 800:
    changes = 0
    offs = []
    for req in reqs:
        for r in reactions:
            factor = 0
            if r[-1][-1] == req[1]:
                factor += req[0]/r[-1][0]
                if factor*r[-1][0] != req[0]:
                    offs += [[req[0]-factor*r[-1][0], req[1]]]
            if factor != 0:
                changes += 1
                print reqs, " + ", r
                req[0] -= r[-1][0]*factor
                if req[0] <= 0:
                    reqs.remove(req)
                for ing in r[:-1]:
                    new = True
                    for req2 in reqs:
                        if req2[1] == ing[1]:
                            new = False
                            req2[0] += ing[0]*factor
                    if new:
                        reqs += [[ing[0]*factor, ing[1]]]
        
        if req[0] > 0:
            for e in extra:
                if e[1] == req[1]:
                    amount = min(e[0],req[0])
                    changes += 1
                    e[0] -= amount
                    req[0] -= amount
                    if e[0] <= 0:
                        extra.remove(e)
                    if req[0] <= 0:
                        reqs.remove(req)
    if changes == 0:
        print "last roundin", reqs
        print "extra", extra
        req = getBest(offs,reqs,costs)
        for r in reactions:
            factor = 0
            if r[-1][-1] == req[1]:
                factor = req[0]/r[-1][0]+1
            if factor != 0:
                newE = True
                for e in extra:
                    if e[1] == req[1]:
                        e[0] += factor*r[-1][0]-req[0]
                        newE = False
                        break
                if newE:
                    extra += [[factor*r[-1][0]-req[0],req[1]]]
                reqs.remove(req)
                for ing in r[:-1]:
                    new = True
                    for req2 in reqs:
                        if req2[1] == ing[1]:
                            new = False
                            req2[0] += ing[0]*factor
                    if new:
                        reqs += [[ing[0]*factor, ing[1]]]
    repeats += 1
    # print repeats

waste = 0
for e in extra:
    for c in costs:
        if e[1] == c[1]:
            waste += c[0]*e[0]

print((1000000000000.0-waste)/costs[-1][0])
print "extra", extra
print waste
print reqs
print repeats

        