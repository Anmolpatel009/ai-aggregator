import numpy as np
import pandas as pd
import cv2
import torch
from ultralytics import YOLO

print("✅ NumPy version:", np.__version__)
print("✅ Pandas version:", pd.__version__)
print("✅ OpenCV version:", cv2.__version__)
print("✅ PyTorch version:", torch.__version__)
print("✅ CUDA available:", torch.cuda.is_available())

# Load YOLOv8 small model
model = YOLO('yolov8n.pt')
print("✅ YOLOv8 model loaded successfully")
