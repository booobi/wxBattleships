import wx
import socket
import cPickle
import SizeHelpers

server_address = ('localhost', 12345)


class MainFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(MainFrame, self).__init__(*args, **kwargs)
        self.initConnection()
        self.requestGameInfo()
        self.initUI()

    # request board + turn
    # enable fire or #waitForOp
    def initConnection(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect(server_address)

    def requestGameInfo(self):
        self.s.send("initialize")
        print "waiting for initialization data from server"  # onInitialWait
        msg = cPickle.loads(self.s.recv(1024))
        if(msg == "Waiting for player to connect"):
            #textfield for waiting - tell player is waiting
            #wait to receive again
            print "I am waiting for player"
            msg = cPickle.loads(self.s.recv(1024))

        self.ownBoardArray = msg
        print "Got board array:", msg

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

        # oppStartX, oppStartY, oppOffsetX, oppOffsetY = 950, 100, 0, 0
        # ownStartX, ownStartY, ownOffsetX, ownOffsetY = 200, 100, 0, 0

        ownStartX, oppStartX, startY, offsetX, offsetY = 200, 950, 100, 0, 0

        # init own buttons(from recv array)
        # 2d 10x10 array

        self.ownBoardButtons = []
        for rowIndex, row in enumerate(self.ownBoardArray):
            for cellIndex, cell in enumerate(row):
                # own board buttons
                ownBoardButton = wx.Button(self.mainPanel, label=cell, size=(40, 40),
                                           pos=(ownStartX + offsetX, startY + offsetY))
                ownBoardButton.Disable()
                self.ownBoardButtons.append(ownBoardButton)

                # opponent board buttons
                oppBoardButton = wx.Button(self.mainPanel, label="", size=(40, 40),
                                           pos=(oppStartX + + offsetX, startY + offsetY))
                oppBoardButton.Bind(wx.EVT_BUTTON, self.OnFire)
                self.opponentBoardButtons.append(oppBoardButton)

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

        # if response contains 'hit'  - call onHit
        # if response contains 'win' - call onHit +  call onWin
        # if response contains 'miss' - call onMiss


app = wx.App()

MainFrame(None)

app.MainLoop()
