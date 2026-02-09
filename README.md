git clone [https://github.com/JavierYago/detector-de-gestos.git](https://github.com/TU_USUARIO/detector-de-gestos.git)
git clone [https://github.com/JavierYago/detector-de-gestos.git](https://github.com/YOUR_USERNAME/detector-de-gestos.git)
# 🖐️ AI Hand Gesture Controller / Control por Gestos con IA

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Vision-orange?logo=google&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green?logo=opencv&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey?logo=windows&logoColor=white)

![Demo del Proyecto](demo.png)

---

**Language / Idioma:** [🇪🇸 Ir a la versión en Español](#-versión-en-español) | [🇺🇸 Go to English Version](#-english-version)

---

## 🇪🇸 Versión en Español

### 📝 Descripción
Este proyecto es un sistema de **Visión Artificial** en tiempo real que detecta la mano del usuario, interpreta la posición de los dedos y ejecuta acciones automatizadas en el ordenador.

Utiliza **Google MediaPipe** para la detección esquelética de la mano y **OpenCV** para el procesamiento de imagen. Actualmente está configurado para lanzar el navegador **Brave** al detectar el gesto de "Amor y Paz", incluyendo un sistema de seguridad para evitar ejecuciones múltiples.

### ✨ Funcionalidades
- **Detección en tiempo real** de 21 puntos clave de la mano.
- **Lógica geométrica** propia para interpretar si los dedos están abiertos o cerrados.
- **Reconocimiento de Gestos:**
  - ✌️ **Paz y Amor:** Abre el navegador Brave (con contador de seguridad).
- **Sistema "Cooldown" (Anti-rebote):** Temporizador inteligente (5 segundos) que impide que la aplicación se abra múltiples veces seguidas si mantienes el gesto.
- **Interfaz Visual:** Muestra el esqueleto de la mano y mensajes de estado sobre la cámara.

### 🚀 Instalación y Uso

#### 1. Requisitos Previos
Necesitas tener **Python 3.10** instalado (recomendado para compatibilidad con MediaPipe).

#### 2. Instalación Paso a Paso
```bash
# 1. Clonar el repositorio
git clone https://github.com/TU_USUARIO/detector-de-gestos.git
cd detector-de-gestos

# 2. Crear entorno virtual
py -3.10 -m venv .venv

# 3. Activar entorno (Windows PowerShell)
.\.venv\Scripts\Activate

# 4. Instalar dependencias
pip install -r requirements.txt
```

#### 3. Configuración
Abre el archivo `main.py` y busca la variable `ruta_brave`. Cambia la ruta por la ubicación de `brave.exe` (o cualquier otro programa que quieras abrir) en tu ordenador:

```python
ruta_brave = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
```

#### 4. Ejecución
```bash
python main.py
```

Para salir, pulsa la tecla ESC.

---

## 🇺🇸 English Version

### 📝 Description
This project is a real-time Computer Vision system that tracks the user's hand, interprets finger positions, and executes automated actions on the PC.

It leverages Google MediaPipe for skeletal hand tracking and OpenCV for image processing. Currently configured to launch the Brave browser upon detecting a "Peace" sign, featuring a debounce system to prevent accidental multiple executions.

### ✨ Features
- Real-time tracking of 21 hand landmarks.

- Custom geometric logic to determine if fingers are open or closed.

- Gesture Recognition:
  - ✌️ Peace Sign: Launches Brave browser (with cooldown timer).

- Cooldown System (Debounce): Smart timer (5 seconds) preventing the app from launching multiple times rapidly.

- Visual Interface: On-screen feedback with text overlays and skeleton drawing.

### 🚀 Installation & Usage

#### 1. Prerequisites
You need Python 3.10 installed (recommended for MediaPipe compatibility).

#### 2. Installation Steps
```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/detector-de-gestos.git
cd detector-de-gestos

# 2. Create virtual environment
py -3.10 -m venv .venv

# 3. Activate environment (Windows PowerShell)
.\.venv\Scripts\Activate

# 4. Install dependencies
pip install -r requirements.txt
```

#### 3. Configuration
Open `main.py` and locate the `ruta_brave` variable. Update the path to point to your local `brave.exe` (or any app you wish to launch):

```python
ruta_brave = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
```

#### 4. Run
```bash
python main.py
```

Press ESC to exit.
