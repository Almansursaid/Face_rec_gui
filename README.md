# Face Recognition GUI Project

This project is a Python-based face recognition system with a user-friendly GUI built using PySimpleGUI and OpenCV. It provides features for training a face recognition model, recognizing faces in real-time, and managing datasets. The system ensures effective face recognition by using LBPH (Local Binary Patterns Histogram) recognizer and follows robust preprocessing techniques.

---

## Features

### 1. Train Recognizer
- Trains the LBPH recognizer on a dataset of face images.
- Ensures that each person has at least 20 images in the dataset for effective training.

### 2. Live Recognition
- Uses a live webcam feed to recognize faces in real-time.
- Matches the detected face with the closest one in the dataset using LBPH.
- Displays the name of the recognized person on the video feed.

### 3. View Dataset
- Provides an overview of the dataset, including the number of images per person.
- Ensures dataset completeness and structure.

### 4. Error Handling
- Handles missing models, insufficient dataset images, and webcam access issues gracefully.
- Provides detailed error messages for troubleshooting.

---

## How It Works

1. **Dataset Preparation**:
   - For each person, the system expects a folder containing at least 20 images in the `dataset/` directory.
   - During training, it preprocesses images:
     - Detects faces using Haar Cascade.
     - Trims unnecessary parts of the image.
     - Applies histogram equalization.
     - Resizes images to 100x100 pixels.

2. **Training the Model**:
   - Uses the LBPH recognizer to train a face recognition model on the dataset.
   - Saves the trained model as `trained_model.yml`.

3. **Live Recognition**:
   - Detects faces in a live webcam feed.
   - Preprocesses each detected face as done during training.
   - Matches the face to the closest likeness in the dataset using a confidence threshold.

---

## Requirements

### Software
- Python 3.8 or later
- GitHub Desktop (for version control)

### Python Libraries
Install the required Python libraries using:
```bash
pip install -r requirements.txt
