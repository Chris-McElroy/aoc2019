min = 231832
max = 767346
tot = 0

for n in range(min,max+1):
    n1 = n/100000
    n2 = n/10000 - n/100000*10
    n3 = n/1000 - n/10000*10
    n4 = n/100 - n/1000*10
    n5 = n/10 - n/100*10
    n6 = n- n/10*10
    
    if n6 >= n5:
        if n5 >= n4:
            if n4 >= n3:
                if n3 >= n2:
                    if n2 >= n1:
                        doubles = [0,0,0,0,0,0,0,0,0,0]
                        if n6 == n5:
                            doubles[n6] += 1
                        if n5 == n4:
                            doubles[n5] += 1
                        if n4 == n3:
                            doubles[n4] += 1
                        if n3 == n2:
                            doubles[n3] += 1
                        if n2 == n1:
                            doubles[n2] += 1
                        works = False
                        for d in doubles:
                            if d == 1:
                                works = True
                        if works:
                            tot += 1
    
print tot