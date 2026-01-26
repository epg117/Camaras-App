# 📷 Monitor de Cámaras IP en Linux (Python + mpv)

Aplicación de escritorio en **Linux** desarrollada en **Python** que permite visualizar **múltiples cámaras IP (RTSP)** en una sola ventana usando **mpv (libmpv)** embebido en una interfaz **PyQt5**.

El proyecto está pensado para uso personal/doméstico y como base para seguir ampliando funcionalidades (pantalla completa, reconexión, grabación, etc.).

---

## 🚀 Características

- Visualización de **4 cámaras IP** en una grilla 2×2
- Uso de **mpv** (ffmpeg) para máxima compatibilidad con RTSP
- Interfaz gráfica con **PyQt5**
- Bajo consumo y baja latencia
- RTSP sobre **TCP** (más estable para cámaras IP)
- Sin audio
- Entorno Python **aislado con venv**
- Funciona correctamente en **Linux Mint / Ubuntu**

---

## 🧠 Tecnologías utilizadas

- **Python 3**
- **mpv / libmpv**
- **python-mpv**
- **PyQt5**
- **RTSP**

---

## 📦 Requisitos del sistema

Instalar dependencias del sistema:

```bash
sudo apt install mpv python3-pyqt5 python3-venv python3-full
```

## Instalación del proyecto

Clonar el repositorio:
```bash
git clone https://github.com/epg117/camaras-app.git
cd camaras-app
```

Crear un entorno virtual (venv):
```bash
python3 -m venv venv --system-site-packages
```

Activa el entorno:
```bash
source venv/bin/activate
```

Instalar dependencias Python:
```bash
pip install python-mpv
```

## Ejecución

### IMPORTANTE: libmpv presenta un bug conocido con locales distintos de C (por ejemplo **es_CL**, **es_ES**).

Opción recomendada:
```bash
LC_NUMERIC=c python camaras.py
```

### Script lanzador (recomendado)

Para no escribir el comando cada vez, se incluye un script **run.sh**:

```bash
#!/bin/bash
export LC_NUMERIC=C
source venv/bin/activate
python camaras.py
```
Ejecutar:

```bash
./run.sh
```
## Acceso directo (.desktop)

Ejemplo de archivo **.desktop**
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
## Notas técnicas importantes
- Se utiliza **RTSP** sobre **TCP** para mayor estabilidad.
- Se desactiva el audio (audio=no) para evitar errores.
- Se desactiva aceleración por hardware si es necesario (hwdec=no)
- **venv** solo contiene dependencias del proyecto, no afecta al Python del sistema.
- El directorio **venv/** es descartable y no deberia subirse al repositorio.

## Estructura del proyecto
```text
camaras-app/
├── camaras.py
├── run.sh
├── venv/
└── README.md
```



