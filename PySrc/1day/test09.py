# Test09.py

# Bool -> True, False

# and, or, not, if, for, while

print(True and False)
print(True | False)
print(True or False)
print(True & False)


print( 1 and 2 )
print( 6 & 3 )
print( 6 or 0 )
print( 6 | 3 )


print(bool(0), bool(''), bool(None), bool([]))
print(bool({}), bool(()), bool(False), bool(0.))

print(0. == .0)

print(bool([[]]))


class Luncher():
    def __init__(self):
        self.menu_ate = ['닭갈비전']
        self.menu_bucket = ['후꾸짱', '참맛집', '산수정', '남쪽나라', '황성',
                       '대풍', '동경주방', '닭갈비전', '우렁식탁', '홍콩반점']

        while self.menu_ate != []:
            m = self.menu_ate.pop()
            for i, value in enumerate(self.menu_bucket):
                if value == m:
                    del self.menu_bucket[i]
                    break

    def run(self):
        n = input('랜덤점신메뉴고르기 : 숫자 1~999 중 하나를 넣어주세요\n')
        num_menu = ((int(n)*13*19)+2)%len(self.menu_bucket)
        print('오늘의 점심은 {}입니다!'.format(self.menu_bucket[num_menu]))



#print(menu_bucket)
    
