# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Sep 12 2010)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import numpy


###########################################################################
## Class menu
###########################################################################

class menu(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer10 = wx.BoxSizer(wx.VERTICAL)

        bSizer12 = wx.BoxSizer(wx.VERTICAL)

        self.m_button21 = wx.Button(self, wx.ID_ANY, u"Student", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer12.Add(self.m_button21, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_button22 = wx.Button(self, wx.ID_ANY, u"Teacher", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer12.Add(self.m_button22, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_button23 = wx.Button(self, wx.ID_ANY, u"Administrator", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer12.Add(self.m_button23, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer10.Add(bSizer12, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer10)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button21.Bind(wx.EVT_BUTTON, self.Enter_S_1)
        self.m_button22.Bind(wx.EVT_BUTTON, self.Enter_T_1)
        self.m_button23.Bind(wx.EVT_BUTTON, self.Enter_A_1)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def Enter_S_1(self, event):
        event.Skip()

    def Enter_T_1(self, event):
        event.Skip()

    def Enter_A_1(self, event):
        event.Skip()

if __name__ == '__main__':
    app = wx.App(False)
    Menu = menu(None)
    Menu.Show()
    app.MainLoop()