#!/usr/bin/env python3
"""
Telegram Bot → Prime Agent Bridge
"""
import subprocess, sys, os
from pathlib import Path

TOKEN = "8273024811:AAGKSGbfcF-nQhzyX06rUDelEm1bRbmySbE"

# Nainštaluj ak treba
try:
    from telegram import Update
    from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
except ImportError:
    subprocess.run([sys.executable, "-m", "pip", "install", "python-telegram-bot[job-queue]"], check=True)
    from telegram import Update
    from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

async def start(update: Update, context):
    await update.message.reply_text(
        "🤖 Marianov Prime Agent je pripravený!\n\n"
        "Pošli mi správu a ja ti odpoviem.\n\n"
        "💡 Skús:\n"
        "• vygeneruj LinkedIn post o AI agentoch\n"
        "• vytvor twitter thread o automatizácii\n"
        "• sprav prieskum konkurencie"
    )

async def handle_message(update: Update, context):
    user_msg = update.message.text
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")

    try:
        result = subprocess.run(
            ["prime-agent", "--print", "--continue", user_msg],
            capture_output=True, text=True, timeout=120,
            cwd=str(Path.home() / "Developer"),
            env={**os.environ, "NO_COLOR": "1"}
        )
        response = (result.stdout or result.stderr).strip()[:4000]
        if not response:
            response = "🤔 Bez odpovede. Skús znova."

        await update.message.reply_text(f"🤖 {response}")
    except subprocess.TimeoutExpired:
        await update.message.reply_text("⏰ Trvá to dlho... skús kratšiu otázku.")
    except Exception as e:
        await update.message.reply_text(f"❌ Chyba: {str(e)[:500]}")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Bot beží! Nájdi ho na Telegrame: @MarianPrimeAgentBot")
    print("   Pošli /start a skús správu!")
    app.run_polling()

if __name__ == "__main__":
    main()
