import string

f = open('input1', 'r')
x = map(int, f.readlines())
y = []
for n in range(len(x)):
    i = x[n]
    y += [0]
    i = i/3 - 2
    while i > 0:
        y[n] += i
        i = i/3 - 2

print x
print y
print sum(y)