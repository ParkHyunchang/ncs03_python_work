#-*- coding: utf-8 -*-


# str type 데이터를 만들어서 참조 값을 변수에 담기

myComment = "abcdeee"

print "id :", id(myComment) # 아이디값 확인
print u"길이:", len(myComment) # 문자열의 길이 확인
print u"e 의 포함 횟수:", myComment.count("e")
print u"시작하는 글자 확인:", myComment.startswith("a")

name1=u"김구라"
name2=u"박현창"
name3=u"김구라"

print "name1 id:",id(name1)
print "name2 id:",id(name2)
print "name3 id:",id(name3)
 
 
isEqual = name1==name2
isEqual2 = name1==name3

print "name1 == name2 :", isEqual
print "name1 == name3 :", isEqual2


