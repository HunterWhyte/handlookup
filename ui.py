# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'handlookup.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(487, 264)
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
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(218, 107, 55, 33))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
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
        self.horizontalSlider = QtWidgets.QSlider(Dialog)
        self.horizontalSlider.setGeometry(QtCore.QRect(310, 65, 160, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider.setTickInterval(4)
        self.horizontalSlider.setObjectName("horizontalSlider")
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
        self.lookupbutton = QtWidgets.QPushButton(Dialog)
        self.lookupbutton.setGeometry(QtCore.QRect(286, 111, 72, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lookupbutton.setFont(font)
        self.lookupbutton.setObjectName("lookupbutton")
        self.clearbutton = QtWidgets.QPushButton(Dialog)
        self.clearbutton.setGeometry(QtCore.QRect(398, 231, 79, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.clearbutton.setFont(font)
        self.clearbutton.setObjectName("clearbutton")
        self.lookupbutton_2 = QtWidgets.QPushButton(Dialog)
        self.lookupbutton_2.setGeometry(QtCore.QRect(360, 110, 116, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lookupbutton_2.setFont(font)
        self.lookupbutton_2.setObjectName("lookupbutton_2")
        self.line_7 = QtWidgets.QFrame(Dialog)
        self.line_7.setGeometry(QtCore.QRect(138, 182, 407, 21))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.randomhand = QtWidgets.QPushButton(Dialog)
        self.randomhand.setGeometry(QtCore.QRect(158, 199, 116, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.randomhand.setFont(font)
        self.randomhand.setObjectName("randomhand")
        self.randomspot = QtWidgets.QPushButton(Dialog)
        self.randomspot.setGeometry(QtCore.QRect(158, 230, 116, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.randomspot.setFont(font)
        self.randomspot.setObjectName("randomspot")
        self.randomhandspot = QtWidgets.QPushButton(Dialog)
        self.randomhandspot.setGeometry(QtCore.QRect(286, 198, 190, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.randomhandspot.setFont(font)
        self.randomhandspot.setObjectName("randomhandspot")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(168, 150, 303, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
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
        self.PositionBox = QtWidgets.QGroupBox(Dialog)
        self.PositionBox.setEnabled(True)
        self.PositionBox.setGeometry(QtCore.QRect(103, 4, 384, 56))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PositionBox.setFont(font)
        self.PositionBox.setObjectName("PositionBox")
        self.pos1 = QtWidgets.QRadioButton(self.PositionBox)
        self.pos1.setGeometry(QtCore.QRect(6, 28, 111, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pos1.setFont(font)
        self.pos1.setObjectName("pos1")
        self.pos3 = QtWidgets.QRadioButton(self.PositionBox)
        self.pos3.setGeometry(QtCore.QRect(246, 28, 111, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pos3.setFont(font)
        self.pos3.setObjectName("pos3")
        self.pos2 = QtWidgets.QRadioButton(self.PositionBox)
        self.pos2.setGeometry(QtCore.QRect(126, 28, 111, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pos2.setFont(font)
        self.pos2.setObjectName("pos2")
        self.playersbox = QtWidgets.QGroupBox(Dialog)
        self.playersbox.setGeometry(QtCore.QRect(-4, 4, 110, 56))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.playersbox.setFont(font)
        self.playersbox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.playersbox.setObjectName("playersbox")
        self.twohanded = QtWidgets.QRadioButton(self.playersbox)
        self.twohanded.setGeometry(QtCore.QRect(12, 28, 41, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.twohanded.setFont(font)
        self.twohanded.setObjectName("twohanded")
        self.threehanded = QtWidgets.QRadioButton(self.playersbox)
        self.threehanded.setGeometry(QtCore.QRect(60, 28, 42, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.threehanded.setFont(font)
        self.threehanded.setObjectName("threehanded")
        self.actionbox = QtWidgets.QGroupBox(Dialog)
        self.actionbox.setGeometry(QtCore.QRect(1, 62, 139, 204))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.actionbox.setFont(font)
        self.actionbox.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.actionbox.setObjectName("actionbox")
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
        self.action2 = QtWidgets.QRadioButton(self.actionbox)
        self.action2.setGeometry(QtCore.QRect(10, 48, 106, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.action2.setFont(font)
        self.action2.setObjectName("action2")
        self.action1 = QtWidgets.QRadioButton(self.actionbox)
        self.action1.setGeometry(QtCore.QRect(10, 24, 106, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.action1.setFont(font)
        self.action1.setObjectName("action1")
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
        self.bblabel = QtWidgets.QLabel(Dialog)
        self.bblabel.setGeometry(QtCore.QRect(252, 62, 56, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bblabel.setFont(font)
        self.bblabel.setObjectName("bblabel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
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
        self.lookupbutton_2.setText(_translate("Dialog", "View Full Chart"))
        self.randomhand.setText(_translate("Dialog", "Random Hand"))
        self.randomspot.setText(_translate("Dialog", "Random Spot"))
        self.randomhandspot.setText(_translate("Dialog", "Random Hand and Spot"))
        self.label_2.setText(_translate("Dialog", "TextLabel"))
        self.PositionBox.setTitle(_translate("Dialog", "Position:"))
        self.pos1.setText(_translate("Dialog", "RadioButton"))
        self.pos3.setText(_translate("Dialog", "RadioButton"))
        self.pos2.setText(_translate("Dialog", "RadioButton"))
        self.playersbox.setTitle(_translate("Dialog", "Players Left:"))
        self.twohanded.setText(_translate("Dialog", "2H"))
        self.threehanded.setText(_translate("Dialog", "3H"))
        self.actionbox.setTitle(_translate("Dialog", "Preflop Action:"))
        self.action3.setText(_translate("Dialog", "RadioButton"))
        self.action4.setText(_translate("Dialog", "RadioButton"))
        self.action2.setText(_translate("Dialog", "RadioButton"))
        self.action1.setText(_translate("Dialog", "RadioButton"))
        self.action5.setText(_translate("Dialog", "RadioButton"))
        self.action6.setText(_translate("Dialog", "RadioButton"))
        self.action7.setText(_translate("Dialog", "RadioButton"))
        self.bblabel.setText(_translate("Dialog", "25+ BB"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
