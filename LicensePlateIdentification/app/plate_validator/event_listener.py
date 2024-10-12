import cv2
import numpy as np
import requests
import pytesseract
import asyncio
from ultralytics import YOLO


model = YOLO('object_detection/models/license_plate_detector.onnx')

def capture_image():
    
    url = 'http://<phone_ip>:8080/shot.jpg'
    
    img_resp = requests.get(url)
    
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    
    img = cv2.imdecode(img_arr, -1)
    
    return img

def detect_license_plate(image):
    
    results = model(image)
    
    plates = results.pandas().xyxy[0]  

    if len(plates) > 0:
    
        for index, row in plates.iterrows():
    
            if row['name'] == 'license_plate':
    
                x1, y1, x2, y2 = int(row['xmin']), int(row['ymin']), int(row['xmax']), int(row['ymax'])
    
                return image[y1:y2, x1:x2]

    return None

def read_plate(image):
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    ret, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    
    plate_text = pytesseract.image_to_string(thresh, config='--psm 8')
    
    return plate_text.strip()

async def check_plate(plate_number):
    
    url = "http://localhost:8000/check_plate/"
    
    response = requests.post(url, json={"plate_number": plate_number})
    
    return response.json()

async def event_listener():
    while True:

        image = capture_image()
        
        plate_image = detect_license_plate(image)
        
        if plate_image is not None:
        
            plate_number = read_plate(plate_image)
        
            if plate_number:
        
                print(f"Detected plate: {plate_number}")
        
                try:
        
                    response = await check_plate(plate_number)
        
                    print(f"Response: {response}")
        
                except requests.exceptions.RequestException as e:
        
                    print(f"Request failed: {e}")
        else:
        
            print("No license plate detected.")
        
        await asyncio.sleep(1)
