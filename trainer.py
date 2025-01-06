import cv2
import os
import numpy as np
from utils import preprocess_image

# Directories and paths
DATASET_DIR = "dataset"
MODEL_PATH = "trained_model.yml"
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Train the recognizer
def train_recognizer():
    image_paths = []
    labels = []
    label_map = {}
    current_label = 0

    for folder_name in os.listdir(DATASET_DIR):
        folder_path = os.path.join(DATASET_DIR, folder_name)
        if os.path.isdir(folder_path):
            label_map[current_label] = folder_name
            for image_name in os.listdir(folder_path):
                image_path = os.path.join(folder_path, image_name)
                image_paths.append((image_path, current_label))
            current_label += 1

    faces = []
    labels = []
    for image_path, label in image_paths:
        gray_image = preprocess_image(image_path)
        if gray_image is not None:
            faces.append(gray_image)
            labels.append(label)

    recognizer.train(faces, np.array(labels))
    recognizer.save(MODEL_PATH)
    return label_map
