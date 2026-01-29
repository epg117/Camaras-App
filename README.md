# 📷 IP Camera Monitor on Linux (Python + mpv)

A desktop application in **Linux** developed in **Python** that allows viewing **multiple IP cameras (RTSP)** in a single window using **mpv (libmpv)** embedded in a **PyQt5** interface.

The project is intended for personal/domestic use and as a base to continue expanding functionalities (full screen, reconnection, recording, etc.).

---

![Monitor de Cámaras IP](https://i.imgur.com/TpvOdKn.jpeg)

## 🚀 Characteristics

- Display of **4 IP cameras** in a 2x2 grid
- Use of **mpv** (ffmpeg) for maximum RTSP compatibility
- Graphical interface with **PyQt5**
- Low power consumption and low latency
- RTSP over **TCP** (more stable for IP cameras)
- No audio
- Python environment **isolated with venv**
- Works correctly on **Linux Mint / Ubuntu**

---

## 🧠 Technologies used

- **Python 3**
- **mpv / libmpv**
- **python-mpv**
- **PyQt5**
- **RTSP**

---

## 📦 System requirements

Install system dependencies:

```bash
sudo apt install mpv python3-pyqt5 python3-venv python3-full
```

## Project instalation

Clone the repository:
```bash
git clone https://github.com/epg117/camaras-app.git
cd camaras-app
```

Create a virtual enviroment (venv):
```bash
python3 -m venv venv --system-site-packages
```

Activate the enviroment:
```bash
source venv/bin/activate
```

Install Python dependencies:
```bash
pip install python-mpv
```

## Execution

### IMPORTANT: libmpv has a known bug with locales other than C (e.g., **es_CL**, **es_ES**).

Recommended option:
```bash
LC_NUMERIC=c python camaras.py
```

### Launcher script (recommended)

To avoid typing the command each time, a **run.sh** script is included:

```bash
nano run.sh
```
Content of **run.sh**:
```bash
#!/bin/bash
export LC_NUMERIC=C
source venv/bin/activate
python camaras.py
```
Execute:

```bash
./run.sh
```
## Direct access (.desktop)

Create **.desktop** file:
```bash
nano ~/.local/share/applications
```
Example of **.desktop** file
```bash
[Desktop Entry]
Name=Mis Cámaras
Comment=Monitor de cámaras IP
Exec=env LC_NUMERIC=C /ruta/al/proyecto/venv/bin/python /ruta/al/proyecto/camaras.py
Icon=video-camera
Terminal=false
Type=Application
Categories=Video;Security;
````
Grant permissions to the **.desktop** file:
```bash
chmod +x ~/.local/share/applications/camaras.desktop
```

Now you can access the shortcut from the menu

## Important Technical Notes
- **RTSP** is used over **TCP** for greater stability.
- Audio is disabled (audio=no) to prevent errors.
- Hardware acceleration is disabled if necessary (hwdec=no).
- **venv** only contains project dependencies and does not affect the system Python.
- The **venv/** directory is disposable and should not be uploaded to the repository.

## Project structure
```text
camaras-app/
├── camaras.py
├── run.sh
├── venv/
└── README.md
```



