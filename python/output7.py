import string

def getParams(code, instr):
    opcode = code[instr] % 100
    param1 = code[instr]/100 % 10
    param2 = code[instr]/1000 % 10
    param3 = code[instr]/10000 % 10
    
    return (opcode, param1, param2, param3)

def getObjects(code, instr, opcode, param1, param2, param3):
    obj1 = 0
    if opcode not in [3,99]:
        if param1 == 1:
            obj1 = code[instr+1]
        else:
            obj1 = code[code[instr+1]]
        
    obj2 = 0
    if opcode not in [3,4,99]:
        if param2 == 1:
            obj2 = code[instr+2]
        else:
            obj2 = code[code[instr+2]]
    
    return (obj1, obj2)
    

def runCode(input, shouldReturn, code, instr):
    i = 0
    while instr < len(code):
        (opcode, param1, param2, param3) = getParams(code, instr)
        
        (obj1, obj2) = getObjects(code, instr, opcode, param1, param2, param3)
        
        if opcode == 1:
            code[code[instr+3]] = obj1 + obj2
            instr += 4
            
        elif opcode == 2:
            code[code[instr+3]] = obj1 * obj2
            instr += 4
            
        elif opcode == 3:
            code[code[instr+1]] = input[i]
            i += 1
            instr += 2
        
        elif opcode == 4:
            if shouldReturn:
                return (obj1, instr+2)
            else:
                print obj1
                
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
        
        elif opcode == 7:
            if obj1 < obj2:
                code[code[instr+3]] = 1
            else:
                code[code[instr+3]] = 0
            instr += 4
            
        elif opcode == 8:
            if obj1 == obj2:
                code[code[instr+3]] = 1
            else:
                code[code[instr+3]] = 0
            instr += 4
        
        elif opcode == 99:
            return (-1, instr)
            break

def inc(seq):
    if seq[3] < seq[4]:
        (a, b) = (seq[3],seq[4])
        (seq[3],seq[4]) = (b, a)
    elif seq[2] < seq[3]:
        (a, b, c) = (seq[2],seq[3],seq[4])
        if a < c:
            (seq[2],seq[3],seq[4]) = (c, a, b)
        else:
            (seq[2],seq[3],seq[4]) = (b, c, a)
    elif seq[1] < seq[2]:
        (a, b, c, d) = (seq[1],seq[2],seq[3],seq[4])
        if a < d:
            (seq[1],seq[2],seq[3],seq[4]) = (d,a,c,b)
        elif a < c:
            (seq[1],seq[2],seq[3],seq[4]) = (c,d,a,b)
        else:
            (seq[1],seq[2],seq[3],seq[4]) = (b,d,c,a)
    elif seq[0] < seq[1]:
        (a, b, c, d, e) = (seq[0],seq[1],seq[2],seq[3],seq[4])
        if a < e:
            (seq[0],seq[1],seq[2],seq[3],seq[4]) = (e,a,d,c,b)
        elif a < d:
            (seq[0],seq[1],seq[2],seq[3],seq[4]) = (d,e,a,c,b)
        elif a < c:
            (seq[0],seq[1],seq[2],seq[3],seq[4]) = (c,e,d,a,b)
        else:
            (seq[0],seq[1],seq[2],seq[3],seq[4]) = (b,e,d,c,a)
        
    # print seq
    return seq

input = [0,0]
phaseSeq = [5,6,7,8,9]
bestOut = 0
bestSeq = [0,0,0,0,0]

for _ in range(120):
    prevOut = 0
    round = 0
    code = []
    for _ in range(5):
        code +=  [[3,8,1001,8,10,8,105,1,0,0,21,38,63,76,93,118,199,280,361,442,99999,3,9,101,3,9,9,102,3,9,9,101,4,9,9,4,9,99,3,9,1002,9,2,9,101,5,9,9,1002,9,5,9,101,5,9,9,1002,9,4,9,4,9,99,3,9,101,2,9,9,102,3,9,9,4,9,99,3,9,101,2,9,9,102,5,9,9,1001,9,5,9,4,9,99,3,9,102,4,9,9,1001,9,3,9,1002,9,5,9,101,2,9,9,1002,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,99]]
    instr = [0,0,0,0,0]
    halted = False
    lastOut = 0
    while round < 200 and halted == False:
        for amp in range(5):
            if round == 0:
                input[0] = phaseSeq[amp]
                input[1] = prevOut
            else:
                input[0] = prevOut
            (prevOut, instr[amp]) = runCode(input, True, code[amp], instr[amp])
            if amp == 4:
                if prevOut == -1:
                    halted = True
                else:
                    lastOut = prevOut
        round += 1
    if round == 200:
        print "need more rounds"
    if bestOut < lastOut:
        bestOut = lastOut
        bestSeq[0:5] = phaseSeq[0:5]
    phaseSeq = inc(phaseSeq)

print bestOut
print bestSeq
