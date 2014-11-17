import os
from PyQt4 import QtCore
from PyQt4.QtGui import QApplication, QMainWindow
import sys
from PyQt4 import QtGui
import time

try:
    #Work around for package name and file name is the same issue
    from voice_recorder.main_ui import Ui_MainWindow
    from voice_recorder.voice_recorder import VoiceRecorder
    from voice_recorder.json_config import JsonConfig
except ImportError:
    from main_ui import Ui_MainWindow
    from voice_recorder import VoiceRecorder
    from json_config import JsonConfig


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
    def create_new_file(self):
        self.current_file = time.strftime('%Y%m%d_%H%I%M.mp3', time.localtime(time.time()))
        self.ui.note_name.setText(self.current_file)
        self.current_full_path = os.path.join(self.note_folder, self.current_file)

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
        self.recorder = None
        self.recorded_seconds = 0
        self.window.connect(self.ui.browser_dir, QtCore.SIGNAL('clicked()'), self.on_browser_dir)
        self.config = JsonConfig()
        self.note_folder = self.config.get("note_folder", r"g:\tmp")
        self.ui.note_folder.setText(self.note_folder)
        #self.create_new_file()

    def on_start(self):
        self.create_new_file()
        if self.recorder is None:
            self.recorder = VoiceRecorder(self.current_full_path)
        self.recorder.start_record()  # constant timer
        # noinspection PyCallByClass
        QtCore.QObject.connect(self.constant_timer, QtCore.SIGNAL("timeout()"), self.on_timer)
        self.constant_timer.start(1000)

    def on_timer(self):
        """
        slot for constant timer timeout
        """
        if self.recorder.is_recording():
            self.recorded_seconds += 1
            val = "%03d:%02d" % (self.recorded_seconds / 60, self.recorded_seconds % 60)
            self.ui.recorded_minutes_and_seconds.setText(val)

    def on_stop(self):
        self.recorder.stop()

    def on_exit(self):
        if (not self.recorder is None) and self.recorder.is_recording():
            self.recorder.stop()
        self.window.close()

    def on_pause(self):
        pass

    def on_resume(self):
        pass

    def on_browser_dir(self):
        dialog = QtGui.QFileDialog(self.window)
        dialog.setFileMode(QtGui.QFileDialog.Directory)
        dialog.setOption(QtGui.QFileDialog.ShowDirsOnly, True)

        if dialog.exec_():
            for d in dialog.selectedFiles():
                self.ui.note_folder.setText(d)
                self.config.set("note_folder", str(d))


def main():
    VoiceRecorderApp()


if __name__ == "__main__":
    main()