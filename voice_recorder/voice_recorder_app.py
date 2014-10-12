from PyQt4 import QtCore
from PyQt4.QtGui import QApplication, QMainWindow
import sys
from main_ui import Ui_MainWindow
from voice_recorder import VoiceRecorder


class VoiceRecorderApp(object):
    def __init__(self):
        app = QApplication(sys.argv)
        self.window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.app_init()
        self.window.show()
        sys.exit(app.exec_())

    # noinspection PyAttributeOutsideInit
    def app_init(self):
        self.window.connect(self.ui.start, QtCore.SIGNAL('triggered()'), self.on_start)
        self.window.connect(self.ui.pause, QtCore.SIGNAL('triggered()'), self.on_pause)
        self.window.connect(self.ui.resume, QtCore.SIGNAL('triggered()'), self.on_resume)
        self.window.connect(self.ui.stop, QtCore.SIGNAL('triggered()'), self.on_stop)
        self.window.connect(self.ui.exit, QtCore.SIGNAL('triggered()'), self.on_exit)
        self.recorder = VoiceRecorder(r"g:\tmp.mp3")

    def on_start(self):
        self.recorder.start_record()

    def on_stop(self):
        self.recorder.stop()

    def on_exit(self):
        self.recorder.stop()
        self.window.close()

    def on_pause(self):
        pass

    def on_resume(self):
        pass


def main():
    VoiceRecorderApp()


if __name__ == "__main__":
    main()