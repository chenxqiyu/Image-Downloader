# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 718)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet("QGroupBox{border:1px ridge gray;margin-top: 1ex;} QGroupBox::title{subcontrol-origin: margin;subcontrol-position:top center;padding:0 3px;}")
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_2.setContentsMargins(-1, -1, 30, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_time_elapsed = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(12)
        self.label_time_elapsed.setFont(font)
        self.label_time_elapsed.setObjectName("label_time_elapsed")
        self.gridLayout_2.addWidget(self.label_time_elapsed, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.progressBar_total = QtWidgets.QProgressBar(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar_total.sizePolicy().hasHeightForWidth())
        self.progressBar_total.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(12)
        self.progressBar_total.setFont(font)
        self.progressBar_total.setStyleSheet("")
        self.progressBar_total.setMaximum(1000)
        self.progressBar_total.setProperty("value", 0)
        self.progressBar_total.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar_total.setFormat("")
        self.progressBar_total.setObjectName("progressBar_total")
        self.gridLayout_2.addWidget(self.progressBar_total, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.progressBar_current = QtWidgets.QProgressBar(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar_current.sizePolicy().hasHeightForWidth())
        self.progressBar_current.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(12)
        self.progressBar_current.setFont(font)
        self.progressBar_current.setStyleSheet("/*\n"
"QProgressBar {\n"
"    border: 2px solid gray;\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: rgba(0, 200, 0);\n"
"    width: 1px;\n"
"}*/")
        self.progressBar_current.setMaximum(1000)
        self.progressBar_current.setProperty("value", 0)
        self.progressBar_current.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar_current.setFormat("")
        self.progressBar_current.setObjectName("progressBar_current")
        self.gridLayout_2.addWidget(self.progressBar_current, 2, 1, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 3)
        self.gridLayout_3.addWidget(self.groupBox_3, 1, 0, 1, 2)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("QGroupBox{border:1px ridge gray;margin-top: 1ex;} QGroupBox::title{subcontrol-origin: margin;subcontrol-position:top center;padding:0 3px;}")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setContentsMargins(30, 30, 30, 30)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        #启动按钮
        self.pushButton_start = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_start.sizePolicy().hasHeightForWidth())
        self.pushButton_start.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_start.setFont(font)
        self.pushButton_start.setObjectName("pushButton_start")
        self.verticalLayout_2.addWidget(self.pushButton_start)


        #取消按钮
        self.pushButton_cancel = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_cancel.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_cancel.sizePolicy().hasHeightForWidth())
        self.pushButton_cancel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_cancel.setFont(font)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.verticalLayout_2.addWidget(self.pushButton_cancel)

        #打开文件夹按钮
        self.pushButton_open = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_open.sizePolicy().hasHeightForWidth())
        self.pushButton_open.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_open.setFont(font)
        self.pushButton_open.setObjectName("pushButton_open")
        self.verticalLayout_2.addWidget(self.pushButton_open)



        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 1)
        self.gridLayout_3.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.groupBox_config = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_config.sizePolicy().hasHeightForWidth())
        self.groupBox_config.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_config.setFont(font)
        self.groupBox_config.setStyleSheet("QGroupBox{border:1px ridge gray;margin-top: 1ex;} QGroupBox::title{subcontrol-origin: margin;subcontrol-position:top center;padding:0 3px;}")
        self.groupBox_config.setFlat(False)
        self.groupBox_config.setCheckable(False)
        self.groupBox_config.setObjectName("groupBox_config")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_config)
        self.verticalLayout.setContentsMargins(20, -1, 20, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_engine = QtWidgets.QWidget(self.groupBox_config)
        self.widget_engine.setObjectName("widget_engine")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_engine)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_google = QtWidgets.QRadioButton(self.widget_engine)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_google.setFont(font)
        self.radioButton_google.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.radioButton_google.setChecked(True)
        self.radioButton_google.setObjectName("radioButton_google")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.radioButton_google)
        self.horizontalLayout.addWidget(self.radioButton_google)
        self.radioButton_bing = QtWidgets.QRadioButton(self.widget_engine)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_bing.setFont(font)
        self.radioButton_bing.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.radioButton_bing.setObjectName("radioButton_bing")
        self.buttonGroup.addButton(self.radioButton_bing)
        self.horizontalLayout.addWidget(self.radioButton_bing)
        self.radioButton_baidu = QtWidgets.QRadioButton(self.widget_engine)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_baidu.setFont(font)
        self.radioButton_baidu.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.radioButton_baidu.setObjectName("radioButton_baidu")
        self.buttonGroup.addButton(self.radioButton_baidu)
        self.horizontalLayout.addWidget(self.radioButton_baidu)
        self.verticalLayout.addWidget(self.widget_engine)
        self.widget_driver = QtWidgets.QWidget(self.groupBox_config)
        self.widget_driver.setObjectName("widget_driver")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_driver)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.radioButton_chrome_headless = QtWidgets.QRadioButton(self.widget_driver)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_chrome_headless.setFont(font)
        self.radioButton_chrome_headless.setChecked(True)
        self.radioButton_chrome_headless.setObjectName("radioButton_chrome_headless")
        self.horizontalLayout_6.addWidget(self.radioButton_chrome_headless)
        self.radioButton_chrome = QtWidgets.QRadioButton(self.widget_driver)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_chrome.setFont(font)
        self.radioButton_chrome.setObjectName("radioButton_chrome")
        self.horizontalLayout_6.addWidget(self.radioButton_chrome)
        self.radioButton_phantomjs = QtWidgets.QRadioButton(self.widget_driver)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_phantomjs.setFont(font)
        self.radioButton_phantomjs.setObjectName("radioButton_phantomjs")
        self.horizontalLayout_6.addWidget(self.radioButton_phantomjs)
        self.verticalLayout.addWidget(self.widget_driver)
        self.widget_keywords = QtWidgets.QWidget(self.groupBox_config)
        self.widget_keywords.setObjectName("widget_keywords")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_keywords)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget_keywords)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_keywords = QtWidgets.QLineEdit(self.widget_keywords)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_keywords.setFont(font)
        self.lineEdit_keywords.setWhatsThis("")
        self.lineEdit_keywords.setInputMask("")
        self.lineEdit_keywords.setObjectName("lineEdit_keywords")
        self.gridLayout.addWidget(self.lineEdit_keywords, 0, 1, 1, 2)
        self.checkBox_from_file = QtWidgets.QCheckBox(self.widget_keywords)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_from_file.sizePolicy().hasHeightForWidth())
        self.checkBox_from_file.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(False)
        self.checkBox_from_file.setFont(font)
        self.checkBox_from_file.setObjectName("checkBox_from_file")
        self.gridLayout.addWidget(self.checkBox_from_file, 1, 0, 1, 1)
        self.lineEdit_path2file = QtWidgets.QLineEdit(self.widget_keywords)
        self.lineEdit_path2file.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_path2file.setFont(font)
        self.lineEdit_path2file.setObjectName("lineEdit_path2file")
        self.gridLayout.addWidget(self.lineEdit_path2file, 1, 1, 1, 1)
        self.pushButton_load_file = QtWidgets.QPushButton(self.widget_keywords)
        self.pushButton_load_file.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_load_file.sizePolicy().hasHeightForWidth())
        self.pushButton_load_file.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_load_file.setFont(font)
        self.pushButton_load_file.setObjectName("pushButton_load_file")
        self.gridLayout.addWidget(self.pushButton_load_file, 1, 2, 1, 1)
        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 6)
        self.gridLayout.setColumnStretch(2, 1)
        self.verticalLayout.addWidget(self.widget_keywords)
        self.widget_output = QtWidgets.QWidget(self.groupBox_config)
        self.widget_output.setObjectName("widget_output")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_output)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.widget_output)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.lineEdit_output = QtWidgets.QLineEdit(self.widget_output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_output.sizePolicy().hasHeightForWidth())
        self.lineEdit_output.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_output.setFont(font)
        self.lineEdit_output.setInputMask("")
        self.lineEdit_output.setObjectName("lineEdit_output")
        self.horizontalLayout_5.addWidget(self.lineEdit_output)
        self.pushButton_output = QtWidgets.QPushButton(self.widget_output)
        self.pushButton_output.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_output.sizePolicy().hasHeightForWidth())
        self.pushButton_output.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_output.setFont(font)
        self.pushButton_output.setObjectName("pushButton_output")
        self.horizontalLayout_5.addWidget(self.pushButton_output)
        self.horizontalLayout_5.setStretch(0, 2)
        self.horizontalLayout_5.setStretch(1, 6)
        self.horizontalLayout_5.setStretch(2, 1)
        self.verticalLayout.addWidget(self.widget_output)
        self.widget_3 = QtWidgets.QWidget(self.groupBox_config)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.checkBox_face_only = QtWidgets.QCheckBox(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_face_only.sizePolicy().hasHeightForWidth())
        self.checkBox_face_only.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_face_only.setFont(font)
        self.checkBox_face_only.setObjectName("checkBox_face_only")
        self.horizontalLayout_4.addWidget(self.checkBox_face_only)
        self.checkBox_safe_mode = QtWidgets.QCheckBox(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_safe_mode.sizePolicy().hasHeightForWidth())
        self.checkBox_safe_mode.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_safe_mode.setFont(font)
        self.checkBox_safe_mode.setCheckable(True)
        self.checkBox_safe_mode.setChecked(True)
        self.checkBox_safe_mode.setObjectName("checkBox_safe_mode")
        self.horizontalLayout_4.addWidget(self.checkBox_safe_mode)
        self.label_6 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.spinBox_max_number = QtWidgets.QSpinBox(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_max_number.sizePolicy().hasHeightForWidth())
        self.spinBox_max_number.setSizePolicy(sizePolicy)
        self.spinBox_max_number.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinBox_max_number.setFont(font)
        self.spinBox_max_number.setMinimum(1)
        self.spinBox_max_number.setMaximum(2000)
        self.spinBox_max_number.setProperty("value", 100)
        self.spinBox_max_number.setObjectName("spinBox_max_number")
        self.horizontalLayout_4.addWidget(self.spinBox_max_number)
        self.label_5 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.spinBox_num_threads = QtWidgets.QSpinBox(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_num_threads.sizePolicy().hasHeightForWidth())
        self.spinBox_num_threads.setSizePolicy(sizePolicy)
        self.spinBox_num_threads.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinBox_num_threads.setFont(font)
        self.spinBox_num_threads.setMinimum(1)
        self.spinBox_num_threads.setMaximum(200)
        self.spinBox_num_threads.setProperty("value", 50)
        self.spinBox_num_threads.setObjectName("spinBox_num_threads")
        self.horizontalLayout_4.addWidget(self.spinBox_num_threads)
        self.horizontalLayout_4.setStretch(0, 2)
        self.horizontalLayout_4.setStretch(1, 2)
        self.horizontalLayout_4.setStretch(4, 1)
        self.horizontalLayout_4.setStretch(5, 1)
        self.verticalLayout.addWidget(self.widget_3)
        self.widget_proxy = QtWidgets.QWidget(self.groupBox_config)
        self.widget_proxy.setObjectName("widget_proxy")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_proxy)
        self.horizontalLayout_2.setContentsMargins(-1, 9, -1, 9)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBox_proxy = QtWidgets.QCheckBox(self.widget_proxy)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_proxy.sizePolicy().hasHeightForWidth())
        self.checkBox_proxy.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_proxy.setFont(font)
        self.checkBox_proxy.setObjectName("checkBox_proxy")
        self.horizontalLayout_2.addWidget(self.checkBox_proxy)
        self.widget_5 = QtWidgets.QWidget(self.widget_proxy)
        self.widget_5.setEnabled(False)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.radioButton_http = QtWidgets.QRadioButton(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_http.sizePolicy().hasHeightForWidth())
        self.radioButton_http.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_http.setFont(font)
        self.radioButton_http.setFocusPolicy(QtCore.Qt.TabFocus)
        self.radioButton_http.setChecked(True)
        self.radioButton_http.setObjectName("radioButton_http")
        self.buttonGroup_2 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.radioButton_http)
        self.horizontalLayout_3.addWidget(self.radioButton_http)
        self.radioButton_socks5 = QtWidgets.QRadioButton(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_socks5.sizePolicy().hasHeightForWidth())
        self.radioButton_socks5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_socks5.setFont(font)
        self.radioButton_socks5.setFocusPolicy(QtCore.Qt.TabFocus)
        self.radioButton_socks5.setChecked(False)
        self.radioButton_socks5.setObjectName("radioButton_socks5")
        self.buttonGroup_2.addButton(self.radioButton_socks5)
        self.horizontalLayout_3.addWidget(self.radioButton_socks5)
        self.lineEdit_proxy = QtWidgets.QLineEdit(self.widget_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_proxy.setFont(font)
        self.lineEdit_proxy.setObjectName("lineEdit_proxy")
        self.horizontalLayout_3.addWidget(self.lineEdit_proxy)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 4)
        self.horizontalLayout_2.addWidget(self.widget_5)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 5)
        self.verticalLayout.addWidget(self.widget_proxy)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 2)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 2)
        self.verticalLayout.setStretch(5, 1)
        self.gridLayout_3.addWidget(self.groupBox_config, 0, 0, 1, 1)
        self.plainTextEdit_log = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        self.plainTextEdit_log.setFont(font)
        self.plainTextEdit_log.setReadOnly(True)
        self.plainTextEdit_log.setPlainText("")
        self.plainTextEdit_log.setTabStopWidth(4)
        self.plainTextEdit_log.setMaximumBlockCount(0)
        self.plainTextEdit_log.setObjectName("plainTextEdit_log")
        self.gridLayout_3.addWidget(self.plainTextEdit_log, 2, 0, 1, 2)
        self.gridLayout_3.setColumnStretch(0, 8)
        self.gridLayout_3.setColumnStretch(1, 2)
        self.gridLayout_3.setRowStretch(0, 7)
        self.gridLayout_3.setRowStretch(1, 3)
        self.gridLayout_3.setRowStretch(2, 4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuAbout.menuAction())
        self.label.setBuddy(self.lineEdit_keywords)
        self.label_7.setBuddy(self.lineEdit_output)
        self.label_6.setBuddy(self.spinBox_max_number)
        self.label_5.setBuddy(self.spinBox_num_threads)

        self.retranslateUi(MainWindow)
        self.checkBox_from_file.clicked['bool'].connect(self.lineEdit_keywords.setDisabled)
        self.checkBox_from_file.clicked['bool'].connect(self.pushButton_load_file.setEnabled)
        self.checkBox_from_file.clicked['bool'].connect(self.lineEdit_path2file.setEnabled)
        self.checkBox_proxy.clicked['bool'].connect(self.widget_5.setEnabled)
        self.checkBox_proxy.clicked['bool'].connect(self.lineEdit_proxy.setFocus)
        self.radioButton_google.toggled['bool'].connect(self.checkBox_safe_mode.setEnabled)
        self.radioButton_bing.toggled['bool'].connect(self.checkBox_safe_mode.setChecked)
        self.radioButton_baidu.toggled['bool'].connect(self.checkBox_safe_mode.setChecked)
        self.radioButton_google.toggled['bool'].connect(self.checkBox_safe_mode.setChecked)
        self.checkBox_from_file.clicked['bool'].connect(self.pushButton_load_file.click)
        self.radioButton_baidu.toggled['bool'].connect(self.widget_driver.setDisabled)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit_keywords, self.checkBox_from_file)
        MainWindow.setTabOrder(self.checkBox_from_file, self.lineEdit_path2file)
        MainWindow.setTabOrder(self.lineEdit_path2file, self.pushButton_load_file)
        MainWindow.setTabOrder(self.pushButton_load_file, self.lineEdit_output)
        MainWindow.setTabOrder(self.lineEdit_output, self.pushButton_output)
        MainWindow.setTabOrder(self.pushButton_output, self.checkBox_face_only)
        MainWindow.setTabOrder(self.checkBox_face_only, self.checkBox_safe_mode)
        MainWindow.setTabOrder(self.checkBox_safe_mode, self.spinBox_max_number)
        MainWindow.setTabOrder(self.spinBox_max_number, self.spinBox_num_threads)
        MainWindow.setTabOrder(self.spinBox_num_threads, self.checkBox_proxy)
        MainWindow.setTabOrder(self.checkBox_proxy, self.radioButton_http)
        MainWindow.setTabOrder(self.radioButton_http, self.radioButton_socks5)
        MainWindow.setTabOrder(self.radioButton_socks5, self.lineEdit_proxy)
        MainWindow.setTabOrder(self.lineEdit_proxy, self.pushButton_start)
        MainWindow.setTabOrder(self.pushButton_start, self.pushButton_cancel)
        MainWindow.setTabOrder(self.pushButton_cancel, self.radioButton_google)
        MainWindow.setTabOrder(self.radioButton_google, self.radioButton_bing)
        MainWindow.setTabOrder(self.radioButton_bing, self.radioButton_baidu)
        MainWindow.setTabOrder(self.radioButton_baidu, self.plainTextEdit_log)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_3.setTitle(_translate("MainWindow", "进度条"))
        self.label_4.setText(_translate("MainWindow", "总用时:"))
        self.label_time_elapsed.setText(_translate("MainWindow", "00:00:00"))
        self.label_2.setText(_translate("MainWindow", "总进度:"))
        self.label_3.setText(_translate("MainWindow", "当前进度:"))
        self.groupBox_2.setTitle(_translate("MainWindow", "控制"))
        self.pushButton_open.setText(_translate("MainWindow", "打开下载文件夹"))
        self.pushButton_start.setText(_translate("MainWindow", "启动"))
        self.pushButton_start.setShortcut(_translate("MainWindow", "返回"))
        self.pushButton_cancel.setText(_translate("MainWindow", "&取消"))
        self.groupBox_config.setTitle(_translate("MainWindow", "配置"))
        self.radioButton_google.setText(_translate("MainWindow", "&谷歌"))
        self.radioButton_bing.setText(_translate("MainWindow", "&Bing"))
        self.radioButton_baidu.setText(_translate("MainWindow", "百度"))
        self.radioButton_chrome_headless.setText(_translate("MainWindow", "谷歌无图形"))
        self.radioButton_chrome.setText(_translate("MainWindow", "谷歌图形化"))
        self.radioButton_phantomjs.setText(_translate("MainWindow", "PhantomJs"))
        self.label.setText(_translate("MainWindow", "&关键词:"))
        self.lineEdit_keywords.setToolTip(_translate("MainWindow", "输入关键字，用逗号分隔  \", \""))
        self.lineEdit_keywords.setStatusTip(_translate("MainWindow", "提示:例如下载乔丹和姚明的图片，输入 \"Micheal Jordan, Yao Ming\""))
        self.lineEdit_keywords.setPlaceholderText(_translate("MainWindow", "多个关键词用逗号 ( , )"))
        self.checkBox_from_file.setText(_translate("MainWindow", "&加载文件:"))
        self.lineEdit_path2file.setStatusTip(_translate("MainWindow", "提示:输入文本文件的路径。文件的每一行都包含一组关键字"))
        self.lineEdit_path2file.setPlaceholderText(_translate("MainWindow", "文件路径"))
        self.pushButton_load_file.setText(_translate("MainWindow", "..."))
        self.label_7.setText(_translate("MainWindow", "&输出文件夹:"))
        self.lineEdit_output.setToolTip(_translate("MainWindow", "输出目录路径."))
        self.lineEdit_output.setStatusTip(_translate("MainWindow", "输出目录路径."))
        self.lineEdit_output.setText(_translate("MainWindow", "./download_images"))
        self.lineEdit_output.setPlaceholderText(_translate("MainWindow", "输出目录路径."))
        self.pushButton_output.setText(_translate("MainWindow", "..."))
        self.checkBox_face_only.setText(_translate("MainWindow", "&只抓人脸图片"))
        self.checkBox_safe_mode.setText(_translate("MainWindow", "&安全模式"))
        self.label_6.setText(_translate("MainWindow", "最大数量\n"
"每个关键字"))
        self.label_5.setText(_translate("MainWindow", "&线程:"))
        self.checkBox_proxy.setText(_translate("MainWindow", "&代理:"))
        self.radioButton_http.setText(_translate("MainWindow", "HTTP"))
        self.radioButton_socks5.setText(_translate("MainWindow", "Socks5"))
        self.lineEdit_proxy.setToolTip(_translate("MainWindow", "IP地址:端口号"))
        self.lineEdit_proxy.setStatusTip(_translate("MainWindow", "xxx.xxx.xxx.xx:端口号"))
        self.lineEdit_proxy.setPlaceholderText(_translate("MainWindow", "xxx.xxx.xxx.xx:端口号"))
        self.menuAbout.setTitle(_translate("MainWindow", "帮助"))
        self.actionAbout.setText(_translate("MainWindow", "关于"))

