# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\mitgobla\Documents\Python\Team Lightning\FLASH\builder\builder-window.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph.opengl import GLViewWidget
from pyqtgraph import mkColor

class CustomGL(GLViewWidget):
    keyPressed = QtCore.pyqtSignal(int)
    mousePressed = QtCore.pyqtSignal(object)

    def __init__(self, parent = None):
        super(CustomGL, self).__init__(parent)

    def keyPressEvent(self, event):
        super(CustomGL, self).keyPressEvent(event)
        self.keyPressed.emit(event.key())

    def mousePressEvent(self, event):
        super(CustomGL, self).mousePressEvent(event)
        self.mousePressed.emit(event)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1030, 689)
        MainWindow.setMinimumSize(QtCore.QSize(1030, 689))
        MainWindow.setMaximumSize(QtCore.QSize(1030, 689))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo/flash-software-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget.setObjectName("centralwidget")
        self.toolBox = QtWidgets.QToolBox(self.centralwidget)
        self.toolBox.setGeometry(QtCore.QRect(610, 0, 421, 591))
        self.toolBox.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.toolBox.setObjectName("toolBox")
        self.page_fileproperties = QtWidgets.QWidget()
        self.page_fileproperties.setGeometry(QtCore.QRect(0, 0, 421, 537))
        self.page_fileproperties.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.page_fileproperties.setObjectName("page_fileproperties")
        self.label = QtWidgets.QLabel(self.page_fileproperties)
        self.label.setGeometry(QtCore.QRect(10, 0, 101, 31))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.lcdNumber_instructions = QtWidgets.QLCDNumber(self.page_fileproperties)
        self.lcdNumber_instructions.setGeometry(QtCore.QRect(10, 80, 101, 31))
        self.lcdNumber_instructions.setObjectName("lcdNumber_instructions")
        self.lcdNumber_bricks = QtWidgets.QLCDNumber(self.page_fileproperties)
        self.lcdNumber_bricks.setGeometry(QtCore.QRect(10, 40, 101, 31))
        self.lcdNumber_bricks.setObjectName("lcdNumber_bricks")
        self.label_2 = QtWidgets.QLabel(self.page_fileproperties)
        self.label_2.setGeometry(QtCore.QRect(120, 40, 291, 31))
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.page_fileproperties)
        self.label_3.setGeometry(QtCore.QRect(120, 80, 291, 31))
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.pushButton_printfile = QtWidgets.QPushButton(self.page_fileproperties)
        self.pushButton_printfile.setEnabled(True)
        self.pushButton_printfile.setGeometry(QtCore.QRect(10, 470, 401, 31))
        self.pushButton_printfile.setToolTip("Generate model data and save the file")
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButton_printfile.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_printfile.setFont(font)
        self.pushButton_printfile.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.pushButton_printfile.setObjectName("pushButton_printfile")
        self.groupBox_filedescription = QtWidgets.QGroupBox(self.page_fileproperties)
        self.groupBox_filedescription.setGeometry(QtCore.QRect(10, 120, 401, 121))
        self.groupBox_filedescription.setObjectName("groupBox_filedescription")
        self.plainTextEdit_filedescription = QtWidgets.QPlainTextEdit(self.groupBox_filedescription)
        self.plainTextEdit_filedescription.setGeometry(QtCore.QRect(10, 20, 381, 91))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setItalic(True)
        self.plainTextEdit_filedescription.setFont(font)
        self.plainTextEdit_filedescription.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.plainTextEdit_filedescription.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_filedescription.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.plainTextEdit_filedescription.setObjectName("plainTextEdit_filedescription")
        self.lineEdit_filename = QtWidgets.QLineEdit(self.page_fileproperties)
        self.lineEdit_filename.setGeometry(QtCore.QRect(120, 0, 291, 31))
        self.lineEdit_filename.setMaxLength(36)
        self.lineEdit_filename.setObjectName("lineEdit_filename")
        self.toolBox.addItem(self.page_fileproperties, "")
        self.page_builder = QtWidgets.QWidget()
        self.page_builder.setEnabled(True)
        self.page_builder.setGeometry(QtCore.QRect(0, 0, 421, 537))
        self.page_builder.setObjectName("page_builder")
        self.groupBox = QtWidgets.QGroupBox(self.page_builder)
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 401, 171))
        self.groupBox.setObjectName("groupBox")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setEnabled(True)
        self.label_10.setGeometry(QtCore.QRect(30, 150, 31, 16))
        self.label_10.setStyleSheet("background-color: transparent;")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.pushButton_down_y = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_down_y.setEnabled(True)
        self.pushButton_down_y.setGeometry(QtCore.QRect(50, 80, 31, 31))
        self.pushButton_down_y.setText("")
        self.pushButton_down_y.setToolTip("Move frame -1 stud on the Y-Axis. Key: S")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("resources/down-icon-16.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_down_y.setIcon(icon1)
        self.pushButton_down_y.setObjectName("pushButton_down_y")
        self.pushButton_delete = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_delete.setEnabled(True)
        self.pushButton_delete.setGeometry(QtCore.QRect(90, 40, 31, 31))
        self.pushButton_delete.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("resources/delete-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_delete.setIcon(icon2)
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.pushButton_delete.setToolTip("Delete brick. Key: X")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setEnabled(True)
        self.label_11.setGeometry(QtCore.QRect(130, 40, 41, 31))
        self.label_11.setStyleSheet("background-color: transparent;")
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.pushButton_down_z = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_down_z.setEnabled(True)
        self.pushButton_down_z.setGeometry(QtCore.QRect(10, 80, 31, 31))
        self.pushButton_down_z.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.pushButton_down_z.setText("")
        self.pushButton_down_z.setIcon(icon1)
        self.pushButton_down_z.setObjectName("pushButton_down_z")
        self.pushButton_down_z.setToolTip("Move frame -1 brick on the Z-Axis. Key: E")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setEnabled(True)
        self.label_8.setGeometry(QtCore.QRect(10, 20, 31, 16))
        self.label_8.setStyleSheet("background-color: transparent;")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.pushButton_up_z = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_up_z.setEnabled(True)
        self.pushButton_up_z.setGeometry(QtCore.QRect(10, 40, 31, 31))
        self.pushButton_up_z.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.pushButton_up_z.setText("")
        self.pushButton_up_z.setToolTip("Move frame 1 brick on the Z-Axis. Key: Q")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("resources/up-icon-16.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_up_z.setIcon(icon3)
        self.pushButton_up_z.setObjectName("pushButton_up_z")
        self.pushButton_place = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_place.setEnabled(True)
        self.pushButton_place.setGeometry(QtCore.QRect(90, 80, 31, 31))
        self.pushButton_place.setText("")
        self.pushButton_place.setToolTip("Place brick of selected colour. Key: Spacebar")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("resources/place-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_place.setIcon(icon4)
        self.pushButton_place.setObjectName("pushButton_place")
        self.pushButton_left_x = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_left_x.setEnabled(True)
        self.pushButton_left_x.setGeometry(QtCore.QRect(10, 120, 31, 31))
        self.pushButton_left_x.setText("")
        self.pushButton_left_x.setToolTip("Move frame -1 stud on the X-Axis. Key: A")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("resources/left-icon-16.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_left_x.setIcon(icon5)
        self.pushButton_left_x.setObjectName("pushButton_left_x")
        self.pushButton_up_y = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_up_y.setEnabled(True)
        self.pushButton_up_y.setGeometry(QtCore.QRect(50, 40, 31, 31))
        self.pushButton_up_y.setText("")
        self.pushButton_up_y.setIcon(icon3)
        self.pushButton_up_y.setObjectName("pushButton_up_y")
        self.pushButton_up_y.setToolTip("Move frame 1 stud on the Y-Axis. Key: W")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setEnabled(True)
        self.label_12.setGeometry(QtCore.QRect(130, 80, 41, 31))
        self.label_12.setStyleSheet("background-color: transparent;")
        self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setEnabled(True)
        self.label_9.setGeometry(QtCore.QRect(50, 20, 31, 16))
        self.label_9.setStyleSheet("background-color: transparent;")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.pushButton_right_x = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_right_x.setEnabled(True)
        self.pushButton_right_x.setGeometry(QtCore.QRect(50, 120, 31, 31))
        self.pushButton_right_x.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("resources/right-icon-16.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_right_x.setIcon(icon6)
        self.pushButton_right_x.setObjectName("pushButton_right_x")
        self.pushButton_right_x.setToolTip("Move frame 1 stud on the X-Axis. Key: D")
        self.label_colour_selected = QtWidgets.QLabel(self.groupBox)
        self.label_colour_selected.setGeometry(QtCore.QRect(90, 123, 231, 21))
        self.label_colour_selected.setObjectName("label_colour_selected")
        self.pushButton_move_right_x = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_move_right_x.setEnabled(True)
        self.pushButton_move_right_x.setGeometry(QtCore.QRect(360, 120, 31, 31))
        self.pushButton_move_right_x.setText("")
        self.pushButton_move_right_x.setIcon(icon6)
        self.pushButton_move_right_x.setObjectName("pushButton_move_right_x")
        self.pushButton_move_right_x.setToolTip("Move entire model 1 stud on the X-Axis")
        self.pushButton_move_left_x = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_move_left_x.setEnabled(True)
        self.pushButton_move_left_x.setGeometry(QtCore.QRect(320, 120, 31, 31))
        self.pushButton_move_left_x.setText("")
        self.pushButton_move_left_x.setIcon(icon5)
        self.pushButton_move_left_x.setObjectName("pushButton_move_left_x")
        self.pushButton_move_left_x.setToolTip("Move entire model -1 stud on the X-Axis")
        self.pushButton_move_up_z = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_move_up_z.setEnabled(True)
        self.pushButton_move_up_z.setGeometry(QtCore.QRect(320, 40, 31, 31))
        self.pushButton_move_up_z.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.pushButton_move_up_z.setText("")
        self.pushButton_move_up_z.setIcon(icon3)
        self.pushButton_move_up_z.setObjectName("pushButton_move_up_z")
        self.pushButton_move_up_z.setToolTip("Move entire model 1 brick on the Z-Axis")
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setEnabled(True)
        self.label_13.setGeometry(QtCore.QRect(340, 150, 31, 16))
        self.label_13.setStyleSheet("background-color: transparent;")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.pushButton_move_up_y = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_move_up_y.setEnabled(True)
        self.pushButton_move_up_y.setGeometry(QtCore.QRect(360, 40, 31, 31))
        self.pushButton_move_up_y.setText("")
        self.pushButton_move_up_y.setIcon(icon3)
        self.pushButton_move_up_y.setObjectName("pushButton_move_up_y")
        self.pushButton_move_up_y.setToolTip("Move entire model 1 stud on the Y-Axis")
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setEnabled(True)
        self.label_14.setGeometry(QtCore.QRect(360, 20, 31, 16))
        self.label_14.setStyleSheet("background-color: transparent;")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        self.label_15.setEnabled(True)
        self.label_15.setGeometry(QtCore.QRect(320, 20, 31, 16))
        self.label_15.setStyleSheet("background-color: transparent;")
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.pushButton_move_down_z = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_move_down_z.setEnabled(True)
        self.pushButton_move_down_z.setGeometry(QtCore.QRect(320, 80, 31, 31))
        self.pushButton_move_down_z.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.pushButton_move_down_z.setText("")
        self.pushButton_move_down_z.setIcon(icon1)
        self.pushButton_move_down_z.setObjectName("pushButton_move_down_z")
        self.pushButton_move_down_z.setToolTip("Move entire model -1 brick on the Z-Axis")
        self.pushButton_move_down_y = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_move_down_y.setEnabled(True)
        self.pushButton_move_down_y.setGeometry(QtCore.QRect(360, 80, 31, 31))
        self.pushButton_move_down_y.setText("")
        self.pushButton_move_down_y.setIcon(icon1)
        self.pushButton_move_down_y.setObjectName("pushButton_move_down_y")
        self.pushButton_move_down_y.setToolTip("Move entire model -1 stud on the Y-Axis")
        self.label_16 = QtWidgets.QLabel(self.groupBox)
        self.label_16.setEnabled(True)
        self.label_16.setGeometry(QtCore.QRect(250, 80, 61, 31))
        self.label_16.setStyleSheet("background-color: transparent;")
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.groupBox_2 = QtWidgets.QGroupBox(self.page_builder)
        self.groupBox_2.setEnabled(True)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 180, 401, 81))
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_red_brick = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_red_brick.setEnabled(True)
        self.pushButton_red_brick.setCheckable(True)
        self.pushButton_red_brick.setChecked(True)
        self.pushButton_red_brick.setGeometry(QtCore.QRect(10, 20, 51, 51))
        self.pushButton_red_brick.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("resources/red-brick.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_red_brick.setIcon(icon7)
        self.pushButton_red_brick.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_red_brick.setObjectName("pushButton_red_brick")
        self.pushButton_red_brick.setToolTip("Red brick. Key: 1")
        self.pushButton_blue_brick = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_blue_brick.setEnabled(True)
        self.pushButton_blue_brick.setCheckable(True)
        self.pushButton_blue_brick.setGeometry(QtCore.QRect(70, 20, 51, 51))
        self.pushButton_blue_brick.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("resources/blue-brick.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_blue_brick.setIcon(icon8)
        self.pushButton_blue_brick.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_blue_brick.setToolTip("Blue brick. Key: 2")
        self.pushButton_blue_brick.setObjectName("pushButton_blue_brick")
        self.pushButton_yellow_brick = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_yellow_brick.setEnabled(True)
        self.pushButton_yellow_brick.setCheckable(True)
        self.pushButton_yellow_brick.setGeometry(QtCore.QRect(130, 20, 51, 51))
        self.pushButton_yellow_brick.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("resources/yellow-brick.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_yellow_brick.setIcon(icon9)
        self.pushButton_yellow_brick.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_yellow_brick.setObjectName("pushButton_yellow_brick")
        self.pushButton_yellow_brick.setToolTip("Yellow brick. Key: 3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.page_builder)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 270, 401, 101))
        self.groupBox_3.setObjectName("groupBox_3")
        self.spinBox_grid_x = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_grid_x.setGeometry(QtCore.QRect(10, 30, 71, 22))
        self.spinBox_grid_x.setMinimum(1)
        self.spinBox_grid_x.setMaximum(50)
        self.spinBox_grid_x.setProperty("value", 10)
        self.spinBox_grid_x.setObjectName("spinBox_grid_x")
        self.spinBox_grid_y = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_grid_y.setGeometry(QtCore.QRect(10, 60, 71, 22))
        self.spinBox_grid_y.setMinimum(1)
        self.spinBox_grid_y.setMaximum(50)
        self.spinBox_grid_y.setProperty("value", 10)
        self.spinBox_grid_y.setObjectName("spinBox_grid_y")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(90, 30, 291, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(90, 60, 291, 21))
        self.label_5.setObjectName("label_5")
        self.toolBox.addItem(self.page_builder, "")
        self.label_status = QtWidgets.QLabel(self.centralwidget)
        self.label_status.setGeometry(QtCore.QRect(620, 600, 401, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_status.setFont(font)
        self.label_status.setObjectName("label_status")
        self.label_printtime = QtWidgets.QLabel(self.centralwidget)
        self.label_printtime.setGeometry(QtCore.QRect(620, 641, 401, 20))
        self.label_printtime.setObjectName("label_printtime")
        self.label_secondstatus = QtWidgets.QLabel(self.centralwidget)
        self.label_secondstatus.setGeometry(QtCore.QRect(620, 621, 401, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_secondstatus.setFont(font)
        self.label_secondstatus.setObjectName("label_secondstatus")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 611, 671))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        #GL WIDGET START
        self.layout_GL = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.layout_GL.setContentsMargins(0, 0, 0, 0)
        self.layout_GL.setObjectName("layout_GL")
        #self.openGL_preview = GLViewWidget(self.gridLayoutWidget)
        self.openGL_preview = CustomGL(self.gridLayoutWidget)
        #self.openGL_preview.setMouseTracking(True)
        #self.openGL_preview.setFocusPolicy(QtCore.Qt.NoFocus)
        self.openGL_preview.setStyleSheet("")
        self.openGL_preview.setBackgroundColor(mkColor(155, 155, 155, 0))
        self.openGL_preview.setObjectName("openGL_preview")
        self.layout_GL.addWidget(self.openGL_preview, 0, 0, 1, 1)
        #self.openGL_preview = QtWidgets.QOpenGLWidget(self.centralwidget)
        #GL WIDGET END
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(612, 590, 421, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1030, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpenWith = QtWidgets.QAction(MainWindow)
        self.actionOpenWith.setObjectName("actionOpen")
        self.actionConvert = QtWidgets.QAction(MainWindow)
        self.actionConvert.setObjectName("actionConvert")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")

        self.actionResetCamera = QtWidgets.QAction(MainWindow)
        self.actionResetCamera.setObjectName("actionResetCamera")
        self.actionToggleDarkMode = QtWidgets.QAction(MainWindow)
        self.actionResetPlacer = QtWidgets.QAction(MainWindow)
        self.actionResetPlacer.setObjectName("actionResetPlacer")
        self.actionToggleDarkMode.setCheckable(True)
        self.actionToggleDarkMode.setObjectName("actionToggleDarkMode")


        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionOpenWith)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)

        self.menuView.addAction(self.actionResetCamera)
        self.menuView.addAction(self.actionResetPlacer)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionToggleDarkMode)

        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Team Lightning FLASH Software"))
        self.label.setText(_translate("MainWindow", "File Name"))
        self.label_2.setText(_translate("MainWindow", "Number of Bricks"))
        self.label_3.setText(_translate("MainWindow", "Estimated number of instructions"))
        self.pushButton_printfile.setText(_translate("MainWindow", "Generate File"))
        self.groupBox_filedescription.setTitle(_translate("MainWindow", "File Description"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_fileproperties), _translate("MainWindow", "File Properties"))
        self.groupBox.setTitle(_translate("MainWindow", "Controls"))
        self.label_10.setText(_translate("MainWindow", "X"))
        self.label_11.setText(_translate("MainWindow", "Delete"))
        self.label_8.setText(_translate("MainWindow", "Z"))
        self.label_12.setText(_translate("MainWindow", "Place"))
        self.label_9.setText(_translate("MainWindow", "Y"))
        self.label_colour_selected.setText(_translate("MainWindow", "Selected Colour:"))
        self.label_13.setText(_translate("MainWindow", "X"))
        self.label_14.setText(_translate("MainWindow", "Y"))
        self.label_15.setText(_translate("MainWindow", "Z"))
        self.label_16.setText(_translate("MainWindow", "Move Model"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Bricks"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Grid Properties"))
        self.label_4.setText(_translate("MainWindow", "Grid X-Axis (bricks)"))
        self.label_5.setText(_translate("MainWindow", "Grid Y-Axis (bricks)"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_builder), _translate("MainWindow", "Builder"))
        self.label_status.setText(_translate("MainWindow", "Status Message"))
        self.label_printtime.setText(_translate("MainWindow", "Estimated Print Time: N/A seconds"))
        self.label_secondstatus.setText(_translate("MainWindow", "Secondary Status Message"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuAbout.setTitle(_translate("MainWindow", "Help"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionOpenWith.setText(_translate("MainWindow", "Open With"))
        self.actionConvert.setText(_translate("MainWindow", "Convert"))
        self.actionResetCamera.setText(_translate("MainWindow", "Reset Camera"))
        self.actionResetPlacer.setText(_translate("MainWindow", "Reset Placer"))
        self.actionToggleDarkMode.setText(_translate("MainWindow", "Dark Mode"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))