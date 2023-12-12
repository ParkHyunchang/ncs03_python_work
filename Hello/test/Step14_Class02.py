#-*- coding: utf-8 -*-

class Car:
    #필드 정의하기
    company = None  # 제조사
    name = None     # 이름
    color = None    # 색상
    
    # 생성자
    def __init__(self, company, name, color):
        print u"__init__() 생성자 호출됨"
        self.company=company
        self.name=name
        self.color=color
    
    # 메소드
    def showInfo(self):
        info = u"제조사:{}, 이름:{}, 색상:{}"\
            .format(self.company, self.name, self.color)
        print info

    
    
if __name__ == '__main__':
    car1=Car(u"현대", u"소나타", u"검정색")
    car2=Car(u"기아", u"K3", u"은색")
    
    car1.showInfo()
    car2.showInfo()
    