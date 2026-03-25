# 🚀 تعليمات إعداد البوت v2 — Final Exam Bot

## الخطوة 1 — إنشاء بوت جديد في تلغرام
1. افتح تلغرام وابحث عن @BotFather
2. أرسل `/newbot`
3. اختر اسم للبوت مثل: `Microbiology Final Bot`
4. اختر username مثل: `micro_final_2026_bot`
5. احفظ التوكن الذي يعطيك إياه ✅

## الخطوة 2 — إنشاء Repository على GitHub
1. افتح github.com → New repository
2. اسم المستودع: `micro-final-bot`
3. اختر **Private** ← Create repository ✅
4. ارفع هذه الملفات (غيّر _v2 من الاسم):
   - `bot_v2.py` → `bot.py`
   - `database_v2.py` → `database.py`
   - `dashboard_v2.py` → `dashboard.py`
   - `run_v2.py` → `run.py`
   - `populate_db_v2.py` → `populate_db.py`
   - `Procfile_v2` → `Procfile`
   - `requirements_v2.txt` → `requirements.txt`
   - `runtime_v2.txt` → `runtime.txt`

## الخطوة 3 — إعداد Railway
1. افتح railway.app → New Project
2. اختر **Deploy from GitHub repo** → اختر المستودع
3. أضف **Volume**:
   - اضغط New → Volume
   - Mount Path: `/data`
4. أضف **Variables**:
   | Name | Value |
   |------|-------|
   | `BOT_TOKEN` | التوكن من BotFather |
   | `TEACHER_CHAT_ID` | الـ ID تبعك (احصل عليه بـ /myid) |
   | `DASH_PASSWORD` | كلمة مرور الداشبورد (اختر ما تريد) |

5. غيّر **Start Command** إلى:
   ```
   python populate_db.py && python run.py
   ```
6. أضف **Public Networking**:
   - Settings → Public Networking → Generate Domain
   - Port: `8090`

## الخطوة 4 — احصل على TEACHER_CHAT_ID
1. بعد رفع البوت وتشغيله
2. افتح البوت في تلغرام
3. أرسل `/myid`
4. انسخ الرقم وضعه في Railway Variables

## الخطوة 5 — تشغيل أول مرة
1. بعد أول deploy شتغل ← الـ Logs يظهر:
   ```
   ✅ تم إضافة 50 سؤال
   Bot v2 started ✅
   ```
2. غيّر Start Command إلى:
   ```
   python run.py
   ```
   (لتجنب تصفير الأسئلة في كل restart)

## الخطوة 6 — تجربة البوت
1. افتح البوت في تلغرام
2. أرسل `/start`
3. اكتب اسمك
4. ابدأ الاختبار!

## رابط الداشبورد
`https://اسم-مشروعك.up.railway.app`
كلمة المرور: ما وضعته في DASH_PASSWORD

## إضافة أسئلة جديدة
أرسل الأسئلة وسيتم إنشاء ملف خاص بها
