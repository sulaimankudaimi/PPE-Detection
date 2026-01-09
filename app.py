{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "ff93f815-b5b4-45c4-8265-602a166630ca",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2026-01-09 11:19:26.657 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "MarkdownMixin.markdown() got an unexpected keyword argument 'unsafe_allow_index'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mTypeError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 11\u001b[39m\n\u001b[32m      8\u001b[39m st.set_page_config(page_title=\u001b[33m\"\u001b[39m\u001b[33mSafeDrill AI - PPE Monitoring\u001b[39m\u001b[33m\"\u001b[39m, page_icon=\u001b[33m\"\u001b[39m\u001b[33m🏗️\u001b[39m\u001b[33m\"\u001b[39m, layout=\u001b[33m\"\u001b[39m\u001b[33mwide\u001b[39m\u001b[33m\"\u001b[39m)\n\u001b[32m     10\u001b[39m \u001b[38;5;66;03m# تصميم CSS مخصص لجعل الواجهة أنيقة\u001b[39;00m\n\u001b[32m---> \u001b[39m\u001b[32m11\u001b[39m \u001b[43mst\u001b[49m\u001b[43m.\u001b[49m\u001b[43mmarkdown\u001b[49m\u001b[43m(\u001b[49m\u001b[33;43m\"\"\"\u001b[39;49m\n\u001b[32m     12\u001b[39m \u001b[33;43m    <style>\u001b[39;49m\n\u001b[32m     13\u001b[39m \u001b[33;43m    .main \u001b[39;49m\u001b[33;43m{\u001b[39;49m\n\u001b[32m     14\u001b[39m \u001b[33;43m        background-color: #f5f7f9;\u001b[39;49m\n\u001b[32m     15\u001b[39m \u001b[33;43m    }\u001b[39;49m\n\u001b[32m     16\u001b[39m \u001b[33;43m    .stTitle \u001b[39;49m\u001b[33;43m{\u001b[39;49m\n\u001b[32m     17\u001b[39m \u001b[33;43m        color: #1e3a8a;\u001b[39;49m\n\u001b[32m     18\u001b[39m \u001b[33;43m        font-family: \u001b[39;49m\u001b[33;43m'\u001b[39;49m\u001b[33;43mHelvetica Neue\u001b[39;49m\u001b[33;43m'\u001b[39;49m\u001b[33;43m, sans-serif;\u001b[39;49m\n\u001b[32m     19\u001b[39m \u001b[33;43m    }\u001b[39;49m\n\u001b[32m     20\u001b[39m \u001b[33;43m    .status-box \u001b[39;49m\u001b[33;43m{\u001b[39;49m\n\u001b[32m     21\u001b[39m \u001b[33;43m        padding: 20px;\u001b[39;49m\n\u001b[32m     22\u001b[39m \u001b[33;43m        border-radius: 10px;\u001b[39;49m\n\u001b[32m     23\u001b[39m \u001b[33;43m        background-color: #ffffff;\u001b[39;49m\n\u001b[32m     24\u001b[39m \u001b[33;43m        box-shadow: 0 4px 6px rgba(0,0,0,0.1);\u001b[39;49m\n\u001b[32m     25\u001b[39m \u001b[33;43m        margin-bottom: 20px;\u001b[39;49m\n\u001b[32m     26\u001b[39m \u001b[33;43m    }\u001b[39;49m\n\u001b[32m     27\u001b[39m \u001b[33;43m    </style>\u001b[39;49m\n\u001b[32m     28\u001b[39m \u001b[33;43m    \u001b[39;49m\u001b[33;43m\"\"\"\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43munsafe_allow_index\u001b[49m\u001b[43m=\u001b[49m\u001b[38;5;28;43;01mTrue\u001b[39;49;00m\u001b[43m)\u001b[49m\n\u001b[32m     30\u001b[39m \u001b[38;5;66;03m# العنوان الجانبي\u001b[39;00m\n\u001b[32m     31\u001b[39m \u001b[38;5;28;01mwith\u001b[39;00m st.sidebar:\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\streamlit\\runtime\\metrics_util.py:531\u001b[39m, in \u001b[36mgather_metrics.<locals>.wrapped_func\u001b[39m\u001b[34m(*args, **kwargs)\u001b[39m\n\u001b[32m    529\u001b[39m         _LOGGER.debug(\u001b[33m\"\u001b[39m\u001b[33mFailed to collect command telemetry\u001b[39m\u001b[33m\"\u001b[39m, exc_info=ex)\n\u001b[32m    530\u001b[39m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[32m--> \u001b[39m\u001b[32m531\u001b[39m     result = \u001b[43mnon_optional_func\u001b[49m\u001b[43m(\u001b[49m\u001b[43m*\u001b[49m\u001b[43margs\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43m*\u001b[49m\u001b[43m*\u001b[49m\u001b[43mkwargs\u001b[49m\u001b[43m)\u001b[49m\n\u001b[32m    532\u001b[39m \u001b[38;5;28;01mexcept\u001b[39;00m RerunException:\n\u001b[32m    533\u001b[39m     \u001b[38;5;66;03m# Duplicated from below, because static analysis tools get confused\u001b[39;00m\n\u001b[32m    534\u001b[39m     \u001b[38;5;66;03m# by deferring the rethrow.\u001b[39;00m\n\u001b[32m    535\u001b[39m     \u001b[38;5;28;01mif\u001b[39;00m tracking_activated \u001b[38;5;129;01mand\u001b[39;00m command_telemetry:\n",
      "\u001b[31mTypeError\u001b[39m: MarkdownMixin.markdown() got an unexpected keyword argument 'unsafe_allow_index'"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "from ultralytics import YOLO\n",
    "import cv2\n",
    "import numpy as np\n",
    "from PIL import Image\n",
    "\n",
    "# إعدادات الصفحة (تظهر في تبويب المتصفح)\n",
    "st.set_page_config(page_title=\"SafeDrill AI - PPE Monitoring\", page_icon=\"🏗️\", layout=\"wide\")\n",
    "\n",
    "# تصميم CSS مخصص لجعل الواجهة أنيقة\n",
    "st.markdown(\"\"\"\n",
    "    <style>\n",
    "    .main {\n",
    "        background-color: #f5f7f9;\n",
    "    }\n",
    "    .stTitle {\n",
    "        color: #1e3a8a;\n",
    "        font-family: 'Helvetica Neue', sans-serif;\n",
    "    }\n",
    "    .status-box {\n",
    "        padding: 20px;\n",
    "        border-radius: 10px;\n",
    "        background-color: #ffffff;\n",
    "        box-shadow: 0 4px 6px rgba(0,0,0,0.1);\n",
    "        margin-bottom: 20px;\n",
    "    }\n",
    "    </style>\n",
    "    \"\"\", unsafe_allow_index=True)\n",
    "\n",
    "# العنوان الجانبي\n",
    "with st.sidebar:\n",
    "    st.image(\"https://img.icons8.com/fluency/96/worker-with-road-cones.png\")\n",
    "    st.title(\"إعدادات النظام\")\n",
    "    conf_threshold = st.slider(\"عتبة الثقة (Confidence)\", 0.0, 1.0, 0.45)\n",
    "    st.info(\"هذا النظام مدعوم بتقنيات YOLOv8 لمراقبة السلامة المهنية في SPC.\")\n",
    "\n",
    "# العنوان الرئيسي\n",
    "st.title(\"🏗️ SafeDrill AI Pro: نظام مراقبة السلامة الذكي\")\n",
    "st.write(\"تحليل فوري لصور ومعدات الوقاية الشخصية في المواقع النفطية.\")\n",
    "\n",
    "# تحميل الموديل (تم استخدام ملف best.pt الخاص بك)\n",
    "@st.cache_resource\n",
    "def load_model():\n",
    "    return YOLO(\"weights/best.pt\")\n",
    "\n",
    "model = load_model()\n",
    "\n",
    "# تقسيم الصفحة إلى أعمدة\n",
    "col1, col2 = st.columns([1, 1])\n",
    "\n",
    "with col1:\n",
    "    st.subheader(\"📤 رفع الصورة للفحص\")\n",
    "    uploaded_file = st.file_uploader(\"اختر صورة من الموقع...\", type=['jpg', 'jpeg', 'png'])\n",
    "\n",
    "if uploaded_file is not None:\n",
    "    # معالجة الصورة\n",
    "    image = Image.open(uploaded_file)\n",
    "    img_array = np.array(image)\n",
    "    \n",
    "    # إجراء التنبؤ\n",
    "    results = model.predict(source=img_array, conf=conf_threshold)\n",
    "    \n",
    "    # رسم النتائج\n",
    "    res_plotted = results[0].plot()\n",
    "    \n",
    "    with col1:\n",
    "        st.image(image, caption=\"الصورة الأصلية\", use_column_width=True)\n",
    "        \n",
    "    with col2:\n",
    "        st.subheader(\"🔍 نتائج التحليل الذكي\")\n",
    "        st.image(res_plotted, caption=\"النتائج المكتشفة\", use_column_width=True)\n",
    "        \n",
    "        # عرض إحصائيات سريعة\n",
    "        st.markdown(\"<div class='status-box'>\", unsafe_allow_html=True)\n",
    "        st.write(\"### ملخص الكشف:\")\n",
    "        count = len(results[0].boxes)\n",
    "        st.success(f\"تم اكتشاف {count} عناصر في الموقع.\")\n",
    "        st.markdown(\"</div>\", unsafe_allow_index=True)\n",
    "\n",
    "else:\n",
    "    with col2:\n",
    "        st.info(\"في انتظار رفع صورة لبدء التحليل...\")\n",
    "        # يمكنك وضع صورة توضيحية هنا"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e331edfb-6eee-4e51-ba4f-ae5a158f6efd",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
