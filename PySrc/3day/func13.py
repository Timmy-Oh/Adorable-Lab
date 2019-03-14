# Func13.py

def sum(i,j): return i+j
def sub(i,j): return i-j
def mul(i,j): return i*j
def div(i,j): return i/j

# def nmj(i,j): return i%j

a= sum
print(a(20, 10))

#람다식
b = lambda i,j:i%j
print(b(32,5))



calcList = [sum, sub, mul, div, b]
for c in calcList:
    print(c(200, 100))

calcList2 = []
calcList2.append(sum)
calcList2.append(sub)
calcList2.append(mul)
calcList2.append(div)

for c in calcList2:
    print(c(200, 100))

사칙연산 = {'덧셈':sum, '뺄셈':sub}
print(사칙연산['덧셈'](20,25))

