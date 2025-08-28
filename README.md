# 📘 HOW-TO: Translate and Burn Captions into Your Video  
### 🧑‍💻 Personal Workflow — English & Arabic

---

## 🔹 Step 1: Prepare your files  
Place the following into the `input/` folder:
- `original.mp4` → your video file  
- `original.srt` → your original captions from Clipchamp

---

## 🔹 Step 2: Translate captions  
Double-click `run.bat`  
This will:
1. Run `translate_srt.py` to create `translated.srt` in the `output/` folder  
2. Open `translated.srt` in Notepad for review

---

## 🔹 Step 3: Review translation  
In Notepad:
- Edit any phrasing, fix spiritual references, adjust clarity  
- Save the file when done

> You stay in full control of the final wording.

---

## 🔹 Step 4: Burn captions into video  
After reviewing, press any key in the command window  
This will run `burn_captions.py` and create:
- `final_video.mp4` in the `output/` folder  
Now your video has hardcoded translated captions.

---

## ✅ Result  
Your translated video is ready to share, archive, or upload.

---

# 🗂️ Folder Structure

```
Caption-Swap-Kit/
│
├── input/
│   ├── original.mp4
│   └── original.srt
│
├── output/
│   ├── translated.srt
│   └── final_video.mp4
│
├── translate_srt.py
├── burn_captions.py
├── run.bat
└── HOW-TO.md
```

---

# 📝 Notes  
- You can change the translation language by editing `translate_srt.py`  
- You can re-run `run.bat` anytime with new videos  
- All steps are local and reproducible — no internet required after setup

---

# 📖 كيفية استخدام مجموعة تحويل الترجمة  
### 🧑‍💻 خطوات شخصية — بالعربية والإنجليزية

---

## 🔹 الخطوة ١: تجهيز الملفات  
ضع الفيديو وملف الترجمة في مجلد `input/`:
- `original.mp4` → ملف الفيديو  
- `original.srt` → ملف الترجمة الأصلي من Clipchamp

---

## 🔹 الخطوة ٢: ترجمة الترجمة  
انقر مرتين على `run.bat`  
سيقوم البرنامج بـ:
1. تشغيل `translate_srt.py` لإنشاء `translated.srt` في مجلد `output/`  
2. فتح الملف في Notepad للمراجعة

---

## 🔹 الخطوة ٣: مراجعة الترجمة  
في Notepad:
- عدّل العبارات، صحّح المعاني، أضف الدقة  
- احفظ الملف بعد الانتهاء

> أنت تتحكم بالكامل في صياغة الترجمة النهائية.

---

## 🔹 الخطوة ٤: دمج الترجمة في الفيديو  
بعد المراجعة، اضغط أي مفتاح في نافذة الأوامر  
سيتم تشغيل `burn_captions.py` وإنشاء:
- `final_video.mp4` في مجلد `output/`  
الآن الفيديو يحتوي على ترجمة مدمجة.

---

## ✅ النتيجة  
الفيديو النهائي جاهز للمشاركة أو الحفظ أو النشر.
