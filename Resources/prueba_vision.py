import cv2
import mediapipe as mp
import serial
import time

# Inicializar mediapipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Configurar la camara
cap = cv2.VideoCapture(0)
print("hola")

# Configurar la conexion serial con Arduino
arduino = serial.Serial('COM3', 9600)  # Reemplaza 'COM3' con el puerto adecuado
time.sleep(2)  # Esperar a que la conexión se establezca

# Funcion para contar los dedos levantados
def count_fingers(hand_landmarks):
    fingers = []
    tips = [8, 12, 16, 20]
    if hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x < hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].x:
        fingers.append(1)
    else:
        fingers.append(0)
    for tip in tips:
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)
    return fingers

with mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        image = cv2.flip(frame, 1)  # Invertir la imagen horizontalmente
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image_rgb.flags.writeable = False
        results = hands.process(image_rgb)
        image_rgb.flags.writeable = True
        image_bgr = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)
        
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(image_bgr, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                fingers = count_fingers(hand_landmarks)
                print(fingers)  # Imprimir el array en la consola
                # Enviar el array al Arduino
                arduino.write(bytes(fingers))
        
        cv2.imshow('Seguidor de tu mano', image_bgr)
        
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
arduino.close()