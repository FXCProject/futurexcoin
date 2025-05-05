from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "7711233839:AAFnU89KQ8d2XTyOM3-_jCzDtvf0yd9JvAU"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Start Game", callback_data='start_game')],
        [InlineKeyboardButton("Get My Invite Link", callback_data='invite')]
]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Welcome to the Future X Airdrop!", reply_markup=reply_markup)

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
