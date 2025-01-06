import cv2
import os
import PySimpleGUI as sg
from utils import preprocess_frame

FACE_CASCADE_PATH = "haarcascade_frontalface_default.xml"
MODEL_PATH = "trained_model.yml"
face_cascade = cv2.CascadeClassifier(FACE_CASCADE_PATH)
recognizer = cv2.face.LBPHFaceRecognizer_create()

def live_recognition(label_map):
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError("Model file not found. Train the recognizer first.")
    recognizer.read(MODEL_PATH)

    cap = cv2.VideoCapture(0)
    sg.popup("Press 'Q' to exit live recognition.", title="Info")

    while True:
        ret, frame = cap.read()
        if not ret:
            sg.popup_error("Error accessing webcam!")
            break

        gray, faces = preprocess_frame(frame, face_cascade)

        for (x, y, w, h) in faces:
            face = gray[y:y + h, x:x + w]
            face = cv2.resize(face, (100, 100))
            label, confidence = recognizer.predict(face)

            if confidence < 70:
                name = label_map[label]
                color = (0, 255, 0)
            else:
                name = "Unknown"
                color = (0, 0, 255)

            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(frame, f"{name} ({int(confidence)})", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

        cv2.imshow("Live Facial Recognition", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
