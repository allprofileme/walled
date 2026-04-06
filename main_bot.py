import os
import telebot
import subprocess

# جلب التوكن من متغيرات البيئة (سنضبطه في إعدادات GitHub)
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "🤖 أهلاً بك! البوت متصل الآن.\nاستخدم أمر /run لتشغيل أداة السبام.")

@bot.message_handler(commands=['run'])
def execute_tool(message):
    bot.reply_to(message, "⏳ جاري تشغيل الأداة على خوادم GitHub...")
    try:
        # تشغيل ملف الأداة المشفرة الخاص بك
        result = subprocess.run(['python', 'سبام تليجرام.py_Enc.py'], capture_output=True, text=True)
        
        if result.stdout:
            bot.send_message(message.chat.id, f"✅ تم التنفيذ:\n{result.stdout}")
        else:
            bot.send_message(message.chat.id, "✅ تم التنفيذ بنجاح.")
    except Exception as e:
        bot.reply_to(message, f"❌ حدث خطأ: {str(e)}")

print("Bot is running...")
bot.polling()

