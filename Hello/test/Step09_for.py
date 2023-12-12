#-*- coding: utf-8 -*-
'''
    - range 내장함수(내장 메소드)와 함께 for 문 사용해보기
'''

print range(10)

names = [u"김구라",u"해골",u"원숭이"]
names.append(u"주뎅이")
names.append(u"덩어리")

for i in range(len(names)):
    print i, u" 번째방의 item : ", names[i]
    
print "-----"

# range(start, end, step)
print range(0, 10, 1)
print range(0, 10, 2)
print range(10, 0, -1)
print range(10, 0, -2)

# names 라는 변수에 담겨있는 이름 목록을 
# for 문을 이용해서 역순으로 출력해 보세요.

for i in range(len(names)-1,-1,-1):
    print i, u"번째 인덱스 item:",names[i]



print u"Step09_for 모듈의 실행순서가 종료 됩니다."



