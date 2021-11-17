# import string

code = [3,8,1005,8,299,1106,0,11,0,0,0,104,1,104,0,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,0,10,4,10,1002,8,1,29,1,1007,14,10,2,1106,8,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,1,8,10,4,10,1002,8,1,58,3,8,1002,8,-1,10,101,1,10,10,4,10,108,0,8,10,4,10,1002,8,1,80,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,0,10,4,10,102,1,8,103,1,5,6,10,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,101,0,8,128,1,106,18,10,1,7,20,10,1006,0,72,1006,0,31,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,0,8,10,4,10,1002,8,1,164,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,1,8,10,4,10,102,1,8,186,1,1007,8,10,1006,0,98,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,0,10,4,10,101,0,8,216,2,102,8,10,1,1008,18,10,1,1108,8,10,1006,0,68,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,1001,8,0,253,3,8,102,-1,8,10,1001,10,1,10,4,10,108,1,8,10,4,10,1002,8,1,274,1,1105,7,10,101,1,9,9,1007,9,1060,10,1005,10,15,99,109,621,104,0,104,1,21102,936995738520,1,1,21102,316,1,0,1106,0,420,21101,0,936995824276,1,21102,1,327,0,1106,0,420,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21102,248129784923,1,1,21102,1,374,0,1105,1,420,21102,29015149735,1,1,21101,385,0,0,1106,0,420,3,10,104,0,104,0,3,10,104,0,104,0,21101,983925826304,0,1,21101,0,408,0,1105,1,420,21102,825012036364,1,1,21101,0,419,0,1105,1,420,99,109,2,22101,0,-1,1,21101,0,40,2,21101,0,451,3,21102,441,1,0,1105,1,484,109,-2,2105,1,0,0,1,0,0,1,109,2,3,10,204,-1,1001,446,447,462,4,0,1001,446,1,446,108,4,446,10,1006,10,478,1101,0,0,446,109,-2,2105,1,0,0,109,4,2102,1,-1,483,1207,-3,0,10,1006,10,501,21102,0,1,-3,21201,-3,0,1,22102,1,-2,2,21102,1,1,3,21101,520,0,0,1106,0,525,109,-4,2105,1,0,109,5,1207,-3,1,10,1006,10,548,2207,-4,-2,10,1006,10,548,21201,-4,0,-4,1105,1,616,21201,-4,0,1,21201,-3,-1,2,21202,-2,2,3,21102,1,567,0,1105,1,525,21202,1,1,-4,21102,1,1,-1,2207,-4,-2,10,1006,10,586,21102,0,1,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,608,21201,-1,0,1,21102,1,608,0,106,0,483,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2106,0,0]

def extendCode(n):
    global code
    if len(code)-5 < n:
        for _ in range(n-len(code)+5):
            code += [0]

def getParams():
    opcode = code[instr] % 100
    param1 = code[instr]/100 % 10
    param2 = code[instr]/1000 % 10
    param3 = code[instr]/10000 % 10
    if opcode == 3:
        param3 = param1
    
    return (opcode, param1, param2, param3)

def getObjects():
    obj1 = 0
    if opcode not in [3,99]:
        if param1 == 1:
            obj1 = code[instr+1]
        elif param1 == 2:
            extendCode(rBase+code[instr+1])
            obj1 = code[rBase+code[instr+1]]
        else:
            extendCode(code[instr+1])
            obj1 = code[code[instr+1]]

    obj2 = 0
    if opcode not in [3,4,9,99]:
        if param2 == 1:
            obj2 = code[instr+2]
        elif param2 == 2:
            extendCode(rBase+code[instr+2])
            obj2 = code[rBase+code[instr+2]]
        else:
            extendCode(code[instr+2])
            obj2 = code[code[instr+2]]
    
    return (obj1, obj2)
    
def bumpInstr():
    global instr
    global rBase
    shouldStop = False
    if opcode in [1,2,7,8]:
        instr += 4
    elif opcode in [3,4]:
        instr += 2
    elif opcode == 5:
        if obj1 != 0:
            instr = obj2
        else:
            instr += 3
    elif opcode == 6:
        if obj1 == 0:
            instr = obj2
        else:
            instr += 3    
    elif opcode == 9:
        rBase += obj1
        instr += 2
    elif opcode == 99:
        shouldStop = True
    else:
        print "got weird opcode"
        shouldStop = True
    return shouldStop

def getOutput():
    global i
    global i2
    global spot
    global area
    global fakeArea
    global visitedAreas
    global dir
    output = 0
    if opcode == 1:
        output = obj1 + obj2
    elif opcode == 2:
        output = obj1 * obj2
    elif opcode == 3:
        # output = input[i2]
        # i += 1
        output = area[spot[0]][spot[1]]
    elif opcode == 4:
        if i == 1:
            if obj1 == 1:
                ph = dir[1]
                dir[1] = -dir[0]
                dir[0] = ph
            else:
                ph = dir[1]
                dir[1] = dir[0]
                dir[0] = -ph
            spot[0] += dir[0]
            spot[1] += dir[1]
            if spot[0] not in range(size) or spot[1] not in range(size):
                print("too small")
            i = 0
            # print obj1
            # print dir
            # print spot
        else:
            i = 1
            area[spot[0]][spot[1]] = obj1
            if fakeArea[spot[0]][spot[1]] == 0:
                visitedAreas += 1
                fakeArea[spot[0]][spot[1]] = 1
            # print obj1
        # print obj1
    elif opcode == 7:
        output = 1 if (obj1 < obj2) else 0
    elif opcode == 8:
        output = 1 if (obj1 == obj2) else 0
    return output

def getPosition():
    add = 1 if opcode == 3 else 3
    position = -1
    global code
    
    if opcode in [1,2,3,7,8]:
        if param3 == 0:
            extendCode(code[instr+add])
            position = code[instr+add]
        elif param3 == 2:
            extendCode(rBase + code[instr+add])
            position = rBase + code[instr+add]
        else:
            print "got weird param3"
    if position not in range(len(code)) and position != -1:
        print position
        print opcode
        print param3
        print "weoif"
        print rBase
        print code[instr+add]
        print len(code)
        print "about to error"
    return position

instr = 0
i = 0
i2 = 0
input = [1]
rBase = 0
size = 200
dir = [-1,0]
spot = [size/2,size/2]
area = [[]]
fakeArea = [[]]
visitedAreas = 0
for r in range(size+1):
    area += [[0]]
    
    fakeArea += [[0]]
    for c in range(size):
        area[r] += [0]
        fakeArea[r] += [0]
area[spot[0]][spot[1]] = 1

while instr < len(code):
    (opcode, param1, param2, param3) = getParams()
    (obj1, obj2) = getObjects()
    output = getOutput()
    pos = getPosition()

    if pos != -1:
        code[pos] = output
    
    if bumpInstr():
        break

print visitedAreas
for i in area:
    s = ""
    for r in i:
        if r == 1:
            s += "&"
        else:
            s += " "
    print s