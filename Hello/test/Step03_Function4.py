#-*- coding: utf-8 -*-

# 문자열 format 만들기

result = u"번호:{} 이름:{} 주소:{}".format(1,u"김구라",u"노량진")

print result

print "---------------"

'''

    keyword arguments 를 함수에 전달 받을수도 있다.
    
    **kwargs
    
    - kwargs 는 keyword arguments 의 약자이다.
'''

def test(**kwargs):
    print "kwargs type:",type(kwargs)
    print kwargs

test()
test(num=1)
test(num=1, name=u"김구라", isMan=True)
