import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# লগিং সেটআপ
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# আপনার BotFather থেকে পাওয়া টোকেনটি এখানে বসাবেন
TOKEN = "YOUR_BOT_TOKEN_HERE"

async def handle_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # ব্যবহারকারী ভিডিও পাঠিয়েছে কিনা চেক করা
    video = update.message.video or update.message.document
    
    if not video:
        await update.message.reply_text("দয়া করে একটি ভিডিও ফাইল পাঠান।")
        return

    await update.message.reply_text("ভিডিওটি প্রসেস করা হচ্ছে, একটু অপেক্ষা করুন...")

    # টেলিগ্রাম ফাইল অবজেক্ট রিট্রিভ করা
    file = await context.bot.get_file(video.file_id)
    
    # টেলিগ্রামের নিজস্ব ফাইল ডাউনলোড লিংক
    file_url = file.file_path
    
    # রেসপন্স লিংক পাঠানো
    response_text = (
        "✅ **আপনার ভিডিও লিংক তৈরি হয়ে গেছে!**\n\n"
        f"📥 **ডাউনলোড/ভিউ লিংক:**\n{file_url}\n\n"
        "🔗 এই লিংকটি আপনি এখন অন্য কারো সাথে শেয়ার করতে পারেন।"
    )
    
    await update.message.reply_text(response_text, parse_mode="Markdown")

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()

    # শুধুমাত্র ভিডিও বা ডকুমেন্ট ফাইল হ্যান্ডেল করার জন্য ফিল্টার
    application.add_handler(MessageHandler(filters.VIDEO | filters.Document.VIDEO, handle_video))

    print("বট সফলভাবে রান হচ্ছে...")
    application.run_polling()
  
