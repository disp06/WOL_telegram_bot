import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from wakeonlan import send_magic_packet

# Настройки
BOT_TOKEN = "token"  # Example: "123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11"
ALLOWED_CHAT_IDS = [YOUR_CHAT_ID]  # Example: [123456789]

# Логирование
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

async def wol(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_chat.id
    if user_id not in ALLOWED_CHAT_IDS:
        await update.message.reply_text("🚫 Access Denied!")
        return

    mac = context.args[0] if context.args else None
    if not mac:
        await update.message.reply_text("❌ Enter MAC: /wol AA:BB:CC:DD:EE:FF")
        return

    try:
        send_magic_packet(mac)
        await update.message.reply_text(f"⚡ I wake up the device: {mac}")
    except Exception as e:
        await update.message.reply_text(f"⚠️ Error: {str(e)}")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("wol", wol))
    app.run_polling()

if __name__ == "__main__":
    main()
