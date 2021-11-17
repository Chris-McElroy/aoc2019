# import string

inputCode = [109,424,203,1,21101,11,0,0,1106,0,282,21102,1,18,0,1105,1,259,1202,1,1,221,203,1,21101,0,31,0,1105,1,282,21102,38,1,0,1106,0,259,21002,23,1,2,21202,1,1,3,21102,1,1,1,21102,57,1,0,1106,0,303,1202,1,1,222,20102,1,221,3,20102,1,221,2,21102,259,1,1,21102,80,1,0,1105,1,225,21101,0,145,2,21102,91,1,0,1105,1,303,2101,0,1,223,20101,0,222,4,21102,259,1,3,21101,225,0,2,21102,1,225,1,21102,1,118,0,1105,1,225,20101,0,222,3,21101,0,197,2,21101,133,0,0,1106,0,303,21202,1,-1,1,22001,223,1,1,21101,0,148,0,1105,1,259,1202,1,1,223,21001,221,0,4,21001,222,0,3,21102,1,19,2,1001,132,-2,224,1002,224,2,224,1001,224,3,224,1002,132,-1,132,1,224,132,224,21001,224,1,1,21102,195,1,0,105,1,109,20207,1,223,2,21002,23,1,1,21102,-1,1,3,21101,0,214,0,1105,1,303,22101,1,1,1,204,1,99,0,0,0,0,109,5,1201,-4,0,249,22101,0,-3,1,22101,0,-2,2,21202,-1,1,3,21102,250,1,0,1106,0,225,22101,0,1,-4,109,-5,2105,1,0,109,3,22107,0,-2,-1,21202,-1,2,-1,21201,-1,-1,-1,22202,-1,-2,-2,109,-3,2106,0,0,109,3,21207,-2,0,-1,1206,-1,294,104,0,99,22102,1,-2,-2,109,-3,2105,1,0,109,5,22207,-3,-4,-1,1206,-1,346,22201,-4,-3,-4,21202,-3,-1,-1,22201,-4,-1,2,21202,2,-1,-1,22201,-4,-1,1,21201,-2,0,3,21101,343,0,0,1105,1,303,1105,1,415,22207,-2,-3,-1,1206,-1,387,22201,-3,-2,-3,21202,-2,-1,-1,22201,-3,-1,3,21202,3,-1,-1,22201,-3,-1,2,22101,0,-4,1,21102,384,1,0,1106,0,303,1106,0,415,21202,-4,-1,-4,22201,-4,-3,-4,22202,-3,-2,-2,22202,-2,-4,-4,22202,-3,-2,-3,21202,-4,-1,-2,22201,-3,-2,1,22102,1,1,-4,109,-5,2105,1,0]

def extend(code, n):
    if len(code)-5 < n:
        for _ in range(n-len(code)+5):
            code += [0]

def getParams(code, instr):
    opcode = code[instr] % 100
    param1 = code[instr]/100 % 10
    param2 = code[instr]/1000 % 10
    param3 = code[instr]/10000 % 10
    if opcode == 3:
        param3 = param1

    return (opcode, param1, param2, param3)

def getObjects(code, rBase, instr):
    (opcode, param1, param2, param3) = getParams(code, instr)
    obj1 = 0
    if opcode not in [3,99]:
        if param1 == 1:
            obj1 = code[instr+1]
        elif param1 == 2:
            extend(code, rBase+code[instr+1])
            obj1 = code[rBase+code[instr+1]]
        else:
            extend(code, code[instr+1])
            obj1 = code[code[instr+1]]

    obj2 = 0
    if opcode not in [3,4,9,99]:
        if param2 == 1:
            obj2 = code[instr+2]
        elif param2 == 2:
            extend(code, rBase+code[instr+2])
            obj2 = code[rBase+code[instr+2]]
        else:
            extend(code, code[instr+2])
            obj2 = code[code[instr+2]]


    obj3 = -1
    add = 1 if opcode == 3 else 3

    if opcode in [1,2,3,7,8]:
        if param3 == 0:
            extend(code, code[instr+add])
            obj3 = code[instr+add]
        elif param3 == 2:
            extend(code, rBase + code[instr+add])
            obj3 = rBase + code[instr+add]
        else:
            print "got weird param3"

    return (opcode, obj1, obj2, obj3)

def bump(instr, opcode):
    if opcode in [1,2,7,8]:
        instr += 4
    elif opcode in [3,4]:
        instr += 2
    elif opcode in [5,6]:
        instr += 3
    elif opcode == 9:
        instr += 2
    return instr

def intcode(newCode, pos):
    code = []
    for i in newCode:
        code += [i]
    instr = 0
    i = 0
    input = [1]
    rBase = 0

    while instr < len(code):
        (opcode, obj1, obj2, obj3) = getObjects(code, rBase, instr)

        instr = bump(instr, opcode)

        if opcode == 1:
            code[obj3] = obj1 + obj2
        elif opcode == 2:
            code[obj3] = obj1 * obj2
        elif opcode == 3:
            num = 0
            if i % 2 == 0:
                num = pos[0]
            else:
                num = pos[1]
            code[obj3] = num
            i += 1
        elif opcode == 4:
            return obj1
            # print obj1
        elif opcode == 5:
            if obj1 != 0:
                instr = obj2
        elif opcode == 6:
            if obj1 == 0:
                instr = obj2
        elif opcode == 7:
            code[obj3] = 1 if (obj1 < obj2) else 0
        elif opcode == 8:
            code[obj3] = 1 if (obj1 == obj2) else 0
        elif opcode == 9:
            rBase += obj1
        else:
            if opcode != 99:
                print "weird opcode"
            break

# intcode(inputCode)

size = 100
start = [1865,1593]
sum = 0
area = []
for r in range(size):
    area += [[]]
    for c in range(size):
        area[r] += [2]

lr = 0
for a in range(size):
    if a > size/10*lr:
        print lr
        lr += 1
    for b in range(size):
        area[a][b] = intcode(inputCode,[a+start[0],b+start[1]])
        # sum += area[a][b]

for r in area:
    s = ""
    for c in r:
        s += str(c)
    print s
# print sum
