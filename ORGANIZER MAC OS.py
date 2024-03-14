import os
import shutil

import Foundation
import objc
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog

NSUserNotification = objc.lookUpClass('NSUserNotification')
NSUserNotificationCenter = objc.lookUpClass('NSUserNotificationCenter')
def notify(title, subtitle, info_text, delay=0,  userInfo={}):
    notification = NSUserNotification.alloc().init()
    notification.setTitle_(title)
    notification.setSubtitle_(subtitle)
    notification.setInformativeText_(info_text)
    notification.setUserInfo_(userInfo)
    notification.setSoundName_("NSUserNotificationDefaultSoundName")
    notification.setDeliveryDate_(Foundation.NSDate.dateWithTimeInterval_sinceDate_(delay, Foundation.NSDate.date()))

    NSUserNotificationCenter.defaultUserNotificationCenter().scheduleNotification_(notification)



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("ORGANIZER")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox_audio = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_audio.setObjectName("checkBox_audio")
        self.verticalLayout.addWidget(self.checkBox_audio)
        self.checkBox_video = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_video.setObjectName("checkBox_video")
        self.verticalLayout.addWidget(self.checkBox_video)
        self.checkBox_docs = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_docs.setObjectName("checkBox_docs")
        self.verticalLayout.addWidget(self.checkBox_docs)
        self.checkBox_programme = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_programme.setObjectName("checkBox_programme")
        self.verticalLayout.addWidget(self.checkBox_programme)
        self.checkBox_plan = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_plan.setObjectName("checkBox_plan")
        self.verticalLayout.addWidget(self.checkBox_plan)
        self.checkBox_image = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_image.setObjectName("checkBox_image")
        self.verticalLayout.addWidget(self.checkBox_image)
        self.checkBox_compressed = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_compressed.setObjectName("checkBox_compressed")
        self.verticalLayout.addWidget(self.checkBox_compressed)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 2)
        self.pushButton_folder = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_folder.setObjectName("pushButton_folder")
        self.gridLayout.addWidget(self.pushButton_folder, 2, 0, 1, 1)
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setObjectName("pushButton_start")
        self.gridLayout.addWidget(self.pushButton_start, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.checkBox_audio.setText("audio formats")
        self.checkBox_video.setText("video formats")
        self.checkBox_docs.setText("docs formats")
        self.checkBox_programme.setText("programme formats")
        self.checkBox_plan.setText("plan formats")
        self.checkBox_image.setText("image formats")
        self.checkBox_compressed.setText("compressed formats")
        self.pushButton_folder.setText("select folder")
        self.pushButton_start.setText("start")

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton_start.clicked.connect(self.start)
        self.pushButton_folder.clicked.connect(self.getPath)

    def getPath(self):
        fname = QFileDialog.getExistingDirectory()
        self.label.setText(fname)

    def folderName(self):
        folders = []
        if self.checkBox_programme.isChecked():
            folders += ['Programs']
        if self.checkBox_image.isChecked():
            folders += ['Image']
        if self.checkBox_audio.isChecked():
            folders += ['Music']
        if self.checkBox_video.isChecked():
            folders += ['Video']
        if self.checkBox_docs.isChecked():
            folders += ['Documents']
        if self.checkBox_plan.isChecked():
            folders += ['Plan']
        if self.checkBox_compressed.isChecked():
            folders += ['Compressed']
        return folders

    def chekFolder(self):
        folder = self.folderName()
        Path = self.label.text()
        x = 0
        while x < len(folder):
            fold = f"{Path}/{folder[x]}"
            if not os.path.exists(fold):
                os.makedirs(fold)
            x += 1

    def typeFile(self):
        typef = []
        if self.checkBox_programme.isChecked():
            typef += [["exe", "msi", "dmg", "pkg", "app"]]
        if self.checkBox_image.isChecked():
            typef += [["jpg", "png", "jpeg", "ico", "gif", "tiff","heic","dng"]]
        if self.checkBox_audio.isChecked():
            typef += [["mp3", "wav"]]
        if self.checkBox_video.isChecked():
            typef += [["mp4", "avi", "webm"]]
        if self.checkBox_docs.isChecked():
            typef += [["txt", "csv", "xlsm", "pdf", "xls", "xlsx","docx","ppt","doc"]]
        if self.checkBox_plan.isChecked():
            typef += [["dwg", "bak"]]
        if self.checkBox_compressed.isChecked():
            typef += [["zip", "rar"]]
        return typef

    def start(self):
        notify("File organiser", "Start", "The process has been Started")
        self.chekFolder()
        path = str(self.label.text())
        files = os.listdir(path)
        xx = len(self.folderName())
        for file in files:
            if os.path.isfile(path + "/" + file):
                ext = (file.split(".")[-1]).lower()
                x = 0
                while x < xx:
                    if ext in self.typeFile()[x]:
                        src = f"{path}/{file}"
                        dst = f"{path}/{self.folderName()[x]}/{file}"
                        shutil.move(src, dst)
                    x += 1
        notify("File organiser", "Finish", "The process has been finished")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
