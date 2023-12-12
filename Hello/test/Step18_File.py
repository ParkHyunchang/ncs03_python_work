#-*- coding: utf-8 -*-
import os
import codecs

print u"현재 작업 디렉토리 :", os.getcwd()
print u"파일 플렛폼의 파일 구분자 :", os.sep

try:
    # 읽어올 파일 경로 구성하기
    filePath=os.getcwd()+os.sep+"testFile.txt"
    print filePath
    # 파일 열기 .open(파일경로, 모드, 인코딩)
    f=codecs.open(filePath,"r","utf-8") # 읽기 모드
    # 텍스트 문서의 내용 읽어들이기
    result=f.read()
    print result
    f.close()
    
    # 파일 만들어서 문자열 기록하기
    letterPath=os.getcwd()+os.sep+"testFile2.txt"
    letter=codecs.open(letterPath, "w", "utf-8") # 쓰기 모드
    letter.write(u"To my Friend ~")
    letter.close() # close 하는 순간 파일이 만들어진다.
    
    # 파일을 열어서 문자열 추가하기
    letter2=codecs.open(letterPath, "a", "utf-8") # 추가 모드
    for i in range(10):
        letter2.write(u"\n안녕하세요")
    letter2.close()
    
    print u".readline() 태스트"
    letter3=codecs.open(letterPath, "r", "utf-8")
    # 한줄씩 읽어와서 출력하기
    print letter3.readline()
    print letter3.readline()
    letter3.close()
    
    print u".readlines() 테스트"
    letter4= codecs.open(letterPath, "r", "utf-8")
    # 한줄씩 읽은 데이터를 liest 에 담아서 리턴해준다.
    lines=letter4.readlines()
    # 반복문 돌면서 출력하기
    for item in lines:
        print item
    
except Exception as e:
    # 예외가 발생했을때 실행되는 블럭
    print(e)
    