#-*- coding: utf-8 -*-

import wx

class MyFram(wx.Frame):
    
    def __init__(self, parent, title):
        super(MyFram, self).__init__(parent, title=title, size=(300, 500))
        
        # 생성자에서  UI 초기화 하는 메소드를 호출하는 구조로 만든다.
        self.InitUI()
        self.Center()
        self.Show()
    def InitUI(self):
        # panel 객체의 참조값 얻어오기
        panel=wx.Panel(self)
        
        # 일반 버튼 객체 만들기
        btn1=wx.Button(panel, label=u"눌러보셈", pos=(5, 5))
        # 토글 버튼
        btn2=wx.ToggleButton(panel, label=u"토글버튼", pos=(100, 5))
        # 일반 버튼
        btn3=wx.Button(panel, label=u"종료", pos=(195, 5))
        
        # 버튼 이벤트 처리 메소드 등록하기
        btn1.Bind(wx.EVT_BUTTON, self.Btn1Clicked)
        btn2.Bind(wx.EVT_TOGGLEBUTTON, self.Btn2Clicked)
        btn3.Bind(wx.EVT_BUTTON, self.Btn3Clicked)
        
    def Btn1Clicked(self, event):
        # 메세지 다이얼로그 띄우기
        dlg=wx.MessageDialog(self, u"메세지", u"제목", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
        print u"BtnClicked() 리턴됨!"
        
    def Btn2Clicked(self, event):
        # 토글 버든의 상태를 bool type 으로 얻어올수 있다.
        # 눌러진 버튼의 참조값을 얻어와서 처리할 수 있다.
        isActive=event.GetEventObject().GetValue()
        if isActive:
            print "activated!"
        else:
            print "not activated!"
        
    def Btn3Clicked(self, event):
        self.Close(True)
    
    
        
if __name__ == "__main__":
    app=wx.App()
    MyFram(None, title="버튼 테스트")
    app.MainLoop()
    
    
    
    