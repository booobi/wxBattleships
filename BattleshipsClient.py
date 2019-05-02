import wx
import SizeHelpers
from SocketClient import SocketClient

server_address = ('localhost', 12345)


class MainFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(MainFrame, self).__init__(*args, **kwargs)

        self.initialize_connection()
        self.request_initial_game_info()
        self.initUI()

    # request board + turn
    # enable fire or #waitForOp
    def initialize_connection(self):
        self.sock_client = SocketClient()
        self.sock_client.initialize_connection(server_address)

    def request_initial_game_info(self):
        # self.s.send("initialize")
        print "waiting for initialization data from server"  # onInitialWait
        msg = self.sock_client.block_wait_data()
        if (msg == "Waiting for player to connect"):
            # textfield for waiting - tell player is waiting
            # block, wait to receive again
            print "I am waiting for player"
            msg = self.sock_client.block_wait_data()

        self.ownBoardArray = msg
        print "Got board array:", msg

    def initUI(self):
        self.mainPanel = wx.Panel(self)
        self.mainPanel.SetFont(wx.SystemSettings.GetFont(0))

        self.sizeX, self.sizeY = wx.GetDisplaySize()

        self.Show()
        self.Maximize()
        self.initialize_boards()

    def initialize_boards(self):
        quarterPointX = wx.GetDisplaySize()[0] / 4
        wx.StaticText(self.mainPanel, label="Your board",
                      pos=(quarterPointX - SizeHelpers.getTextSizeX("Your board") / 2, 30))
        wx.StaticText(self.mainPanel, label="Opponent board",
                      pos=(self.sizeX - quarterPointX - SizeHelpers.getTextSizeX("Opponent board") / 2, 30))

        self.opponentBoardButtons = []

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
        btnIndx = self.opponentBoardButtons.index(btnObj)

        self.sock_client.send_data(btnIndx)
        # result - True/False
        isHit = True

        # if response contains 'hit'  - call onHit
        # if response contains 'win' - call onHit +  call onWin
        # if response contains 'miss' - call onMiss


app = wx.App()

MainFrame(None)

app.MainLoop()
