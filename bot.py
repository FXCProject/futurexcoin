from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "7711233839:AAFnU89KQ8d2XTyOM3-_jCzDtvf0yd9JvAU"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
keyboard = [
[InlineKeyboardButton("Get My Invite Link", callback_data='invite')],
[InlineKeyboardButton("My Score", callback_data='score')],
[InlineKeyboardButton("Tasks", callback_data='tasks')]
]
reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Welcome to the Future X Airdrop!", reply_markup=reply_markup)

    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
