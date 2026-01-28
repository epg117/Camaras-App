import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QFrame
from PyQt5.QtCore import Qt

CAMARAS = [
    "rtsp://user:password@your-camera-ip/h264/ch1/main/av_stream",
    "rtsp://user:password@your-camera-ip/h264/ch2/main/av_stream",
    "rtsp://user:password@your-camera-ip/h264/ch3/main/av_stream",
    "rtsp://user:password@your-camera-ip/h264/ch4/main/av_stream",
]

class Player(QFrame):
    def __init__(self, url):
        super().__init__()
        self.url = url
        self.proc = None
        self.setStyleSheet("background-color: black;")
        self.setAttribute(Qt.WA_NativeWindow)
        self.setAttribute(Qt.WA_DontCreateNativeAncestors)

    def showEvent(self, event):
        if self.proc is None:
            self.start_mpv()
        super().showEvent(event)

    def start_mpv(self):
        wid = str(int(self.winId()))

        cmd = [
            "mpv",
            "--no-config",
            "--profile=low-latency",
            "--rtsp-transport=tcp",
            "--hwdec=auto",
            "--vo=x11",
            "--cache=no",
            "--audio=no",
            f"--wid={wid}",
            self.url
        ]

        self.proc = subprocess.Popen(cmd)

    def closeEvent(self, event):
        if self.proc:
            self.proc.terminate()
        super().closeEvent(event)

class CamarasApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mis Cámaras")
        self.resize(1000, 700)

        layout = QGridLayout(self)
        layout.setSpacing(2)

        posiciones = [(0,0), (0,1), (1,0), (1,1)]

        for pos, url in zip(posiciones, CAMARAS):
            layout.addWidget(Player(url), *pos)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = CamarasApp()
    win.show()
    sys.exit(app.exec_())


