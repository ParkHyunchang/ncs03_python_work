#-*- coding: utf-8 -*-

# Step13_main.py

import MyModule, YourModule

print "Step13_main.py __name__ :", __name__

# 만일 main 으로 시작 되었을때 실행할 코드가 있다면
# 아래와 같이 작성한다.

if __name__=="__main__":
    # main 으로 시작 되었을때만 실행순서가 들어온다.
    MyModule.printNick()
    YourModule.printNick()


    














