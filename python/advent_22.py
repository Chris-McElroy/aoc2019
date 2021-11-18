import numpy as np

instructions = list()
with open('in_22') as f:
    instructions = f.readlines()

def apply(deck, instr):
    s = instr.split()
    if 'stack' in s:
        deck = np.flip(deck)
    elif 'cut' in s:
        idx = int(s[-1])
        deck = np.concatenate([deck[idx:], deck[:idx]])
    else:
        inc = int(s[-1])
        idxs = np.argsort((np.arange(len(deck))*inc)%len(deck))
        deck = deck[idxs]
    return deck

def apply_card(card, count, instr):
    s = instr.split()
    if 'stack' in s:
        card = count - card-1
    elif 'cut' in s:
        idx = int(s[-1])
        if idx < 0: idx = count + idx
        if card < idx:
            card = card + count - idx
        else:
            card = card - idx
    else:
        inc = int(s[-1])
        card = (card*inc)%count
    return card

'''
count = 10007
card = 2019
for instr in instructions:
    card = apply_card(card, count, instr)

print(card)
'''
#print(apply_card(3,10,'deal into new stack'))

def apply_all_instr(card, count, instructions):
    for instr in instructions:
        card = apply_card(card, count, instr)
    return card

def apply_instr_general(app, count, instr):
    coef, const = app
    s = instr.split()
    if 'stack' in s:
        coef = -coef
        const = -(const+1)
    elif 'cut' in s:
        idx = int(s[-1])
        const -= idx
    else:
        inc = int(s[-1])
        coef *= inc
        const *= inc
    return coef%count,const%count

def apply_all_general(count, instructions):
    app = (1,0)
    for instr in instructions:
        app = apply_instr_general(app, count, instr)
    return app

def apply_to_app(app1, app2, count):
    coef1, const1 = app1
    coef2, const2 = app2
    coef = (coef1*coef2)%count
    const = (const1 + coef1*const2)%count
    return coef, const

def multi_app(app, reps, count):
    if reps == 0:
        return (1,0)
    if reps%2 == 1:
        return apply_to_app(multi_app(app, reps-1,count),app,count)
    compound = multi_app(app,reps//2, count)
    return apply_to_app(compound,compound,count)

def euler(a,m,coefs = (1,0,0,1)):
    if m == 0:
        return (a,coefs[:2])
    q = a//m
    r = a%m
    s0,t0,s1,t1 = coefs
    s2 = s0 - q*s1
    t2 = t0 - q*t1
    return euler(m,r,(s1,t1,s2,t2))

count = 119315717514047
reps = 101741582076661
inv_reps = count - reps

card = 2020

app = (apply_all_general(count, instructions))
coef, const = multi_app(app, reps, count)
inv_coef = euler(coef, count)[1][0]
start = (inv_coef*(2020-const))%count
print(start)

'''
length = 0
while True:
    if length%10000 == 0:
        print(length)
    if length > 0 and card == init_card:
        break
    card = apply_all_instr(card, count, instructions)
    length += 1

print(f'cycle detected length {length}')

actual_reps = reps%length
for _ in range(actual_reps):
    card = apply_all_instr(card, count, instructions)
print(card)
'''