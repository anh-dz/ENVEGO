# Form implementation generated from reading ui file '/Users/minkalexvina/Desktop/Project/Envego/App/view/envego cheat copy.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets

class BANANA(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__()
        self.setObjectName("self")
        self.resize(679, 403)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/Users/minkalexvina/Desktop/Project/Envego/App/view/qrc/logo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.setWindowIcon(icon)
        self.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(self)
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
        self.label_21 = QtWidgets.QLabel(self.page)
        self.label_21.setGeometry(QtCore.QRect(40, 40, 111, 111))
        self.label_21.setText("")
        self.label_21.setPixmap(QtGui.QPixmap("/Users/minkalexvina/Desktop/Project/Envego/App/view/../qrc/search/banana.png"))
        self.label_21.setScaledContents(True)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.page)
        self.label_22.setGeometry(QtCore.QRect(20, 220, 141, 31))
        self.label_22.setStyleSheet("font: 22pt;\n"
"color: black;")
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.page)
        self.label_23.setGeometry(QtCore.QRect(50, 170, 91, 41))
        self.label_23.setStyleSheet("font: 26pt;\n"
"color: black;\n"
"font: bold;")
        self.label_23.setObjectName("label_23")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.page)
        self.textBrowser_2.setGeometry(QtCore.QRect(180, 30, 481, 331))
        self.textBrowser_2.setStyleSheet("background-color: rgb(242,242,242);\n"
"color: black;\n"
"border-radius: 10px;")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.page_2)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 661, 361))
        self.textBrowser.setObjectName("textBrowser")
        self.stackedWidget.addWidget(self.page_2)
        self.retranslateUi(self)

    def retranslateUi(self, another=None):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "ENVEGO"))
        self.label_22.setText(_translate("self", "L?????ng calo: 88"))
        self.label_23.setText(_translate("self", "CHU???I"))
        self.textBrowser_2.setHtml(_translate("self", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:24pt; font-weight:600; color:#000000; background-color:transparent;\">Trong 100g chu???i cung c???p:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:18pt; color:#000000; background-color:transparent;\">- L?????ng Calo: 88, ch??nh x??c 88.7 calo</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:18pt; color:#000000; background-color:transparent;\">- Protein: 1.1 gram.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:18pt; color:#000000; background-color:transparent;\">- Ch???t x??: 2.6 gram.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:18pt; color:#000000; background-color:transparent;\">- Carbohydrate: 22.8 gram.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:18pt; color:#000000; background-color:transparent;\">- Ch???t b??o: 0.3 gram.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:18pt; color:#000000; background-color:transparent;\">- ???????ng: 12.2 gram.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:18pt; color:#000000; background-color:transparent;\">- Ch???t kh??c: Kali, vitamin B6, vitamin C, ch???t ch???ng oxy h??a v?? c??c phytonutrients.</span></p></body></html>"))
        self.textBrowser.setHtml(_translate("self", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">????1001 ??I???U N??N BI???T V??? ENVEGO ????</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ENVEGO l?? m???t d??? ??n n???m trong chu???i ho???t ?????ng c???a cu???c thi &quot; Future Blue Innovation 2022 &quot; do m???ng l?????i HUB Network - M???ng l?????i CLB Kh???i nghi???p, ?????i m???i S??ng t???o &amp; Chuy???n ?????i s??? Th??? ???? t??? ch???c. </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">???????c th??nh l???p b???i m???t nh??m c??c b???n h???c sinh tr?????ng THPT Cao B?? Qu??t- Gia L??m, ENVEGO s??? h???u c??i t??n gh??p b???i c??c ch??? c??i ?????u c???a m???i t??? kh??a c???t l??i m?? d??? ??n h?????ng ?????n: Environment, Vegetarian, Go. V???i s???c tr??? v?? tinh th???n nhi???t huy???t, ch??ng m??nh mong r???ng c?? th??? thay ?????i c??ch nh??n ?????i v???i m???t ch??? ????? ??n u???ng m?? ph???n ????ng m???i ng?????i cho r???ng v?? c??ng nh??m ch??n v?? c???m th???y kh?? kh??n ????? c?? th??? g???n b?? su???t qu?? tr??nh l??u d??i. D??? ??n kh??ng ch??? gi??p m???i ng?????i h??nh th??nh th??i quen ??n chay l??nh m???nh, ????ng c??ch, h??n th??? n???a c??n mong mu???n t??? nh???ng thay ?????i nh??? ???? c?? th??? gi??p b???o v??? m??i tr?????ng t??? h???u qu??? c???a qu?? tr??nh ch??n nu??i ch??a ???????c ??p d???ng c??ng ngh??? hi???n ?????i, c??ng nh?? ???ng h??? s??? chuy???n h?????ng c???a c??ch th???c canh t??c t???i Vi???t Nam sang n??ng nghi???p s???ch nh???m b???o v??? s???c kh???e ng?????i ti??u d??ng.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">V???y n??n, n???u nh?? b???n ??ang t???p t??nh ??n chay m?? kh??ng bi???t ph???i b???t ?????u t??? ????u. Hay b???n l?? ng?????i d??y d???n kinh nghi???m, c?? mong mu???n chia s??? v???i m???i ng?????i nh???ng tr???i nghi???m trong qu?? tr??nh ??i t??m ph????ng ph??p, c??c c??ng th???c n???u n?????ng m???i m???, th?? v??? th?? ENVEGO l?? n??i d??nh cho b???n. T???i ????y, m???i ng?????i c?? th??? t??m hi???u nhi???u h??n v??? ki???n th???c c???a vi???c ??n chay ????ng c??ch, tho???i m??i chia s??? c??u chuy???n c???a b???n th??n c??ng nh?? mang ?????n nh???ng th???c ????n s??ng t???o cho m???t b???a c??m ngon mi???ng, ?????y ????? dinh d?????ng. H??y c??ng ENVEGO ph??t tri???n m???t c???ng ?????ng th??n thi???n, l??nh m???nh, hi???u qu??? ????? c??ng nhau b???o v??? m??i tr?????ng v?? c??? s???c kh???e c???a m???i c?? nh??n ngay th??i n??o!</p></body></html>"))
