# -*- coding:utf-8 -*-

import mysql.connector
from errno import errorcode

#DB 접속정보를 dict type 으로 준비한다.

config={
        "user":"root",
        "password":"maria",
        "host":"127.0.0.1",
        "database":"acorn",
        "port":3306
    }

try:
    #Maria DB 연결 객체
    # **config => kwargs 를 dict type 으로 매칭시키기
    conn=mysql.connector.connect(**config)
    #연결되는지 확인
    print conn
    
    # member 테이블에 저장할 정보
    name1 = u"해골"
    addr1 = u"행신동"
    
    # 실행할 sql문 준비하기
    sql=u"INSERT INTO member (name,addr) VALUES(%s, %s)"
    
    # %s 에 바인딩 할 내용을 tuple type 에 담는다.
    sql_arg=(name1, addr1)
    
    # db 에 select, insert, update, delete 등의 작업을 할 객체 
    cursor=conn.cursor()
    # .execute(수행할 sql 문, %s 바인딩할 인자들)
    cursor.execute(sql, sql_arg)
    
    conn.commit()
    print u"member 테이블에 정보를 저장했습니다."
    
except mysql.connector.Error as err:
    # 예외가 발생했을 때 수행할 작업
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print "아이디 혹은 비밀번호가 틀려요"
    elif err.errno == errorcode.ER_BAD_ERROR:
        print "DB 오류"
    else:
        print "기타 오류"
    conn.rollback()
else:
    print "정상 수행했습니다."
finally:
    #예외가 발생하던 안하던 수행이 보장되는 블럭에서 마무리 작업
    cursor.close()
    conn.close()
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    