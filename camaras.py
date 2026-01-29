import locale
locale.setlocale(locale.LC_NUMERIC, 'C')

import sys
import subprocess

from PyQt5.QtWidgets import (
    QApplication, QWidget, QGridLayout,
    QFrame, QLabel, QVBoxLayout, QHBoxLayout
)
from PyQt5.QtCore import QTimer, Qt


# =========================
# CONFIGURACIÓN DE CÁMARAS
# =========================
CAMARAS = [
    ("Terraza", "rtsp://user:pass@YOUR-CAMERA-IP/h264/ch1/main/av_stream"),
    ("Patio",   "rtsp://user:pass@YOUR-CAMERA-IP/h264/ch2/main/av_stream"),
    ("Exterior 1",  "rtsp://user:pass@YOUR-CAMERA-IP/h264/ch3/main/av_stream"),
    ("Exterior 2",  "rtsp://user:pass@YOUR-CAMERA-IP/h264/ch4/main/av_stream"),
]


# =========================
# WIDGET DE UNA CÁMARA
# =========================
class CameraWidget(QWidget):
    def __init__(self, name, url):
        super().__init__()
        self.name = name
        self.url = url
        self.proc = None

        self.setStyleSheet("background-color: black;")

        # Indicador de estado
        self.indicator = QLabel()
        self.indicator.setFixedSize(12, 12)
        self.indicator.setStyleSheet(self._style("connecting"))

        # Nombre de la cámara
        self.title = QLabel(name)
        self.title.setStyleSheet("color: white; font-size: 12px;")

        header = QWidget()
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(0, 0, 0, 0)
        header_layout.setSpacing(6)

        header_layout.addWidget(self.indicator, alignment=Qt.AlignVCenter)
        header_layout.addWidget(self.title, alignment=Qt.AlignVCenter)
        header_layout.addStretch()

        # Área de video
        self.video = QFrame()
        self.video.setStyleSheet("background-color: black;")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(5, 5, 5, 5)
        layout.addWidget(header)
        layout.addWidget(self.video, stretch=1)

        self.start_mpv()

        # Timer para verificar estado
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_status)
        self.timer.start(2000)

    # -------------------------
    # Lanzar mpv
    # -------------------------
    def start_mpv(self):
        self.set_status("connecting")

        cmd = [
            "mpv",
            "--no-border",
            "--no-audio",
            "--hwdec=auto",
            "--rtsp-transport=tcp",
            "--profile=low-latency",
            f"--wid={int(self.video.winId())}",
            self.url
        ]

        try:
            self.proc = subprocess.Popen(cmd)
        except FileNotFoundError:
            self.set_status("offline")
            print("ERROR: mpv no encontrado")

    # -------------------------
    # Revisar estado
    # -------------------------
    def check_status(self):
        if self.proc is None:
            self.set_status("offline")
            return

        if self.proc.poll() is None:
            self.set_status("online")
        else:
            self.set_status("offline")

    # -------------------------
    # UI estado
    # -------------------------
    def set_status(self, status):
        self.indicator.setStyleSheet(self._style(status))

    def _style(self, status):
        colors = {
            "online": "#00ff00",
            "connecting": "#ffcc00",
            "offline": "#ff0000"
        }
        return f"""
            background-color: {colors[status]};
            border-radius: 6px;
        """


# =========================
# APP PRINCIPAL
# =========================
class CamarasApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mis Cámaras")
        self.setGeometry(100, 100, 1000, 700)

        layout = QGridLayout(self)
        layout.setSpacing(10)

        posiciones = [(0, 0), (0, 1), (1, 0), (1, 1)]

        for (name, url), (row, col) in zip(CAMARAS, posiciones):
            cam = CameraWidget(name, url)
            layout.addWidget(cam, row, col)


# =========================
# MAIN
# =========================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = CamarasApp()
    win.show()
    sys.exit(app.exec_())

