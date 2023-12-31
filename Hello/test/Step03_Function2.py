#-*- coding: utf-8 -*-

'''
    파이썬 에서는 함수에 전달받는 인자의 갯수를 
    자유롭게 지정할 수 있다.
    
    *args
    
    - args 는 arguments(인자들) 의 약자
    - args 대신에 다른 변수명을 쓸수도 있지만 관례상 args 라고 한다.
'''

def test(*args):
    # args 는 list type 의 read only version 인 tuple type
    print "args type:", type(args)
    print args

test()
test(10)
test(10, 20)
test(10, 20, 30)
test("a", "b", "c")

print "--------------------"

def test2(a, *args):
    print a, args

# test2() #오류발생 인자는 최소 1개는 전달해야 한다.
test2("aaa")

# "bbb" 는 a 라는 변수에 담기고 10,20,30 은 tuple 로 args 에 전달됨!
test2("bbb", 10, 20, 30)


print u"Stpe03_Function2 모듈이 종료 됩니다."






























