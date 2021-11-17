import copy

input = "59738571488265718089358904960114455280973585922664604231570733151978336391124265667937788506879073944958411270241510791284757734034790319100185375919394328222644897570527214451044757312242600574353568346245764353769293536616467729923693209336874623429206418395498129094105619169880166958902855461622600841062466017030859476352821921910265996487329020467621714808665711053916709619048510429655689461607438170767108694118419011350540476627272614676919542728299869247813713586665464823624393342098676116916475052995741277706794475619032833146441996338192744444491539626122725710939892200153464936225009531836069741189390642278774113797883240104687033645"
start = 303673
inputL = map(int,input)
print inputL
print len(inputL)
print len(input)*10000-start
while len(inputL) < (len(input)*10001-start)*0.1:
    inputL += map(int,input)

numRounds = 10
theLen = len(inputL)

for r in range(numRounds):
    print inputL[:8]
    for i in range(theLen-1):
        for j in range(i+1,theLen):
            inputL[i] += inputL[j]
            # print i, j, ((j+1)/(i+1)), base[((j+1)/(i+1))%4], inputL[j], newL[i]
        inputL[i] %= 10


# base = [[0,1,0,-1]]
#
# for i in range(1,len(inputL)):
#     base += [[]]
#     if i > 3:
#         base[0] += [base[0][i%4]]
#     for j in range(len(inputL)):
#         base[i] += [base[0][((j+1)/(i+1))%4]]
#
# base[0] += [base[0][(len(inputL)%4)]]
# base[0].remove(0)
# # print base
#
# for r in range(numRounds):
#
#     if r%10 == 0:
#         print inputL[280:]
#     newL = []
#     for i in range(len(inputL)):
#         newL += [0]
#         for j in range(i,len(inputL)):
#             newL[i] += base[i][j]*inputL[j]
#             # print i, j, ((j+1)/(i+1)), base[((j+1)/(i+1))%4], inputL[j], newL[i]
#     for i in range(len(inputL)):
#         inputL[i] = abs(newL[i])%10
print inputL[:8]
