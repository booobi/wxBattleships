import wx
# THESE REQUIRE WX.APP OBJECT
# CAN'T BE USED AS STANDALONE

def getTextSizeX(text):
    font = wx.SystemSettings.GetFont(0)
    dc = wx.ScreenDC()
    dc.SetFont(font)
    return dc.GetTextExtent(text)[0]


def getTextSizeY(text):
    font = wx.SystemSettings.GetFont(0)
    dc = wx.ScreenDC()
    dc.SetFont(font)
    return dc.GetTextExtent(text)[1]
