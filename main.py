import cv2
import mediapipe as mp
import subprocess
import time

# --- CONFIGURACIÓN ---
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)

ruta_brave = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
ultimo_lanzamiento = 0
cooldown_lanzamiento = 5 # segundos

# IDs de las puntas de los dedos (Índice, Medio, Anular, Meñique)
# El pulgar (4) lo tratamos aparte porque se mueve de lado.
ids_puntas = [8, 12, 16, 20]

def detectar_gesto(hand_landmarks):
    dedos = []

    # 1. Lógica para el PULGAR (Es especial porque se mueve en horizontal)
    # Comparamos la coordenada X de la punta (4) con el nudillo (3)
    # Nota: Esto asume mano derecha frente a cámara. Si usas la izquierda puede ir al revés.
    if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x:
        dedos.append(1) # Pulgar abierto
    else:
        dedos.append(0) # Pulgar cerrado

    # 2. Lógica para los 4 DEDOS restantes (Verticales)
    # Si la punta (Y) está más arriba que el nudillo inferior (Y), está abierto.
    # Recuerda: En pantalla, "Arriba" es Y=0, "Abajo" es Y=1. 
    for id_punta in ids_puntas:
        # Comparamos punta (id_punta) con el nudillo que está 2 posiciones abajo (id_punta - 2)
        if hand_landmarks.landmark[id_punta].y < hand_landmarks.landmark[id_punta - 2].y:
            dedos.append(1) # Abierto
        else:
            dedos.append(0) # Cerrado
            
    return dedos

# --- INICIO DEL PROGRAMA ---
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:

    print("¡Sistema listo! Haz gestos frente a la cámara.")
    
    while cap.isOpened():
        success, image = cap.read()
        if not success: continue

        # Preparar imagen
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image)

        # Dibujar
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # 1. DIBUJAR ESQUELETO
                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())
                
                # 2. ANALIZAR GESTO
                estado_dedos = detectar_gesto(hand_landmarks)
                
                # 3. MOSTRAR RESULTADO EN PANTALLA
                # estado_dedos será algo como [1, 1, 1, 1, 1] (Mano abierta)
                # o [0, 0, 0, 0, 0] (Puño)
                
                gesto_texto = str(estado_dedos)
                
                if estado_dedos == [0, 0, 0, 0, 0]:
                    gesto_texto = "MANO CERRADA"
                elif estado_dedos == [1, 1, 1, 1, 1]:
                    cv2.putText(image, "¡GESTO DETECTADO!", (50, 50), 
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
                elif estado_dedos == [0, 1, 1, 0, 0]:
                    cv2.putText(image, "¡GESTO DETECTADO!", (50, 50), 
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
                    tiempo_actual = time.time()
                    if tiempo_actual - ultimo_lanzamiento > cooldown_lanzamiento:
                        try:
                            subprocess.Popen(ruta_brave)
                            ultimo_lanzamiento = tiempo_actual
                        except Exception as e:
                            print(f"Error al lanzar Brave: {e}")
                    else:
                        segundos_restantes = int (cooldown_lanzamiento - (tiempo_actual - ultimo_lanzamiento))
                        cv2.putText(image, f"Espera {segundos_restantes}s", (50, 100), 
                                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                
                # Escribir texto en la imagen (posición 50, 50)
                cv2.putText(image, gesto_texto, (50, 50), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

        cv2.imshow('Detector de Gestos Pro', cv2.flip(image, 1))
        
        if cv2.waitKey(5) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()