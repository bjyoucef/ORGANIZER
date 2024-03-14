import os
import shutil
import Foundation
import objc
import sys
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
    docs_formats = ["txt", "csv", "xlsm", "pdf", "xls","xlsx","docx","ppt","doc"]
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



NSUserNotification = objc.lookUpClass('NSUserNotification')
NSUserNotificationCenter = objc.lookUpClass('NSUserNotificationCenter')
#
def notify(title, subtitle, info_text, delay=0,  userInfo={}):
    notification = NSUserNotification.alloc().init()
    notification.setTitle_(title)
    notification.setSubtitle_(subtitle)
    notification.setInformativeText_(info_text)
    notification.setUserInfo_(userInfo)

    notification.setSoundName_("NSUserNotificationDefaultSoundName")
    notification.setDeliveryDate_(Foundation.NSDate.dateWithTimeInterval_sinceDate_(delay, Foundation.NSDate.date()))
    NSUserNotificationCenter.defaultUserNotificationCenter().scheduleNotification_(notification)

def organ():
    path = chekFolder()
    print(path)
    notify("File organiser", "Start", "The process has been Started")
    files = os.listdir(path)
    for file in files:
        if os.path.isfile(path + "/" + file):
            ext = (file.split(".")[-1]).lower()
            x = 0
            while x < len(folderName()):
                if ext in typeFile()[x]:
                    shutil.move(path + "/" + file, path + "/" + folderName()[x] + "/" + file)
                x += 1
    notify("File organiser", "Finish", "The process has been finished")


class fileOrgan(QWidget):
    def __init__(self, parent=None):
        super(fileOrgan, self).__init__(parent)
        organ()


def main():
    app = QApplication(sys.argv)
    ex = fileOrgan()


if __name__ == '__main__':
    main()
