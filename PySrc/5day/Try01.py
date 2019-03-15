# Try01.py
# try except else finally

x = input('숫자 입력\n')

try:
    print(10/int(x))
except ZeroDivisionError as e:
    print('{} : {}으로는 나눌수가 없네요...ㅜㅜ'.format(e, x))

except ValueError as e:
    print('숫자를 입력하세요')
    print(e)

else:
    print('좋은 시도였네')
finally:
    print('입력 : ', x)


