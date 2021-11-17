deckSize = 10007


def dealWI(deck, inc):
    newDeck = range(deckSize)
    for i in range(deckSize):
        newDeck[i*inc % deckSize] = deck[i]

    return newDeck

def dealNS(deck):
    newDeck = range(deckSize)
    for i in range(deckSize):
        newDeck[deckSize-1-i] = deck[i]

    return newDeck

def cut(deck, N):
    if N < 0:
        N = deckSize + N
    newDeck = range(deckSize)
    for i in range(deckSize):
        newDeck[i] = deck[(i+N) % deckSize]
    return newDeck

myDeck = range(deckSize)

myDeck = dealWI(myDeck, 55)
myDeck = cut(myDeck, -6791)
myDeck = dealWI(myDeck, 9)
myDeck = cut(myDeck, -5412)
myDeck = dealWI(myDeck, 21)
myDeck = dealNS(myDeck)
myDeck = dealWI(myDeck, 72)
myDeck = cut(myDeck, -362)
myDeck = dealWI(myDeck, 24)
myDeck = cut(myDeck, -5369)
myDeck = dealWI(myDeck, 22)
myDeck = cut(myDeck, 731)
myDeck = dealWI(myDeck, 72)
myDeck = cut(myDeck, 412)
myDeck = dealNS(myDeck)
myDeck = dealWI(myDeck, 22)
myDeck = cut(myDeck, -5253)
myDeck = dealWI(myDeck, 73)
myDeck = dealNS(myDeck)
myDeck = cut(myDeck, -6041)
myDeck = dealNS(myDeck)
myDeck = cut(myDeck, 6605)
myDeck = dealWI(myDeck, 6)
myDeck = cut(myDeck, 9897)
myDeck = dealWI(myDeck, 59)
myDeck = cut(myDeck, -9855)
myDeck = dealNS(myDeck)
myDeck = cut(myDeck, -7284)
myDeck = dealWI(myDeck, 7)
myDeck = cut(myDeck, 332)
myDeck = dealWI(myDeck, 37)
myDeck = dealNS(myDeck)
myDeck = dealWI(myDeck, 43)
myDeck = dealNS(myDeck)
myDeck = dealWI(myDeck, 59)
myDeck = cut(myDeck, 1940)
myDeck = dealWI(myDeck, 16)
myDeck = cut(myDeck, 3464)
myDeck = dealWI(myDeck, 24)
myDeck = cut(myDeck, -7766)
myDeck = dealWI(myDeck, 36)
myDeck = cut(myDeck, -156)
myDeck = dealWI(myDeck, 18)
myDeck = cut(myDeck, 8207)
myDeck = dealWI(myDeck, 33)
myDeck = cut(myDeck, -393)
myDeck = dealWI(myDeck, 4)
myDeck = dealNS(myDeck)
myDeck = cut(myDeck, -4002)
myDeck = dealNS(myDeck)
myDeck = cut(myDeck, -8343)
myDeck = dealNS(myDeck)
myDeck = dealWI(myDeck, 70)
myDeck = dealNS(myDeck)
myDeck = cut(myDeck, 995)
myDeck = dealWI(myDeck, 22)
myDeck = cut(myDeck, 1267)
myDeck = dealWI(myDeck, 47)
myDeck = cut(myDeck, -3161)
myDeck = dealNS(myDeck)
myDeck = dealWI(myDeck, 34)
myDeck = cut(myDeck, -6221)
myDeck = dealWI(myDeck, 26)
myDeck = cut(myDeck, 4956)
myDeck = dealWI(myDeck, 57)
myDeck = dealNS(myDeck)
myDeck = cut(myDeck, -4983)
myDeck = dealWI(myDeck, 36)
myDeck = cut(myDeck, -1101)
myDeck = dealNS(myDeck)
myDeck = dealWI(myDeck, 2)
myDeck = cut(myDeck, 4225)
myDeck = dealWI(myDeck, 35)
myDeck = cut(myDeck, -721)
myDeck = dealWI(myDeck, 17)
myDeck = cut(myDeck, 5866)
myDeck = dealWI(myDeck, 40)
myDeck = cut(myDeck, -531)
myDeck = dealNS(myDeck)
myDeck = dealWI(myDeck, 63)
myDeck = cut(myDeck, -5839)
myDeck = dealWI(myDeck, 30)
myDeck = cut(myDeck, 5812)
myDeck = dealWI(myDeck, 35)
myDeck = dealNS(myDeck)
myDeck = dealWI(myDeck, 46)
myDeck = cut(myDeck, -5638)
myDeck = dealWI(myDeck, 60)
myDeck = dealNS(myDeck)
myDeck = dealWI(myDeck, 33)
myDeck = cut(myDeck, -4690)
myDeck = dealWI(myDeck, 7)
myDeck = cut(myDeck, 6264)
myDeck = dealNS(myDeck)
myDeck = cut(myDeck, 8949)
myDeck = dealNS(myDeck)
myDeck = cut(myDeck, -4329)
myDeck = dealWI(myDeck, 52)
myDeck = cut(myDeck, 3461)
myDeck = dealWI(myDeck, 47)

print myDeck
for i in range(deckSize):
    if myDeck[i] == 2019:
        print i
