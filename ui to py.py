
# python -m PyQt5.uic.pyuic -x ORGANIZER.ui -o ORGANIZER MAC OS.py

from PyQt5.QtCore import Qt


def programme_f(state):
    if state == Qt.Checked:
        return True
    elif state == Qt.Unchecked:
        return False


def compressed_f(state):
    if state == Qt.Checked:
        return True
    elif state == Qt.Unchecked:
        return False


def plan_f(state):
    if state == Qt.Checked:
        return True
    elif state == Qt.Unchecked:
        return False


def docs_f(state):
    if state == Qt.Checked:
        return True
    elif state == Qt.Unchecked:
        return False


def video_f(state):
    if state == Qt.Checked:
        return True
    elif state == Qt.Unchecked:
        return False


def audio_f(state):
    if state == Qt.Checked:
        return True
    elif state == Qt.Unchecked:
        return False


def image_f(state):
    if state == Qt.Checked:
        return True
    elif state == Qt.Unchecked:
        return False

self.checkBox_audio.stateChanged.connect(audio_f)
self.checkBox_video.stateChanged.connect(video_f)
self.checkBox_docs.stateChanged.connect(docs_f)
self.checkBox_programme.stateChanged.connect(programme_f)
self.checkBox_plan.stateChanged.connect(plan_f)
self.checkBox_image.stateChanged.connect(image_f)
self.checkBox_compressed.stateChanged.connect(compressed_f)