#-*- coding: utf-8 -*-
'''
    MyDeco 모듈 만든거 사용하기
'''
from deco.MyDeco import HelloBye, Auth

@HelloBye
def test1():
    print "test!() called"
    
@Auth
def test2():
    print "test2() called"


if __name__ == '__main__':
    test1()
    test2()
    