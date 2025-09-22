import os
import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# Enable logging for debugging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Get bot token from environment variable
TOKEN = os.getenv("BOT_TOKEN")

# Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["📊 Live History", "📜 Full History"],
        ["Win/Loss History", "Download History"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "👋 Welcome to the Bot!\nChoose an option below:",
        reply_markup=reply_markup
    )

# Handle text messages (buttons)
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if "Live History" in text:
        await update.message.reply_text(
            "📊 Live History\n\n"
            "1️⃣ Round: 12345 | Big/Small: Big | Number: 8 | Color: 🔴 Red\n"
            "2️⃣ Round: 12344 | Big/Small: Small | Number: 2 | Color: ⚫ Black\n"
            "3️⃣ Round: 12343 | Big/Small: Big | Number: 9 | Color: 🔴 Red\n"
            "4️⃣ Round: 12342 | Big/Small: Small | Number: 1 | Color: 🟢 Green\n"
            "5️⃣ Round: 12341 | Big/Small: Big | Number: 7 | Color: 🔴 Red"
        )

    elif "Full History" in text:
        await update.message.reply_text(
            "📜 Full History\n\n"
            "Showing last 50 rounds from API (demo):\n"
            "1️⃣ Round: 12345 | Big/Small: Big | Number: 8 | Color: 🔴 Red\n"
            "...\n"
            "50️⃣ Round: 12296 | Big/Small: Small | Number: 3 | Color: ⚫ Black"
        )

    else:
        await update.message.reply_text("❌ Unknown option. Please use the buttons.")

# Main function
async def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
