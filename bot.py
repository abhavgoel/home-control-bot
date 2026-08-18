import os

from dotenv import load_dotenv
from wakeonlan import send_magic_packet
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from pywizlight import wizlight, PilotBuilder

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
PC_MAC_ADDRESS = os.getenv("PC_MAC_ADDRESS")
LIGHT_IP = os.getenv("LIGHT_IP")


if not BOT_TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN is not set in .env")

if not PC_MAC_ADDRESS:
    raise ValueError("PC_MAC_ADDRESS is not set in .env")

light = wizlight(LIGHT_IP)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏠 Geol's Home Bot\n\n"
        "/wake - Wake PC\n"
    )

async def wake_pc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    send_magic_packet(PC_MAC_ADDRESS)

    await update.message.reply_text(
        "PC should be waking up shortly..."
)

async def turn_light_on():
    await light.turn_on(PilotBuilder(
        scene=6 #Scene Cozy in Wiz app
    ))

async def im_home(update: Update, context: ContextTypes.DEFAULT_TYPE):
    send_magic_packet(PC_MAC_ADDRESS)
    await turn_light_on()

    await update.message.reply_text(
        "⚡ Setup activated!\n\n"
        "🖥️ PC → Waking\n"
        "💡 Light → ON"
    )


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("wake_pc", wake_pc))
    app.add_handler(CommandHandler("im_home", im_home))

    print("Bot running...")
    app.run_polling()


if __name__ == "__main__":
    main()