#-*- coding: utf-8 -*-


if __name__ == '__main__':
    try:
        num1 = input("젯수 입력:")
        num2 = input("피젯수 입력:")
        print num2,"를", num1, "으로 나눈값:", num2/num1
    except ZeroDivisionError as zde:
        print "어떤수를 0으로 나눌수는 없습니다.", zde
    except Exception as e:
        print "알수 없는 에러 발생!", e
    else:
        print "오류없이 수행되었습니다."
    finally:
        print "오류발생과 상관없이 반듯이 실행이 보장되는 블럭입니다."
    
    print "프로그램을 마무리 합니다."
