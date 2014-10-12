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
        self.window.closeEvent = self.on_close_main
        sys.exit(app.exec_())

    def on_close_main(self, *kwargs):
        if hasattr(self, "on_exit"):
            self.on_exit()

    # noinspection PyAttributeOutsideInit
    def app_init(self):
        self.window.connect(self.ui.start, QtCore.SIGNAL('triggered()'), self.on_start)
        self.window.connect(self.ui.start_button, QtCore.SIGNAL('clicked()'), self.on_start)
        self.window.connect(self.ui.pause, QtCore.SIGNAL('triggered()'), self.on_pause)
        self.window.connect(self.ui.pause_button, QtCore.SIGNAL('clicked()'), self.on_pause)
        self.window.connect(self.ui.resume, QtCore.SIGNAL('triggered()'), self.on_resume)
        self.window.connect(self.ui.resume_button, QtCore.SIGNAL('clicked()'), self.on_resume)
        self.window.connect(self.ui.stop, QtCore.SIGNAL('triggered()'), self.on_stop)
        self.window.connect(self.ui.stop_button, QtCore.SIGNAL('clicked()'), self.on_stop)
        self.window.connect(self.ui.exit, QtCore.SIGNAL('triggered()'), self.on_exit)
        self.constant_timer = QtCore.QTimer()
        self.recorder = VoiceRecorder(r"g:\tmp.mp3")
        self.recorded_seconds = 0

    def on_start(self):
        self.recorder.start_record()  # constant timer
        QtCore.QObject.connect(self.constant_timer, QtCore.SIGNAL("timeout()"), self.on_timer)
        self.constant_timer.start(1000)

    def on_timer(self):
        """
        slot for constant timer timeout
        """
        if self.recorder.is_recording():
            self.recorded_seconds += 1
            val = "%03d:%02d" % (self.recorded_seconds / 100, self.recorded_seconds % 100)
            self.ui.recorded_minutes_and_seconds.setText(val)

    def on_stop(self):
        self.recorder.stop()

    def on_exit(self):
        if self.recorder.is_recording():
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