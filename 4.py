# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Sep 12 2010)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import basicwork as bk
import wx




###########################################################################
## Class main
###########################################################################

class main(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_button2 = wx.Button(self, wx.ID_ANY, u"scores", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.m_button2, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_button3 = wx.Button(self, wx.ID_ANY, u"graph", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.m_button3, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_textCtrl1 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.m_textCtrl1, 0, wx.ALL | wx.EXPAND, 5)

        self.m_button31 = wx.Button(self, wx.ID_ANY, u"student", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.m_button31, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_textCtrl2 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.m_textCtrl2, 0, wx.ALL | wx.EXPAND, 5)

        self.m_button4 = wx.Button(self, wx.ID_ANY, u"teacher", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.m_button4, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_textCtrl3 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.m_textCtrl3, 0, wx.ALL | wx.EXPAND, 5)

        self.m_button5 = wx.Button(self, wx.ID_ANY, u"administrator", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.m_button5, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button2.Bind(wx.EVT_BUTTON, self.show_scores)
        self.m_button3.Bind(wx.EVT_BUTTON, self.show_graph)
        self.m_button31.Bind(wx.EVT_BUTTON, self.enter_student_interface)
        self.m_button4.Bind(wx.EVT_BUTTON, self.enter_teacher_interface)
        self.m_button5.Bind(wx.EVT_BUTTON, self.enter_administrator_interface)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def show_scores(self, event):
        event.Skip()

    def show_graph(self, event):
        event.Skip()
        bk.graph()


    def enter_student_interface(self, event):
        event.Skip()


    def enter_teacher_interface(self, event):
        event.Skip()


    def enter_administrator_interface(self, event):
        event.Skip()


###########################################################################
## Class student
###########################################################################

class student(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        self.m_button6 = wx.Button(self, wx.ID_ANY, u"search", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.m_button6, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_textCtrl4 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.m_textCtrl4, 1, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(bSizer2)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button6.Bind(wx.EVT_BUTTON, self.search_score)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def search_score(self, event):
        event.Skip()


###########################################################################
## Class teacher
###########################################################################

class teacher(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        self.m_textCtrl9 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.m_textCtrl9, 0, wx.ALL | wx.EXPAND, 5)

        self.m_button10 = wx.Button(self, wx.ID_ANY, u"add", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.m_button10, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_textCtrl10 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.m_textCtrl10, 0, wx.ALL | wx.EXPAND, 5)

        self.m_button11 = wx.Button(self, wx.ID_ANY, u"delete", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.m_button11, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_textCtrl11 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.m_textCtrl11, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_textCtrl12 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.m_textCtrl12, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_button12 = wx.Button(self, wx.ID_ANY, u"change", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.m_button12, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.SetSizer(bSizer4)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button10.Bind(wx.EVT_BUTTON, self.add_student)
        self.m_button11.Bind(wx.EVT_BUTTON, self.delete_student)
        self.m_button12.Bind(wx.EVT_BUTTON, self.change_score)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def add_student(self, event):
        event.Skip()

    def delete_student(self, event):
        event.Skip()

    def change_score(self, event):
        event.Skip()



    app = wx.App()
    Main = main(None)
    Main.Show()
    app.MainLoop()

