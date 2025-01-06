import os
import PySimpleGUI as sg
from trainer import train_recognizer
from recognizer import live_recognition
from dataset_manager import view_dataset

# Paths
MODEL_PATH = "trained_model.yml"

# GUI Layout
layout = [
    [sg.Text("Face Recognition System", font=("Helvetica", 25), justification="center")],
    [sg.Button("Train Recognizer"), sg.Button("Start Live Recognition")],
    [sg.Button("View Dataset"), sg.Button("Exit")]
]

# Main Window
window = sg.Window("Face Recognition System", layout)

while True:
    event, _ = window.read()

    if event in (sg.WINDOW_CLOSED, "Exit"):
        break

    # Train the model
    if event == "Train Recognizer":
        sg.popup("Training recognizer... Please wait.", title="Info")
        label_map = train_recognizer()
        sg.popup("Training completed successfully!", title="Success")

    # Live recognition
    elif event == "Start Live Recognition":
        if not os.path.exists(MODEL_PATH):
            sg.popup_error("Please train the recognizer first!")
        else:
            live_recognition(label_map)

    # View dataset
    elif event == "View Dataset":
        view_dataset()

window.close()