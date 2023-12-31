#-*- coding: utf-8 -*-

import wx

# wx.Frame 을 상속받은 클래스 정의하기
class MyFrame(wx.Frame):
    
    def __init__(self, parent, title):
        # 부모 생성자에 필요한 값 넘겨주기
        super(MyFrame, self)\
            .__init__(parent, title=title, size=(300, 250))
        
        # 프레임에 TextCtrl 이라는 UI 추가하기
        self.txtA=wx.TextCtrl(self, style=wx.TE_MULTILINE)
        # 하단 상태바 보이게 하기
        self.CreateStatusBar()
        
        # 메뉴바 객체 생성
        menuBar=wx.MenuBar()
        # 메뉴 객체 생성
        mnuFile=wx.Menu()
        # 메뉴 아이템 객체 생성
        mnuNew=wx.MenuItem(mnuFile, wx.ID_NEW, "New", u"새로운 문서")
        
        # 메뉴에 아이템 추가하기
        mnuFile.Append(mnuNew)
        # 메뉴에 아이템 추가하기 2
        mnuOpen=wx.MenuItem(mnuFile, wx.ID_OPEN, "Open", u"파일열기")
        mnuFile.Append(mnuOpen)
        # 구분선 나타내기
        mnuFile.AppendSeparator()
        # 메뉴에 아이템 추가하기 3 (다른방법)
        # 메뉴 아이템의 참조값이 리턴된다.
        mnuExit=mnuFile.Append(wx.ID_EXIT, "Exit", u"종료하기")
        
        # 메뉴바에 메뉴 추가하기
        menuBar.Append(mnuFile, "File")
        # 프레임 메뉴바 추가하기
        self.SetMenuBar(menuBar)
        
        # 화면의 가운데에 보이게 하기
        self.Center()
        self.Show()
        
        # 메뉴 아이템 클릭 이벤트 처리
        self.Bind(wx.EVT_MENU, self.NewClicked, mnuNew)
        self.Bind(wx.EVT_MENU, self.OpenClicked, mnuOpen)
        self.Bind(wx.EVT_MENU, self.ExitClicked, mnuExit)
        
    
    # 메뉴 아이템 New 를 클릭했을때 호출될 메소드 정의
    def NewClicked(self, event):
        # print u"New 를 클릭했네?"
        # text area 에 메세지 출력하기
        self.txtA.SetLabelText(u"New 를 클릭했네?")
        
    # 메뉴 아이템 Open 을 클릭했을때 호출될 메소드 정의
    def OpenClicked(self, event):
        # text area 에 메세지 출력하기
        self.txtA.SetLabelText(u"Open 을 클릭했네?")
        
    def ExitClicked(self, evnet):
        self.Close(True) # 강제 종료
    
    
if __name__ == '__main__':
    # main 으로 실행했을때 실행순서가 들어오는 부분
    
    app=wx.App()
    #MyFrame 객체 생성
    MyFrame(None, title=u"연습")
    app.MainLoop()
    