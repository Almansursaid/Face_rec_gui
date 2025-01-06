import os
import PySimpleGUI as sg

DATASET_DIR = "dataset"

def view_dataset():
    dataset_info = []

    for folder_name in os.listdir(DATASET_DIR):
        folder_path = os.path.join(DATASET_DIR, folder_name)
        if os.path.isdir(folder_path):
            num_images = len(os.listdir(folder_path))
            dataset_info.append(f"{folder_name}: {num_images} images")

    if dataset_info:
        sg.popup_scrolled("Dataset Information:", "\n".join(dataset_info), title="Dataset")
    else:
        sg.popup_error("No dataset found!")