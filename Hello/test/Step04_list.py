#-*- coding: utf-8 -*-
'''
    -list type
    1. 순서가 있다.
    2. 여러 type 의 데이터를 저장할 수 있다.
    3. 값 변경 가능
'''

a=[1,2,3]
b=[10, True, "abcd"]
c=[10, 20, 30]
d=a

# 같은 참조값인지 확인!!!
print "a id:", id(a)
print "d id:", id(d)

print "a[0] :",a[0]
print "a[1] :",a[1]
print "a[2] :",a[2]

family=[u"엄마",u"아빠",u"나"]

print u"가족 구성원 목록:", family[0], family[1], family[2]
print u"가족 구성원 수:", len(family)

# list type 에 데이터 추가
family.append(u"남동생")
family.append(u"여동생")

print u"추가된 구성원 :", family[3], family[4]
print u"가족 구성원 수:", len(family)

# 값에 의한 삭제
family.remove(u"남동생")

# 인덱스에 의한 삭제
del family[0]

print u"삭제후 구성원 목록:", family[0], family[1], family[2]
print u"삭제후 구성원 수:", len(family)

# 빈 list type 객체 만들고
numbers=[]

# 데이터 추가
numbers.append(10)
numbers.append(40)
numbers.append(50)
numbers.append(20)
numbers.append(30)

# 맨마지막에 있는걸 하나씩 빼내는 것은 pop 이라고 있어

# list 의 구조 확인
print numbers

# 오름 차순 정렬
numbers.sort()
print u"오름 차순 정렬후  numbers:", numbers

# 내림 차순 정렬
numbers.sort(reverse=True) # keyword argument 전달
print u"내림 차순 정렬후 numbers:", numbers

# slice 연습
numbers2=[1,2,3,4,5,6,7,8,9,10]

print numbers2
print numbers2[0:2]
print numbers2[2:9]
print numbers2[-5:-1]

print range(10)
print range(20)

a = range(5)
print "a type:", type(a)

# list 에 들어있는 값을 하나씩 순서대로 참조해서 
for i in range(10):
    # 출력해보기
    print i
    
print "--------------------------------------------"
    
friends=["cat","dog","elephant","snake","frog"]

for item in friends:
    print item
    
print "--------------------------------------------"
    
for i in range(len(friends)):
    print friends[i]
    
print "Step04_list 모듈의 실행순서가 종료 됩니다."



















