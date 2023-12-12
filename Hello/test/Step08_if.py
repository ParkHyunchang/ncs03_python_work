#-*- coding: utf-8 -*-
'''
    - if 문 사용하기
    
    1. 조건부로 특정 블럭을 수행 하고자 할때 사용
    2. 들여쓰기로 특정 블럭을 구성한다.
'''
from test.Step03_Function4 import result

# 단일 if 문

if True:
    print "ok 1"
    print "ok 2"
    
if False:
    print "ok 3"
    print "ok 4"
    
isWait=True

# 조건부 수행
if isWait:
    print "wait!"
    print "wait!"
    print "wait!"
    
# 양자택일
num=11

if num%2==0:
    print u"{} 은 짝수입니다.".format(num)
else:
    print u"{} 은 홀수입니다.".format(num)

# 다중 if 문
jumsu=85

if jumsu >= 90:
    print u"{} 점은 수입니다.".format(jumsu)
elif jumsu >= 80:
    print u"{} 점은 우입니다.".format(jumsu)
elif jumsu >= 70:
    print u"{} 점은 미입니다.".format(jumsu)
elif jumsu >= 60:
    print u"{} 점은 양입니다.".format(jumsu)
else:
    print u"{} 점은 가입니다.".format(jumsu)

# 참고 (3항 연산)

isMan=True

result = u"남자 입니다." if isMan else u"여자입니다."

print "isMan : ",result
"""
위의 3항 연산은 아래와 같은 로직이다.
result2 = None
if isMan:
    result2 = u"남자입니다."
else:
    result2 = u"여자입니다"
""" 
print u"Step08_if 모듈의 실행 순서가 종료됩니다."




















