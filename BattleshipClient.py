import wx
import socket
import pickle
import SizeHelpers


server_address = ('localhost', 12345)

class MainFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(MainFrame, self).__init__(*args, **kwargs)
        self.initConnection()
        self.requestGameInfo()
        self.initUI()

    #request board + turn
    #enable fire or #waitForOp
    def initConnection(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect(server_address)

    def requestGameInfo(self):
        self.s.send("initialize")
        print "waiting for initialization data from server" # onInitialWait
        self.boardArray = self.s.recv(1024)
        # drawOwnBoard(data)
        print self.boardArray

    def initUI(self):
        self.mainPanel = wx.Panel(self)
        self.mainPanel.SetFont(wx.SystemSettings.GetFont(0))

        self.sizeX, self.sizeY = wx.GetDisplaySize()

        self.Show()
        self.Maximize()
        self.initBoards()

    def initBoards(self):
        quarterPointX = wx.GetDisplaySize()[0] / 4
        wx.StaticText(self.mainPanel, label="Your board",
                      pos=(quarterPointX - SizeHelpers.getTextSizeX("Your board") / 2, 30))
        wx.StaticText(self.mainPanel, label="Opponent board",
                      pos=(self.sizeX - quarterPointX - SizeHelpers.getTextSizeX("Opponent board") / 2, 30))

        self.opponentBoardButtons = []

        startX, startY, offsetX, offsetY = 950, 100, 0, 0


        # init own buttons(from recv array)


        # init enemy buttons
        for i in range(100):
            currentButton = wx.Button(self.mainPanel, label="S", size=(40, 40),
                                      pos=(startX + offsetX, startY + offsetY), id = i)
            currentButton.Bind(wx.EVT_BUTTON, self.OnFire)
            self.opponentBoardButtons.append(currentButton)
            offsetX += 40
            if offsetX > 360:
                offsetY += 40
                offsetX = 0


    def OnFire(self, e):

        btnObj = e.GetEventObject()
        # send guess to server
        self.s.sendall(str(btnObj.GetId()))
        # result - True/False
        isHit = True

        #if response contains hit onHit
        #if response contains win! onHit + onWin
        #if response contains
        if isHit:
            btnObj.Disable()
            # print msg
        else:
            # print msg
            pass

        opponentButtonsLeft = [wx.Button for button in self.opponentBoardButtons if button.IsEnabled()]
        print btnObj.GetId()
        if (opponentButtonsLeft == 0):
            # onWin()
            pass


app = wx.App()

MainFrame(None)

app.MainLoop()
