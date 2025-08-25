import cv2
from ultralytics import YOLO
import time
import numpy as np
from datetime import datetime
import os

class ObjectDetector:
    def __init__(self, model_path='best.pt'):
        self.model = YOLO(model_path)
        self.conf_threshold = 0.6
        self.img_size = 640
        
        # Klasör oluşturma
        self.save_dir = 'detections'
        if not os.path.exists(self.save_dir):
            os.makedirs(self.save_dir)
            os.makedirs(os.path.join(self.save_dir, 'screenshots'))
            os.makedirs(os.path.join(self.save_dir, 'videos'))

    def process_frame(self, frame, results):
        # FPS hesaplama
        current_time = time.time()
        fps = int(1 / (current_time - self.prev_time))
        self.prev_time = current_time
        
        # Tespit edilen nesnelerin sayısını tutma
        detections = {'person': 0, 'car': 0, 'animal': 0}
        
        # Tespitleri işleme
        for r in results:
            boxes = r.boxes
            for box in boxes:
                # Koordinatlar
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                
                # Güven skoru
                conf = box.conf[0]
                
                # Sınıf
                cls = int(box.cls[0])
                class_name = self.model.names[cls]
                
                # Nesne sayısını güncelleme
                if class_name in detections:
                    detections[class_name] += 1
                
                # Çerçeve çizme
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                
                # Etiket oluşturma
                label = f'{class_name} {conf:.2f}'
                t_size = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2)[0]
                cv2.rectangle(frame, (x1, y1-t_size[1]-3), (x1+t_size[0], y1), (0, 255, 0), -1)
                cv2.putText(frame, label, (x1, y1-2), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
        
        # FPS ve tespit sayılarını gösterme
        info_text = f'FPS: {fps}'
        for obj, count in detections.items():
            info_text += f' | {obj}: {count}'
        cv2.putText(frame, info_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
        return frame

    def capture_screenshot(self, frame):
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = os.path.join(self.save_dir, 'screenshots', f'detection_{timestamp}.jpg')
        cv2.imwrite(filename, frame)
        print(f'Ekran görüntüsü kaydedildi: {filename}')

    def start_detection(self, source=0):
        self.prev_time = time.time()
        
        # Video kaynağını ayarlama
        if isinstance(source, str) and (source.endswith('.mp4') or source.endswith('.avi')):
            cap = cv2.VideoCapture(source)
            is_video = True
        else:
            cap = cv2.VideoCapture(source)  # Webcam için
            is_video = False
        
        # Video kayıt ayarları
        if is_video:
            output_path = os.path.join(self.save_dir, 'videos', 'output_video.mp4')
            frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            fps = int(cap.get(cv2.CAP_PROP_FPS))
            out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height))
        
        print("Kontroller:")
        print("'q' - Çıkış")
        print("'s' - Ekran görüntüsü alma")
        print("'+' - Güven eşiğini artırma")
        print("'-' - Güven eşiğini azaltma")
        
        while cap.isOpened():
            success, frame = cap.read()
            if not success:
                break
            
            # YOLO tespiti
            results = self.model.predict(frame, imgsz=self.img_size, conf=self.conf_threshold)
            
            # Frame'i işleme
            processed_frame = self.process_frame(frame, results)
            
            # Görüntüyü gösterme
            cv2.imshow('Object Detection', processed_frame)
            
            # Video kaydetme
            if is_video:
                out.write(processed_frame)
            
            # Tuş kontrolleri
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
            elif key == ord('s'):
                self.capture_screenshot(processed_frame)
            elif key == ord('+') and self.conf_threshold < 0.95:
                self.conf_threshold += 0.05
                print(f'Güven eşiği artırıldı: {self.conf_threshold:.2f}')
            elif key == ord('-') and self.conf_threshold > 0.1:
                self.conf_threshold -= 0.05
                print(f'Güven eşiği azaltıldı: {self.conf_threshold:.2f}')
        
        # Temizlik
        cap.release()
        if is_video:
            out.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    detector = ObjectDetector()
    
    # Kaynak seçimi (0: webcam, "video.mp4": video dosyası)
    source = 0  # Webcam için
    # source = "path/to/your/video.mp4"  # Video dosyası için
    
    detector.start_detection(source)
