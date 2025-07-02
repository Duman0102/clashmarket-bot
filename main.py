from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Telegram BotFather-ден алынған токен (қазір ашық түрде қалдыра бер, кейін .env қыламыз)
TOKEN = "7696013475:AAGWWevcauSO-8DhC77h7jx8dWoQDC-lKbs"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    buttons = [["🛒 Каталог", "📢 Жарнама"], ["⚠️ Ескерту"]]
    markup = ReplyKeyboardMarkup(buttons, resize_keyboard=True)
    await update.message.reply_text(
        f"Қош келдің, {user.first_name}!\nБұл Clash of Clans аккаунт бот 👑",
        reply_markup=markup
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "🛒 Каталог":
        await update.message.reply_photo(
            photo="https://i.imgur.com/YLUqYMb.jpeg",
            caption="📦 TH15 Max\n💰 10$\n✉️ @admin_kz"
        )
        await update.message.reply_photo(
            photo="https://i.imgur.com/5sMQ96m.jpeg",
            caption="📦 TH13 Full Hero\n💰 5$\n✉️ @admin_kz"
        )
    elif text == "📢 Жарнама":
        await update.message.reply_text("📢 Жарнама беру үшін: @admin_kz")
    elif text == "⚠️ Ескерту":
        await update.message.reply_text("❗Барлық аккаунттар үшін жауапкершілік сатушыда.")
    else:
        await update.message.reply_text("Төмендегі батырмаларды қолданыңыз 👇")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == "__main__":
    main()
