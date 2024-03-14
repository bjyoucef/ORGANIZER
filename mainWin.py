import os
import shutil
import sys
from win10toast import ToastNotifier
from PyQt5.QtWidgets import QFileDialog, QWidget, QApplication


def folderName():
    folders = ['Image', 'Music', 'Video', 'Documents', 'Programs', 'Plan', 'Compressed']
    return folders


def getPath():
    fname = QFileDialog.getExistingDirectory()
    return fname


def typeFile():
    image_formats = ["jpg", "png", "jpeg", "ico", "gif", "tiff"]
    audio_formats = ["mp3", "wav"]
    video_formats = ["mp4", "avi", "webm"]
    docs_formats = ["txt", "csv", "xlsm", "pdf", "xls"]
    programme_formats = ["exe", "msi","dmg","pkg","app"]
    plan_formats = ["dwg", "bak"]
    compressed_formats = ["zip", "rar"]

    return image_formats, audio_formats, video_formats, docs_formats, programme_formats, plan_formats, compressed_formats


def chekFolder():
    folder = folderName()
    Path = getPath()
    x = 0
    while x < len(folder):
        if not os.path.exists(Path + "/" + folder[x]):
            os.makedirs(Path + "/" + folder[x])
        x += 1
    return Path


def notification(title,info_text,icon, duration):
    toast = ToastNotifier()
    toast.show_toast(title, info_text,icon, duration)

# notification("File organiser", "The process has been Started","ubm.ico", 2)



def organ():
    path = chekFolder()
    notification("File organiser", "The process has been Started","ubm.ico", 2)
    files = os.listdir(path)
    for file in files:
        if os.path.isfile(path + "/" + file):
            ext = (file.split(".")[-1]).lower()
            x = 0
            while x < len(folderName()):
                if ext in typeFile()[x]:
                    shutil.move(path + "/" + file, path + "/" + folderName()[x] + "/" + file)
                x += 1
    notification("File organiser","The process has been finished","ubm.ico",duration=5)


class fileOrgan(QWidget):
    def __init__(self, parent=None):
        super(fileOrgan, self).__init__(parent)
        organ()


def main():
    app = QApplication(sys.argv)
    ex = fileOrgan()


if __name__ == '__main__':
    main()
