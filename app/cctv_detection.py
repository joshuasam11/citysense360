import tempfile
import cv2
from ultralytics import YOLO
import os

model = YOLO("yolov8n.pt")

def run_detection(uploaded_file):
    # get extension (.jpg, .png, etc)
    _, ext = os.path.splitext(uploaded_file.name)

    # save file with correct extension
    with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as tmp:
        tmp.write(uploaded_file.read())
        temp_path = tmp.name

    results = model(temp_path)
    annotated = results[0].plot()

    return annotated
