git clone [https://github.com/JavierYago/detector_de_gestos.git](https://github.com/JavierYago/detector_de_gestos.git)
git clone [https://github.com/JavierYago/detector_de_gestos.git](https://github.com/JavierYago/detector_de_gestos.git)
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

### 🔧 Comandos (gestos → acciones)
Estos son los gestos añadidos y la acción que ejecuta el programa actualmente:

- ` [0,0,0,0,0]` (Puño cerrado): envía `Win + Down` dos veces (minimizar/mostrar escritorio según Windows).
- ` [1,1,0,0,0]` (Gesto tipo "Paz"/dos dedos): lanza Overwolf con argumentos para abrir la app (ej. CurseForge) usando `ruta_forge` + `ruta_forge_args`.
- ` [1,1,1,1,1]` (Mano abierta): envía `Alt + F4` (cerrar ventana activa).
- ` [0,1,1,0,0]` (Índice+Medio abiertos): ejecuta `ruta_brave` (lanza Brave).
- ` [0,1,0,0,0]` (Solo índice abierto): envía `Ctrl + T` (abrir nueva pestaña en navegador activo).
- ` [0,0,1,0,0]` (Solo medio abierto): envía `Win + Up` dos veces (maximizar ventana).
- ` [1,0,1,0,0]` (Pulgar + medio abiertos): envía `Alt + Tab` (cambiar ventana).

Notas:
- Existe un `cooldown` por defecto de 5 segundos para evitar ejecutar la misma acción repetidamente si mantienes el gesto.
- Overwolf/CurseForge se lanza pasando el ejecutable y una lista de argumentos; edita `ruta_forge_args` en `main.py` para cambiar el `OVERWOLF_APP_ID`.
- Estas acciones usan `pyautogui` para simular atajos de teclado; instala `pyautogui` si no está en tu entorno (`pip install pyautogui`).

### ⚙️ Personalización
Todas las acciones asociadas a cada gesto son totalmente ajustables por el usuario. Puedes editar `main.py` para:

- Cambiar qué gesto dispara cada acción (modificando las condiciones en `detectar_gesto` o las comparaciones de `estado_dedos`).
- Reemplazar las acciones actuales por cualquier otra llamada a programa, comando de `subprocess`, o combinación de `pyautogui`.
- Ajustar el `cooldown` modificando la variable `cooldown_lanzamiento`.

Consejo rápido: crea funciones separadas (por ejemplo `accion_minimizar()`, `accion_lanzar_forge()`) y llama a la función correspondiente desde el bloque donde se detecta el gesto. Así es más fácil que el "consumidor" del código cambie el comportamiento sin tocar la lógica de detección.

### 🚀 Instalación y Uso

#### 1. Requisitos Previos
Necesitas tener **Python 3.10** instalado (recomendado para compatibilidad con MediaPipe).

#### 2. Instalación Paso a Paso
```bash
# 1. Clonar el repositorio
git clone https://github.com/JavierYago/detector_de_gestos.git
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

### 🔧 Commands (gestures → actions)
The gestures added and the action the program currently executes:

- ` [0,0,0,0,0]` (Closed fist): sends `Win + Down` twice (minimize/show desktop behavior on Windows).
- ` [1,1,0,0,0]` ("Peace"/two fingers): launches Overwolf with arguments to open an app (e.g. CurseForge) using `ruta_forge` + `ruta_forge_args`.
- ` [1,1,1,1,1]` (Open hand): sends `Alt + F4` (close active window).
- ` [0,1,1,0,0]` (Index+Middle open): runs `ruta_brave` (launches Brave).
- ` [0,1,0,0,0]` (Index only): sends `Ctrl + T` (open new tab in active browser).
- ` [0,0,1,0,0]` (Middle only): sends `Win + Up` twice (maximize window).
- ` [1,0,1,0,0]` (Thumb + Middle open): sends `Alt + Tab` (switch window).

Notes:
- There is a default 5-second cooldown to avoid repeated triggers while holding a gesture.
- Overwolf/CurseForge is launched by calling the executable with a list of arguments; edit `ruta_forge_args` in `main.py` to change the `OVERWOLF_APP_ID`.
- Several actions use `pyautogui` to emulate keyboard shortcuts; install `pyautogui` if missing (`pip install pyautogui`).

### ⚙️ Customization
All actions tied to gestures are fully user-adjustable. Edit `main.py` to:

- Change which gesture triggers each action (by modifying the conditions in `detectar_gesto` or the `estado_dedos` comparisons).
- Replace current actions with any other program call, `subprocess` command, or `pyautogui` shortcut.
- Adjust the cooldown by changing the `cooldown_lanzamiento` variable.

Quick tip: implement separate functions (e.g. `accion_minimizar()`, `accion_launch_forge()`) and call them from the gesture-handling block. That makes it easy for an end user to swap behaviors without touching detection logic.

### 🚀 Installation & Usage

#### 1. Prerequisites
You need Python 3.10 installed (recommended for MediaPipe compatibility).

#### 2. Installation Steps
```bash
# 1. Clone the repository
git clone https://github.com/JavierYago/detector_de_gestos.git
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
