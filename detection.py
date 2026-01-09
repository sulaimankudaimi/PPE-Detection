import cv2
from ultralytics import YOLO

# استخدام مسار نسبي ليعمل على أي جهاز أو سحابة
model = YOLO("best.pt") 

cap = cv2.VideoCapture(0)
while cap.isOpened():
    success, frame = cap.read()
    if success:
        results = model(frame, conf=0.4, imgsz=320)
        annotated_frame = results[0].plot()
        cv2.imshow("YOLOv8 Detection", annotated_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
