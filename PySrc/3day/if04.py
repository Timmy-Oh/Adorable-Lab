# if04.py

# 입력숫자를 3 으로 나눈 나머지가
# 0 -> 가위, 1 -> 바위, 2 -> 보
# 그렇지 않으면 -> 잘못 입력
print('숫자를 입력하세요')
i1 = int(input())

c = i1 % 3

if c == 0: print('가위')
elif c==1: print('바위')
elif c==2: print('보')
else : print('잘못 입력')

 
