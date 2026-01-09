import cv2
from ultralytics import YOLO
import matplotlib.pyplot as plt

# 1. تحميل الموديل (استخدام الاسم المباشر طالما الملف بجانبه في GitHub)
model = YOLO("best.pt")

# 2. إجراء التنبؤ 
# ملاحظة: استبدل 'test.jpg' باسم أي صورة موجودة فعلياً في مستودعك
image_path = "test.jpg" 
results = model.predict(source=image_path, conf=0.25)

# 3. معالجة وعرض النتيجة
res_plotted = results[0].plot()

# تحويل الألوان للعرض الصحيح باستخدام Matplotlib
plt.figure(figsize=(12, 8))
plt.imshow(cv2.cvtColor(res_plotted, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title("نتائج فحص معدات السلامة - SPC")
plt.show()
