import locale
locale.setlocale(locale.LC_NUMERIC, 'C')

import sys
import mpv
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QFrame

# YOU CAN ADD ALL YOUR CAMERAS HERE, THE SCRIPT IS BUILT FOR 2X2 GRID SO YOU CAN EDIT IT
CAMARAS = [
    "rtsp://user:pass@YOUR-CAMERA-IP/h264/ch1/main/av_stream",
]

class Player(QFrame):
    def __init__(self, url):
        super().__init__()
        self.setStyleSheet("background-color: black;")

        self.player = mpv.MPV(
            wid=str(int(self.winId())),
            vo='gpu',
            hwdec='auto',
            rtsp_transport='tcp',
            audio='no'
        )
        self.player.play(url)
    
class CamarasApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mis Cámaras")
        self.setGeometry(100, 100, 1000, 700)

        layout = QGridLayout(self)
        posiciones = [(0,0), (0,1), (1,0), (1,1)]

        for pos, url in zip(posiciones, CAMARAS):
            cam = Player(url)
            layout.addWidget(cam, *pos)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = CamarasApp()
    win.show()
    sys.exit(app.exec_())
