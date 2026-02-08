import mediapipe
import os

print("--- REPORTE DE DIAGNÓSTICO ---")
print(f"1. Ubicación del archivo importado: {mediapipe.__file__}")
print(f"2. Contenido de la carpeta: {os.listdir(os.path.dirname(mediapipe.__file__))}")
print(f"3. ¿Existe 'solutions'? {'solutions' in dir(mediapipe)}")
print("------------------------------")