# Form implementation generated from reading ui file 'envego cheat.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(679, 403)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("qrc/logo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 681, 401))
        font = QtGui.QFont()
        font.setKerning(True)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setStyleSheet("background-color: rgb(105,126,64);")
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.page)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 80, 681, 53))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.editSearchBar = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.editSearchBar.setMinimumSize(QtCore.QSize(401, 41))
        self.editSearchBar.setMaximumSize(QtCore.QSize(401, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.editSearchBar.setFont(font)
        self.editSearchBar.setAcceptDrops(True)
        self.editSearchBar.setAutoFillBackground(False)
        self.editSearchBar.setStyleSheet("QLineEdit{\n"
"  color: black;\n"
"  background-color: white;\n"
"  border: 0px solid;\n"
"  border-radius: 10px;\n"
"}")
        self.editSearchBar.setText("")
        self.editSearchBar.setMaxLength(1000)
        self.editSearchBar.setFrame(True)
        self.editSearchBar.setClearButtonEnabled(False)
        self.editSearchBar.setObjectName("editSearchBar")
        self.horizontalLayout_2.addWidget(self.editSearchBar)
        self.buttonSearch = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonSearch.sizePolicy().hasHeightForWidth())
        self.buttonSearch.setSizePolicy(sizePolicy)
        self.buttonSearch.setMinimumSize(QtCore.QSize(41, 41))
        self.buttonSearch.setMaximumSize(QtCore.QSize(41, 41))
        self.buttonSearch.setStyleSheet("border: 0px;")
        self.buttonSearch.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("qrc/search.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.buttonSearch.setIcon(icon1)
        self.buttonSearch.setIconSize(QtCore.QSize(36, 36))
        self.buttonSearch.setFlat(False)
        self.buttonSearch.setObjectName("buttonSearch")
        self.horizontalLayout_2.addWidget(self.buttonSearch)
        spacerItem1 = QtWidgets.QSpacerItem(120, 20, QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.page)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(180, 150, 331, 71))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.buttonRecipes = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.buttonRecipes.setMinimumSize(QtCore.QSize(91, 41))
        self.buttonRecipes.setMaximumSize(QtCore.QSize(91, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.buttonRecipes.setFont(font)
        self.buttonRecipes.setStyleSheet("QPushButton{\n"
"  color: white;\n"
"  background-color: blue;\n"
"  border: 0px solid;\n"
"  border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"  background-color: rgb(56, 56, 56);\n"
"}")
        self.buttonRecipes.setFlat(True)
        self.buttonRecipes.setObjectName("buttonRecipes")
        self.horizontalLayout_3.addWidget(self.buttonRecipes)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.buttonFood = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.buttonFood.setMinimumSize(QtCore.QSize(91, 41))
        self.buttonFood.setMaximumSize(QtCore.QSize(91, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.buttonFood.setFont(font)
        self.buttonFood.setStyleSheet("QPushButton{\n"
"  color: white;\n"
"  background-color: green;\n"
"  border: 0px solid;\n"
"  border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"  background-color: rgb(56, 56, 56);\n"
"}")
        self.buttonFood.setFlat(True)
        self.buttonFood.setObjectName("buttonFood")
        self.horizontalLayout_3.addWidget(self.buttonFood)
        self.labelImage = QtWidgets.QLabel(self.page)
        self.labelImage.setGeometry(QtCore.QRect(0, 240, 681, 161))
        self.labelImage.setText("")
        self.labelImage.setPixmap(QtGui.QPixmap("qrc/bìa.png"))
        self.labelImage.setScaledContents(True)
        self.labelImage.setObjectName("labelImage")
        self.scrollArea = QtWidgets.QScrollArea(self.page)
        self.scrollArea.setGeometry(QtCore.QRect(0, 220, 681, 161))
        self.scrollArea.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.scrollArea.setStyleSheet("border: 0px solid;")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 681, 161))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widgetSearch = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widgetSearch.setObjectName("widgetSearch")
        self.label = QtWidgets.QLabel(self.widgetSearch)
        self.label.setGeometry(QtCore.QRect(50, 10, 61, 71))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../qrc/search/apple.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.widgetSearch)
        self.label_5.setGeometry(QtCore.QRect(20, 100, 121, 31))
        self.label_5.setStyleSheet("font: 18pt;\n"
"color: black;")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.widgetSearch)
        self.widgetSearch_3 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widgetSearch_3.setObjectName("widgetSearch_3")
        self.label_2 = QtWidgets.QLabel(self.widgetSearch_3)
        self.label_2.setGeometry(QtCore.QRect(50, 20, 71, 71))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../qrc/search/banana.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(self.widgetSearch_3)
        self.label_6.setGeometry(QtCore.QRect(20, 100, 121, 31))
        self.label_6.setStyleSheet("font: 18pt;\n"
"color: black;")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.widgetSearch_3)
        self.widgetSearch_4 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widgetSearch_4.setObjectName("widgetSearch_4")
        self.label_3 = QtWidgets.QLabel(self.widgetSearch_4)
        self.label_3.setGeometry(QtCore.QRect(30, 10, 91, 81))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../qrc/search/Strawberry.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_7 = QtWidgets.QLabel(self.widgetSearch_4)
        self.label_7.setGeometry(QtCore.QRect(20, 100, 121, 31))
        self.label_7.setStyleSheet("font: 18pt;\n"
"color: black;")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.widgetSearch_4)
        self.widgetSearch_2 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widgetSearch_2.setObjectName("widgetSearch_2")
        self.label_4 = QtWidgets.QLabel(self.widgetSearch_2)
        self.label_4.setGeometry(QtCore.QRect(40, 10, 91, 81))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../qrc/search/avocado.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_8 = QtWidgets.QLabel(self.widgetSearch_2)
        self.label_8.setGeometry(QtCore.QRect(13, 100, 131, 31))
        self.label_8.setStyleSheet("font: 18pt;\n"
"color: black;")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.widgetSearch_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.page)
        self.scrollArea_2.setGeometry(QtCore.QRect(0, 220, 681, 161))
        self.scrollArea_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.scrollArea_2.setStyleSheet("border: 0px solid;")
        self.scrollArea_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.scrollArea_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 681, 161))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.widgetSearch_9 = QtWidgets.QWidget(self.scrollAreaWidgetContents_3)
        self.widgetSearch_9.setObjectName("widgetSearch_9")
        self.label_17 = QtWidgets.QLabel(self.widgetSearch_9)
        self.label_17.setGeometry(QtCore.QRect(50, 10, 61, 71))
        self.label_17.setText("")
        self.label_17.setPixmap(QtGui.QPixmap("../qrc/search/apple.png"))
        self.label_17.setScaledContents(True)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.widgetSearch_9)
        self.label_18.setGeometry(QtCore.QRect(20, 100, 121, 31))
        self.label_18.setStyleSheet("font: 18pt;\n"
"color: black;")
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_5.addWidget(self.widgetSearch_9)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)
        self.scrollArea_3 = QtWidgets.QScrollArea(self.page)
        self.scrollArea_3.setGeometry(QtCore.QRect(0, 220, 681, 161))
        self.scrollArea_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.scrollArea_3.setStyleSheet("border: 0px solid;")
        self.scrollArea_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.scrollArea_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea_3.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 681, 161))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_4)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.widgetSearch_11 = QtWidgets.QWidget(self.scrollAreaWidgetContents_4)
        self.widgetSearch_11.setObjectName("widgetSearch_11")
        self.label_21 = QtWidgets.QLabel(self.widgetSearch_11)
        self.label_21.setGeometry(QtCore.QRect(50, 20, 71, 71))
        self.label_21.setText("")
        self.label_21.setPixmap(QtGui.QPixmap("../qrc/search/banana.png"))
        self.label_21.setScaledContents(True)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.widgetSearch_11)
        self.label_22.setGeometry(QtCore.QRect(20, 100, 121, 31))
        self.label_22.setStyleSheet("font: 18pt;\n"
"color: black;")
        self.label_22.setObjectName("label_22")
        self.pushButton = QtWidgets.QPushButton(self.widgetSearch_11)
        self.pushButton.setGeometry(QtCore.QRect(10, 90, 41, 16))
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_6.addWidget(self.widgetSearch_11)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_4)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.page_2)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 661, 361))
        self.textBrowser.setObjectName("textBrowser")
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 679, 24))
        self.menubar.setObjectName("menubar")
        self.menuEnvego = QtWidgets.QMenu(self.menubar)
        self.menuEnvego.setObjectName("menuEnvego")
        MainWindow.setMenuBar(self.menubar)
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionFull_Recipes = QtGui.QAction(MainWindow)
        self.actionFull_Recipes.setObjectName("actionFull_Recipes")
        self.actionFull_Food = QtGui.QAction(MainWindow)
        self.actionFull_Food.setObjectName("actionFull_Food")
        self.actionHelp = QtGui.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionSetting = QtGui.QAction(MainWindow)
        self.actionSetting.setObjectName("actionSetting")
        self.actionclear = QtGui.QAction(MainWindow)
        self.actionclear.setObjectName("actionclear")
        self.menuEnvego.addAction(self.actionAbout)
        self.menuEnvego.addSeparator()
        self.menuEnvego.addAction(self.actionFull_Food)
        self.menuEnvego.addAction(self.actionFull_Recipes)
        self.menuEnvego.addSeparator()
        self.menuEnvego.addAction(self.actionHelp)
        self.menuEnvego.addAction(self.actionSetting)
        self.menubar.addAction(self.menuEnvego.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ENVEGO"))
        self.editSearchBar.setPlaceholderText(_translate("MainWindow", "Tìm kiếm"))
        self.buttonRecipes.setText(_translate("MainWindow", "Công Thức"))
        self.buttonFood.setText(_translate("MainWindow", "Thức Ăn"))
        self.label_5.setText(_translate("MainWindow", "Lượng calo: 52"))
        self.label_6.setText(_translate("MainWindow", "Lượng calo: 88"))
        self.label_7.setText(_translate("MainWindow", "Lượng calo: 32"))
        self.label_8.setText(_translate("MainWindow", "Lượng calo: 160"))
        self.label_18.setText(_translate("MainWindow", "Lượng calo: 52"))
        self.label_22.setText(_translate("MainWindow", "Lượng calo: 88"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">🥬1001 ĐIỀU NÊN BIẾT VỀ ENVEGO 🥬</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ENVEGO là một dự án nằm trong chuỗi hoạt động của cuộc thi &quot; Future Blue Innovation 2022 &quot; do mạng lưới HUB Network - Mạng lưới CLB Khởi nghiệp, Đổi mới Sáng tạo &amp; Chuyển đổi số Thủ đô tổ chức. </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Được thành lập bởi một nhóm các bạn học sinh trường THPT Cao Bá Quát- Gia Lâm, ENVEGO sở hữu cái tên ghép bởi các chữ cái đầu của mỗi từ khóa cốt lõi mà dự án hướng đến: Environment, Vegetarian, Go. Với sức trẻ và tinh thần nhiệt huyết, chúng mình mong rằng có thể thay đổi cách nhìn đối với một chế độ ăn uống mà phần đông mọi người cho rằng vô cùng nhàm chán và cảm thấy khó khăn để có thể gắn bó suốt quá trình lâu dài. Dự án không chỉ giúp mọi người hình thành thói quen ăn chay lành mạnh, đúng cách, hơn thế nữa còn mong muốn từ những thay đổi nhỏ đó có thể giúp bảo vệ môi trường từ hậu quả của quá trình chăn nuôi chưa được áp dụng công nghệ hiện đại, cũng như ủng hộ sự chuyển hướng của cách thức canh tác tại Việt Nam sang nông nghiệp sạch nhằm bảo vệ sức khỏe người tiêu dùng.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Vậy nên, nếu như bạn đang tập tành ăn chay mà không biết phải bắt đầu từ đâu. Hay bạn là người dày dặn kinh nghiệm, có mong muốn chia sẻ với mọi người những trải nghiệm trong quá trình đi tìm phương pháp, các công thức nấu nướng mới mẻ, thú vị thì ENVEGO là nơi dành cho bạn. Tại đây, mọi người có thể tìm hiểu nhiều hơn về kiến thức của việc ăn chay đúng cách, thoải mái chia sẻ câu chuyện của bản thân cũng như mang đến những thực đơn sáng tạo cho một bữa cơm ngon miệng, đầy đủ dinh dưỡng. Hãy cùng ENVEGO phát triển một cộng đồng thân thiện, lành mạnh, hiệu quả để cùng nhau bảo vệ môi trường và cả sức khỏe của mỗi cá nhân ngay thôi nào!</p></body></html>"))
        self.menuEnvego.setTitle(_translate("MainWindow", "Envego"))
        self.actionAbout.setText(_translate("MainWindow", "Về chúng tôi"))
        self.actionFull_Recipes.setText(_translate("MainWindow", "Danh sách công thức"))
        self.actionFull_Recipes.setShortcut(_translate("MainWindow", "Ctrl+U"))
        self.actionFull_Food.setText(_translate("MainWindow", "Danh sách thức ăn"))
        self.actionFull_Food.setShortcut(_translate("MainWindow", "Ctrl+T"))
        self.actionHelp.setText(_translate("MainWindow", "HDSD"))
        self.actionSetting.setText(_translate("MainWindow", "Cài đặt"))
        self.actionclear.setText(_translate("MainWindow", "clear"))
        self.actionclear.setToolTip(_translate("MainWindow", "Clear"))
        self.actionclear.setShortcut(_translate("MainWindow", "Ctrl+Backspace"))
