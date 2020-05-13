from PyQt5 import QtCore, QtGui, QtWidgets
from random import randrange
import ranges
from chart import coords
allhands = [['aa', 'aks', 'aqs', 'ajs', 'ats', 'a9s', 'a8s', 'a7s', 'a6s', 'a5s', 'a4s', 'a3s', 'a2s'],
            ['ako', 'kk', 'kqs', 'kjs', 'kts', 'k9s', 'k8s', 'k7s', 'k6s', 'k5s', 'k4s', 'k3s', 'k2s'],
            ['aqo', 'kqo', 'qq', 'qjs', 'qts', 'q9s', 'q8s', 'q7s', 'q6s', 'q5s', 'q4s', 'q3s', 'q2s'],
            ['ajo', 'kjo', 'qjo', 'jj', 'jts', 'j9s', 'j8s', 'j7s', 'j6s', 'j5s', 'j4s', 'j3s', 'j2s'],
            ['ato', 'kto', 'qto', 'jto', 'tt', 't9s', 't8s', 't7s', 't6s', 't5s', 't4s', 't3s', 't2s'],
            ['a9o', 'k9o', 'q9o', 'j9o', 't9o', '99', '98s', '97s', '96s', '95s', '94s', '93s', '92s'],
            ['a8o', 'k8o', 'q8o', 'j8o', 't8o', '98o', '88', '87s', '86s', '85s', '84s', '83s', '82s'],
            ['a7o', 'k7o', 'q7o', 'j7o', 't7o', '97o', '87o', '77', '76s', '75s', '74s', '73s', '72s'],
            ['a6o', 'k6o', 'q6o', 'j6o', 't6o', '96o', '86o', '76o', '66', '65s', '64s', '63s', '62s'],
            ['a5o', 'k5o', 'q5o', 'j5o', 't5o', '95o', '85o', '75o', '65o', '55', '54s', '53s', '52s'],
            ['a4o', 'k4o', 'q4o', 'j4o', 't4o', '94o', '84o', '74o', '64o', '54o', '44', '43s', '42s'],
            ['a3o', 'k3o', 'q3o', 'j3o', 't3o', '93o', '83o', '73o', '63o', '53o', '43o', '33', '32s'],
            ['a2o', 'k2o', 'q2o', 'j2o', 't2o', '92o', '82o', '72o', '62o', '52o', '42o', '32o', '22']]


class Ui_Dialog():
    def setupUi(self, Dialog):
        Dialog.setObjectName("Opening Ranges")
        Dialog.setFixedSize(486, 264)
        Dialog.setWindowIcon(QtGui.QIcon("Spin and Go Preflop Charts/icon.png"))

        # LINES AND STATIC LABELS
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(90, 0, 31, 61))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(0, 50, 106, 21))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(105, 50, 396, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Dialog)
        self.line_4.setGeometry(QtCore.QRect(124, 58, 31, 206))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(Dialog)
        self.line_5.setGeometry(QtCore.QRect(0, 255, 151, 21))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.stacklabel = QtWidgets.QLabel(Dialog)
        self.stacklabel.setGeometry(QtCore.QRect(143, 64, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.stacklabel.setFont(font)
        self.stacklabel.setObjectName("stacklabel")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(308, 84, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(338, 84, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(368, 84, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(398, 84, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(428, 84, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(456, 84, 23, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.line_6 = QtWidgets.QFrame(Dialog)
        self.line_6.setGeometry(QtCore.QRect(139, 95, 407, 21))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.handlabel = QtWidgets.QLabel(Dialog)
        self.handlabel.setGeometry(QtCore.QRect(166, 114, 46, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.handlabel.setFont(font)
        self.handlabel.setObjectName("handlabel")
        self.line_7 = QtWidgets.QFrame(Dialog)
        self.line_7.setGeometry(QtCore.QRect(138, 182, 407, 21))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.result = QtWidgets.QLabel(Dialog)
        self.result.setGeometry(QtCore.QRect(168, 150, 303, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.result.setFont(font)
        self.result.setObjectName("result")
        self.line_9 = QtWidgets.QFrame(Dialog)
        self.line_9.setGeometry(QtCore.QRect(150, 152, 31, 26))
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(Dialog)
        self.line_10.setGeometry(QtCore.QRect(164, 142, 312, 21))
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.line_11 = QtWidgets.QFrame(Dialog)
        self.line_11.setGeometry(QtCore.QRect(460, 152, 31, 26))
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.line_12 = QtWidgets.QFrame(Dialog)
        self.line_12.setGeometry(QtCore.QRect(164, 168, 310, 21))
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.bblabel = QtWidgets.QLabel(Dialog)
        self.bblabel.setGeometry(QtCore.QRect(252, 62, 56, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bblabel.setFont(font)
        self.bblabel.setObjectName("bblabel")

        # HAND ENTRY GUI

        # entry box
        self.hand = QtWidgets.QLineEdit(Dialog)
        self.hand.setGeometry(QtCore.QRect(218, 110, 55, 33))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.hand.setFont(font)
        self.hand.setObjectName("hand")
        self.hand.setMaxLength(4)
        self.hand.textEdited.connect(lambda: textchanged(self))
        def textchanged(self):
            self.result.setText("")

        # ENTER
        self.lookupbutton = QtWidgets.QPushButton(Dialog)
        self.lookupbutton.setGeometry(QtCore.QRect(286, 115, 72, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lookupbutton.setFont(font)
        self.lookupbutton.setObjectName("lookupbutton")
        self.lookupbutton.clicked.connect(lambda: lookup(self))

        def lookup(self):
            hand = self.hand.text()
            if hand == "":
                return None
            hand = hand.replace("10","t")
            hand = hand.lower()
            stacksize = (int(self.stackslider.value())/4)
            order  = ["a","k","q","j","t","9","8","7","6","5","4","3","2"]
            if len(hand) < 2:
                self.result.setText("Invalid Hand")
                return None
            if not hand[0] in order or not hand[1] in order:
                self.result.setText("Invalid Hand")
                return None
            if hand[0] == hand[1] and not len(hand) == 2:
                self.result.setText("Invalid Hand")
                return None
            if not hand[0] == hand[1] and (not len(hand) == 3 or not hand[2] in ["o","s"]):
                self.result.setText("Invalid Hand")
                return None

            if order.index(hand[0]) > order.index(hand[1]):
                handlist = list(hand)
                card1 = handlist[0]
                card2 = handlist[1]
                handlist[0] = card2
                handlist[1] = card1
                hand = ''.join(handlist)
            x = None
            y = None
            for i in range(13):
                for j in range(13):
                    if hand == allhands[i][j]:
                        x = j
                        y = i

            if x == None or y == None:
                self.result.setText("Invalid Hand")
                return None

            if self.threehanded.isChecked():
                handed = 3
            elif self.twohanded.isChecked():
                handed = 2

            if self.pos1.isChecked():
                posit = 1
            elif self.pos2.isChecked():
                posit = 2
            elif self.pos3.isChecked():
                posit = 3

            if self.action1.isChecked():
                act = 1
            elif self.action2.isChecked():
                act = 2
            elif self.action3.isChecked():
                act = 3
            elif self.action4.isChecked():
                act = 4
            elif self.action5.isChecked():
                act = 5
            elif self.action6.isChecked():
                act = 6
            else:
                act = 7
            self.result.setText(ranges.lookup(x,y,handed,posit,act,stacksize))
            return None

        # VIEW FULL CHART
        self.viewchart = QtWidgets.QPushButton(Dialog)
        self.viewchart.setGeometry(QtCore.QRect(360, 115, 116, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.viewchart.setFont(font)
        self.viewchart.setObjectName("viewchart")
        self.viewchart.clicked.connect(lambda: determinechart(self))

        def determinechart(self):
            hand = self.hand.text()
            if hand == "":
                hand = "22"
            hand = hand.replace("10", "t")
            hand = hand.lower()
            stacksize = (int(self.stackslider.value()) / 4)
            order = ["a", "k", "q", "j", "t", "9", "8", "7", "6", "5", "4", "3", "2"]
            if len(hand) < 2:
                self.result.setText("Invalid Hand")
                return None
            if not hand[0] in order or not hand[1] in order:
                self.result.setText("Invalid Hand")
                return None
            if hand[0] == hand[1] and not len(hand) == 2:
                self.result.setText("Invalid Hand")
                return None
            if not hand[0] == hand[1] and (not len(hand) == 3 or not hand[2] in ["o", "s"]):
                self.result.setText("Invalid Hand")
                return None

            if order.index(hand[0]) > order.index(hand[1]):
                handlist = list(hand)
                card1 = handlist[0]
                card2 = handlist[1]
                handlist[0] = card2
                handlist[1] = card1
                hand = ''.join(handlist)
            x = None
            y = None
            for i in range(13):
                for j in range(13):
                    if hand == allhands[i][j]:
                        x = j
                        y = i

            if x == None or y == None:
                self.result.setText("Invalid Hand")
                return None

            if self.threehanded.isChecked():
                handed = 3
            elif self.twohanded.isChecked():
                handed = 2

            if self.pos1.isChecked():
                posit = 1
            elif self.pos2.isChecked():
                posit = 2
            elif self.pos3.isChecked():
                posit = 3

            if self.action1.isChecked():
                act = 1
            elif self.action2.isChecked():
                act = 2
            elif self.action3.isChecked():
                act = 3
            elif self.action4.isChecked():
                act = 4
            elif self.action5.isChecked():
                act = 5
            elif self.action6.isChecked():
                act = 6
            else:
                act = 7
            (posx, posy,chart,chartpath) = coords(x,y,handed,posit,act,stacksize)

            displaychart(self,posx,posy,chart,chartpath)
            return None



        def displaychart(self, posx, posy,chart,chartpath):
            win = QtWidgets.QDialog()
            win.setWindowIcon(QtGui.QIcon("Spin and Go Preflop Charts/icon.png"))
            win.setWindowTitle(chart)
            chartpath = chartpath
            imagelabel = QtWidgets.QLabel(win)
            pixmap = QtGui.QPixmap(chartpath)
            imagelabel.setPixmap(pixmap)
            if chart == "Nash Push" or chart == "Nash Call":
                squarelabel = QtWidgets.QLabel(win)
                squarepixmap = QtGui.QPixmap("Spin and Go Preflop Charts/nashsquare.png")
                squarelabel.setPixmap(squarepixmap)
                win.setFixedSize(pixmap.width(), pixmap.height())
            # elif chart == "BB vs SB shove 3-way" or chart == "BB vs BU shove 3-way" or chart == "BB defend vs shove HU":
            #     squarelabel = QtWidgets.QLabel(win)
            #     squarepixmap = QtGui.QPixmap('Spin and Go Preflop Charts/square.png')
            #     squarelabel.setPixmap(squarepixmap)
            #     win.setFixedSize(pixmap.width(), pixmap.height())
            else:
                squarelabel = QtWidgets.QLabel(win)
                squarepixmap = QtGui.QPixmap("Spin and Go Preflop Charts/square.png")
                squarelabel.setPixmap(squarepixmap)
                # colorlabel = QtWidgets.QLabel(win)
                # colorlabelpixmap = QtGui.QPixmap('Spin and Go Preflop Charts/Headsup Charts/Colour code.png')
                # colorlabel.setPixmap(colorlabelpixmap)
                # win.setFixedSize(pixmap.width(), pixmap.height() + colorlabelpixmap.height())
                # colorlabel.setGeometry(QtCore.QRect(0, pixmap.height()-10, colorlabelpixmap.width(), colorlabelpixmap.height()))
                win.setFixedSize(pixmap.width(), pixmap.height())


            squarelabel.setGeometry(QtCore.QRect(posx, posy, squarepixmap.width(), squarepixmap.height()))

            win.exec_()


        # STACK SLIDER
        self.stackslider = QtWidgets.QSlider(Dialog)
        self.stackslider.setGeometry(QtCore.QRect(310, 65, 160, 22))
        self.stackslider.setOrientation(QtCore.Qt.Horizontal)
        self.stackslider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.stackslider.setTickInterval(4)
        self.stackslider.setObjectName("stackslider")
        self.stackslider.valueChanged.connect((lambda: stackchanged(self)))
        # 0 to 100 default


        def stackchanged(self):
            stack = self.stackslider.value()/4
            self.result.setText("")
            if stack > 24.5:
                self.bblabel.setText("25+ BB")
            else:
                self.bblabel.setText("{:4.1f}".format(stack) + " BB")

        # POSITION GUI
        self.PositionBox = QtWidgets.QGroupBox(Dialog)
        self.PositionBox.setEnabled(True)
        self.PositionBox.setGeometry(QtCore.QRect(103, 4, 384, 56))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PositionBox.setFont(font)
        self.PositionBox.setObjectName("PositionBox")

        self.pos1 = QtWidgets.QRadioButton(self.PositionBox)
        self.pos1.setGeometry(QtCore.QRect(6, 24, 111, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pos1.setFont(font)
        self.pos1.setObjectName("pos1")
        self.pos1.toggled.connect(lambda: position(self))

        self.pos2 = QtWidgets.QRadioButton(self.PositionBox)
        self.pos2.setGeometry(QtCore.QRect(106, 24, 111, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pos2.setFont(font)
        self.pos2.setObjectName("pos2")
        self.pos2.toggled.connect(lambda: position(self))

        self.pos3 = QtWidgets.QRadioButton(self.PositionBox)
        self.pos3.setGeometry(QtCore.QRect(226, 24, 111, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pos3.setFont(font)
        self.pos3.setObjectName("pos3")
        self.pos3.toggled.connect(lambda: position(self))

        def position(self):
            self.result.setText("")
            if self.twohanded.isChecked():
                if self.pos1.isChecked():
                    self.action1.setText("SB minraise")
                    self.action1.setVisible(True)

                    self.action2.setText("SB shove")
                    self.action2.setVisible(True)

                    self.action3.setText("SB limp")
                    self.action3.setVisible(True)

                    self.action4.setText("")
                    self.action4.setVisible(False)

                    self.action5.setText("")
                    self.action5.setVisible(False)

                    self.action6.setText("")
                    self.action6.setVisible(False)

                    self.action7.setText("")
                    self.action7.setVisible(False)
                if self.pos2.isChecked():
                    self.action1.setText("Open")
                    self.action1.setVisible(True)

                    self.action2.setText("")
                    self.action2.setVisible(False)

                    self.action3.setText("")
                    self.action3.setVisible(False)

                    self.action4.setText("")
                    self.action4.setVisible(False)

                    self.action5.setText("")
                    self.action5.setVisible(False)

                    self.action6.setText("")
                    self.action6.setVisible(False)

                    self.action7.setText("")
                    self.action7.setVisible(False)
                if self.pos3.isChecked():
                    self.action1.setText("Push")
                    self.action1.setVisible(True)

                    self.action2.setText("Call")
                    self.action2.setVisible(True)

                    self.action3.setText("")
                    self.action3.setVisible(False)

                    self.action4.setText("")
                    self.action4.setVisible(False)

                    self.action5.setText("")
                    self.action5.setVisible(False)

                    self.action6.setText("")
                    self.action6.setVisible(False)

                    self.action7.setText("")
                    self.action7.setVisible(False)
            if self.threehanded.isChecked():
                if self.pos1.isChecked():
                    self.action1.setText("BU minraise")
                    self.action1.setVisible(True)

                    self.action2.setText("BU shove")
                    self.action2.setVisible(True)

                    self.action3.setText("BU limp")
                    self.action3.setVisible(True)

                    self.action4.setText("SB minraise")
                    self.action4.setVisible(True)

                    self.action5.setText("SB 2.5x")
                    self.action5.setVisible(True)

                    self.action6.setText("SB shove")
                    self.action6.setVisible(True)

                    self.action7.setText("SB limp")
                    self.action7.setVisible(True)

                if self.pos2.isChecked():
                    self.action1.setText("BU minraise")
                    self.action1.setVisible(True)

                    self.action2.setText("BU limp")
                    self.action2.setVisible(True)

                    self.action3.setText("BU fold")
                    self.action3.setVisible(True)

                    self.action4.setText("")
                    self.action4.setVisible(False)

                    self.action5.setText("")
                    self.action5.setVisible(False)

                    self.action6.setText("")
                    self.action6.setVisible(False)

                    self.action7.setText("")
                    self.action7.setVisible(False)

                if self.pos3.isChecked():
                    self.action1.setText("Open")
                    self.action1.setVisible(True)

                    self.action2.setText("")
                    self.action2.setVisible(False)

                    self.action3.setText("")
                    self.action3.setVisible(False)

                    self.action4.setText("")
                    self.action4.setVisible(False)

                    self.action5.setText("")
                    self.action5.setVisible(False)

                    self.action6.setText("")
                    self.action6.setVisible(False)

                    self.action7.setText("")
                    self.action7.setVisible(False)
            self.action1.setChecked(True)

        # NUMBER OF PLAYERS GUI
        self.playersbox = QtWidgets.QGroupBox(Dialog)
        self.playersbox.setGeometry(QtCore.QRect(-4, 4, 110, 56))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.playersbox.setFont(font)
        self.playersbox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.playersbox.setObjectName("playersbox")

        self.twohanded = QtWidgets.QRadioButton(self.playersbox)
        self.twohanded.setGeometry(QtCore.QRect(60, 24, 41, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.twohanded.setFont(font)
        self.twohanded.setObjectName("twohanded")
        self.twohanded.toggled.connect(lambda: players(self))

        self.threehanded = QtWidgets.QRadioButton(self.playersbox)
        self.threehanded.setGeometry(QtCore.QRect(12, 24, 42, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.threehanded.setFont(font)
        self.threehanded.setObjectName("threehanded")
        self.threehanded.toggled.connect(lambda: players(self))

        def players(self):
            self.result.setText("")
            if self.twohanded.isChecked():
                if self.pos3.isChecked():
                    self.pos2.setChecked(True)
                self.pos3.setText("Nash Eq")
            if self.threehanded.isChecked():
                if self.pos3.isChecked():
                    self.pos1.setChecked(True)
                self.pos3.setText("Button")
            position(self)


        # ACTION GUI
        self.actionbox = QtWidgets.QGroupBox(Dialog)
        self.actionbox.setGeometry(QtCore.QRect(1, 62, 139, 204))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.actionbox.setFont(font)
        self.actionbox.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.actionbox.setObjectName("actionbox")

        self.action1 = QtWidgets.QRadioButton(self.actionbox)
        self.action1.setGeometry(QtCore.QRect(10, 24, 106, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.action1.setFont(font)
        self.action1.setObjectName("action1")

        self.action2 = QtWidgets.QRadioButton(self.actionbox)
        self.action2.setGeometry(QtCore.QRect(10, 48, 106, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.action2.setFont(font)
        self.action2.setObjectName("action2")

        self.action3 = QtWidgets.QRadioButton(self.actionbox)
        self.action3.setGeometry(QtCore.QRect(10, 72, 106, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.action3.setFont(font)
        self.action3.setObjectName("action3")

        self.action4 = QtWidgets.QRadioButton(self.actionbox)
        self.action4.setGeometry(QtCore.QRect(10, 96, 106, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.action4.setFont(font)
        self.action4.setObjectName("action4")

        self.action5 = QtWidgets.QRadioButton(self.actionbox)
        self.action5.setGeometry(QtCore.QRect(11, 120, 106, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.action5.setFont(font)
        self.action5.setObjectName("action5")

        self.action6 = QtWidgets.QRadioButton(self.actionbox)
        self.action6.setGeometry(QtCore.QRect(10, 144, 106, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.action6.setFont(font)
        self.action6.setObjectName("action6")

        self.action7 = QtWidgets.QRadioButton(self.actionbox)
        self.action7.setGeometry(QtCore.QRect(10, 168, 106, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.action7.setFont(font)
        self.action7.setObjectName("action7")

        # RANDOM HAND GUI
        self.randomhandbutton = QtWidgets.QPushButton(Dialog)
        self.randomhandbutton.setGeometry(QtCore.QRect(158, 199, 116, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.randomhandbutton.setFont(font)
        self.randomhandbutton.setObjectName("randomhandbutton")
        self.randomhandbutton.clicked.connect(lambda: randomhand(self))

        def randomhand(self):
            selectedhand = allhands[randrange(13)][randrange(13)]
            self.hand.setText(selectedhand[0].upper() + selectedhand[1].upper() + selectedhand[2:])
            self.result.setText("")
            return None

        self.randomspotbutton = QtWidgets.QPushButton(Dialog)
        self.randomspotbutton.setGeometry(QtCore.QRect(158, 230, 116, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.randomspotbutton.setFont(font)
        self.randomspotbutton.setObjectName("randomspotbutton")
        self.randomspotbutton.clicked.connect(lambda: randomspot(self))

        def randomspot(self):
            self.stackslider.setValue(randrange(25, 100))
            randomplayers = randrange(0,2)
            if randomplayers == 0:
                self.threehanded.setChecked(True)
                randomposition = randrange(0,3)
            else:
                self.twohanded.setChecked(True)
                randomposition = randrange(0,2)
            players(self)

            if randomposition == 0:
                self.pos1.setChecked(True)
            elif randomposition == 1:
                self.pos2.setChecked(True)
            else:
                self.pos3.setChecked(True)
            position(self)

            if randomplayers == 0:
                if randomposition == 0:
                    randomaction = randrange(7)
                elif randomposition == 1:
                    randomaction = randrange(3)
                else:
                    randomaction = 0
            elif randomplayers == 1:
                if randomposition == 0:
                    randomaction = randrange(3)
                else:
                    randomaction = 0

            if randomaction == 0:
                self.action1.setChecked(True)
            elif randomaction == 1:
                self.action2.setChecked(True)
            elif randomaction == 2:
                self.action3.setChecked(True)
            elif randomaction == 3:
                self.action4.setChecked(True)
            elif randomaction == 4:
                self.action5.setChecked(True)
            elif randomaction == 5:
                self.action6.setChecked(True)
            else:
                self.action7.setChecked(True)
            self.result.setText("")

            return None

        self.randomhandspotbutton = QtWidgets.QPushButton(Dialog)
        self.randomhandspotbutton.setGeometry(QtCore.QRect(286, 198, 190, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.randomhandspotbutton.setFont(font)
        self.randomhandspotbutton.setObjectName("randomhandspotbutton")
        self.randomhandspotbutton.clicked.connect(lambda: randomhandspot(self))

        def randomhandspot(self):
            randomhand(self)
            randomspot(self)




        # CLEAR
        self.clearbutton = QtWidgets.QPushButton(Dialog)
        self.clearbutton.setGeometry(QtCore.QRect(398, 231, 79, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.clearbutton.setFont(font)
        self.clearbutton.setObjectName("clearbutton")
        self.clearbutton.clicked.connect(lambda: clearall(self))

        def clearall(self):
            # clear all inputs
            self.action1.setChecked(True)
            self.threehanded.setChecked(True)
            self.pos1.setChecked(True)
            players(self)
            position(self)
            self.stackslider.setValue(99)
            self.hand.setText("")
            self.result.setText("")
            return None
        clearall(self)

        def show_popup(self):
            msg = QtWidgets.QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("Spin and Go Preflop Charts/icon.png"))
            msg.setWindowTitle("Spin & Go Preflop Study Tool")
            msg.setText("ATTENTION:\n THIS TOOL IS EXCLUSIVELY FOR STUDYING PURPOSES.\n USE IN GAMES IS PROHIBITED.\n "
                        "YOU ARE LIKELY TO FACE REPERCUSSIONS IF YOU USE THIS TOOL DURING A GAME.")
            msg.setDefaultButton(QtWidgets.QMessageBox.Retry)
            #msg.setIcon(QtWidgets.QMessageBox.Information)
            x = msg.exec_()

        show_popup(self)
        # init
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Spin & Go Preflop Study Tool"))
        self.stacklabel.setText(_translate("Dialog", "Effective Stack:"))
        self.label.setText(_translate("Dialog", "0"))
        self.label_3.setText(_translate("Dialog", "5"))
        self.label_4.setText(_translate("Dialog", "10"))
        self.label_5.setText(_translate("Dialog", "15"))
        self.label_6.setText(_translate("Dialog", "20"))
        self.label_7.setText(_translate("Dialog", "25+"))
        self.handlabel.setText(_translate("Dialog", "Hand:"))
        self.lookupbutton.setText(_translate("Dialog", "Lookup"))
        self.clearbutton.setText(_translate("Dialog", "Clear All"))
        self.viewchart.setText(_translate("Dialog", "View Full Chart"))
        self.randomhandbutton.setText(_translate("Dialog", "Random Hand"))
        self.randomspotbutton.setText(_translate("Dialog", "Random Spot"))
        self.randomhandspotbutton.setText(_translate("Dialog", "Random Hand and Spot"))
        self.result.setText(_translate("Dialog", ""))
        self.PositionBox.setTitle(_translate("Dialog", "Position:"))
        self.pos1.setText(_translate("Dialog", "Big Blind"))
        self.pos2.setText(_translate("Dialog", "Small Blind"))
        self.pos3.setText(_translate("Dialog", "Button"))
        self.playersbox.setTitle(_translate("Dialog", "Players Left:"))
        self.twohanded.setText(_translate("Dialog", "2H"))
        self.threehanded.setText(_translate("Dialog", "3H"))
        self.actionbox.setTitle(_translate("Dialog", "Preflop Action:"))
        self.action1.setText(_translate("Dialog", "BU minraise"))
        self.action2.setText(_translate("Dialog", "BU shove"))
        self.action3.setText(_translate("Dialog", "BU limp"))
        self.action4.setText(_translate("Dialog", "SB minraise"))
        self.action5.setText(_translate("Dialog", "SB 2.5x"))
        self.action6.setText(_translate("Dialog", "SB shove"))
        self.action7.setText(_translate("Dialog", "SB limp"))
        self.bblabel.setText(_translate("Dialog", u"25+ BB"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    app.setQuitOnLastWindowClosed(True)
    sys.exit(app.exec_())
