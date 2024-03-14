import os
import shutil

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog

class Main(object):
    def setup_ui(self, main_window):
        main_window.setObjectName("MainWindow")
        main_window.setWindowTitle("ORGANIZER")
        self.centralWidget = QtWidgets.QWidget(main_window)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox_audio = QtWidgets.QCheckBox(self.centralWidget)
        self.checkBox_audio.setObjectName("checkBox_audio")
        self.verticalLayout.addWidget(self.checkBox_audio)
        self.checkBox_video = QtWidgets.QCheckBox(self.centralWidget)
        self.checkBox_video.setObjectName("checkBox_video")
        self.verticalLayout.addWidget(self.checkBox_video)
        self.checkBox_docs = QtWidgets.QCheckBox(self.centralWidget)
        self.checkBox_docs.setObjectName("checkBox_docs")
        self.verticalLayout.addWidget(self.checkBox_docs)
        self.checkBox_programme = QtWidgets.QCheckBox(self.centralWidget)
        self.checkBox_programme.setObjectName("checkBox_programme")
        self.verticalLayout.addWidget(self.checkBox_programme)
        self.checkBox_plan = QtWidgets.QCheckBox(self.centralWidget)
        self.checkBox_plan.setObjectName("checkBox_plan")
        self.verticalLayout.addWidget(self.checkBox_plan)
        self.checkBox_image = QtWidgets.QCheckBox(self.centralWidget)
        self.checkBox_image.setObjectName("checkBox_image")
        self.verticalLayout.addWidget(self.checkBox_image)
        self.checkBox_compressed = QtWidgets.QCheckBox(self.centralWidget)
        self.checkBox_compressed.setObjectName("checkBox_compressed")
        self.verticalLayout.addWidget(self.checkBox_compressed)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 2)
        self.pushButton_folder = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_folder.setObjectName("pushButton_folder")
        self.gridLayout.addWidget(self.pushButton_folder, 2, 0, 1, 1)
        self.pushButton_start = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_start.setObjectName("pushButton_start")
        self.gridLayout.addWidget(self.pushButton_start, 2, 1, 1, 1)
        main_window.setCentralWidget(self.centralWidget)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)

        self.checkBox_audio.setText("audio formats")
        self.checkBox_video.setText("video formats")
        self.checkBox_docs.setText("docs formats")
        self.checkBox_programme.setText("programme formats")
        self.checkBox_plan.setText("plan formats")
        self.checkBox_image.setText("image formats")
        self.checkBox_compressed.setText("compressed formats")
        self.pushButton_folder.setText("select folder")
        self.pushButton_start.setText("start")

        QtCore.QMetaObject.connectSlotsByName(main_window)
        self.pushButton_start.clicked.connect(self.start)
        self.pushButton_folder.clicked.connect(self.get_path)

    def get_path(self):
        fname = QFileDialog.getExistingDirectory()
        self.label.setText(fname)

    def folder_name(self):
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

    def check_folder(self):
        folder = self.folder_name()
        path = self.label.text()
        x = 0
        while x < len(folder):
            fold = f"{path}/{folder[x]}"
            if not os.path.exists(fold):
                os.makedirs(fold)
            x += 1

    def type_file(self):
        typeFiles = []
        if self.checkBox_programme.isChecked():
            typeFiles += [["exe", "msi", "dmg", "pkg", "app"]]
        if self.checkBox_image.isChecked():
            typeFiles += [["jpg", "png", "jpeg", "ico", "gif", "tiff"]]
        if self.checkBox_audio.isChecked():
            typeFiles += [["mp3", "wav"]]
        if self.checkBox_video.isChecked():
            typeFiles += [["mp4", "avi", "webm"]]
        if self.checkBox_docs.isChecked():
            typeFiles += [["txt", "csv", "xlsm", "pdf", "xls", "xlsx"]]
        if self.checkBox_plan.isChecked():
            typeFiles += [["dwg", "bak"]]
        if self.checkBox_compressed.isChecked():
            typeFiles += [["zip", "rar"]]
        return typeFiles

    def start(self):
        path = str(self.label.text())
        if path != "":
            self.check_folder()
            files = os.listdir(path)
            xx = len(self.folder_name())
            for file in files:
                if os.path.isfile(path + "/" + file):
                    ext = (file.split(".")[-1]).lower()
                    x = 0
                    while x < xx:
                        if ext in self.type_file()[x]:
                            src = f"{path}/{file}"
                            dst = f"{path}/{self.folder_name()[x]}/{file}"
                            shutil.move(src, dst)
                        x += 1
        else:
            pass


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Main()
    ui.setup_ui(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
