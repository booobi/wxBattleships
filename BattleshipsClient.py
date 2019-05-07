import wx
import SizeHelpers
from SocketClient import SocketClient
from pubsub import pub
from ReceiverThread import ReceiverThread

server_address = ('localhost', 12345)


class MainFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(MainFrame, self).__init__(*args, **kwargs)

        self.initialize_connection()
        self.initialize_frame_UI()
        self.initialize_action_text_UI()
        pub.subscribe(self.initialize_board_data, "initial")
        pub.subscribe(self.on_waiting_opponent, "wait_connect")
        # pub.subscribe(self.on_opponent_turn, "wait_turn")
        # pub.subscribe(self.on_own_turn, "go_turn")
        ReceiverThread(self.sock_client)

    # request board + turn
    # enable fire or #waitForOp

    def initialize_connection(self):
        self.sock_client = SocketClient()
        self.sock_client.initialize_connection(server_address)

    def initialize_frame_UI(self):
        self.mainPanel = wx.Panel(self)
        self.mainPanel.SetFont(wx.SystemSettings.GetFont(0))

        self.sizeX, self.sizeY = wx.GetDisplaySize()

        self.Show()

        self.Maximize()

    def initialize_action_text_UI(self):
        action_text = "Waiting for opponent to connect ..."
        self.action_text_field = wx.StaticText(self.mainPanel,
                                               pos=(775 - SizeHelpers.getTextSizeX(action_text) / 2, 150),
                                               label=action_text)

    def initialize_board_data(self, arr):
        self.ownBoardArray = arr
        wx.CallAfter(self.initialize_boards_UI)

    def initialize_boards_UI(self):
        print "called init BOARDS"
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
        for row in self.ownBoardArray:
            for cell in row:
                # own board buttons
                ownBoardButton = wx.Button(self.mainPanel, label=cell, size=(40, 40),
                                           pos=(ownStartX + offsetX, startY + offsetY))
                ownBoardButton.Disable()
                self.ownBoardButtons.append(ownBoardButton)

                # opponent board buttons
                oppBoardButton = wx.Button(self.mainPanel, label="A", size=(40, 40),
                                           pos=(oppStartX + + offsetX, startY + offsetY))
                oppBoardButton.Bind(wx.EVT_BUTTON, self.OnFire)
                self.opponentBoardButtons.append(oppBoardButton)

                offsetX += 40
                if offsetX > 360:
                    offsetY += 40
                    offsetX = 0
        ReceiverThread(self.sock_client)

    def set_action_text(self, text):
        self.action_text_field.SetLabelText(text)

    def on_waiting_opponent(self):
        ReceiverThread(self.sock_client)

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
