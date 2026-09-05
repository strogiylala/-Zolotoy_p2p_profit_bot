import os
import telebot

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "🔥 ZOLOTOY P2P BOT\n\n"
        "Бот запущений.\n\n"
        "💰 Баланс — встановити баланс\n"
        "🔥 ДАЙ СПРЕДИ — пошук спредів\n"
        "⚙️ Налаштування — налаштування"
    )


@bot.message_handler(commands=["balance"])
def balance(message):
    bot.send_message(
        message.chat.id,
        "💰 Напиши свій баланс у USDT.\n\n"
        "Наприклад:\n"
        "1000"
    )


@bot.message_handler(commands=["spread"])
def spread(message):
    bot.send_message(
        message.chat.id,
        "🔥 Модуль пошуку спредів поки налаштовується.\n\n"
        "Підключимо:\n"
        "• Bybit\n"
        "• Binance\n"
        "• MEXC\n"
        "• Gate"
    )


@bot.message_handler(commands=["settings"])
def settings(message):
    bot.send_message(
        message.chat.id,
        "⚙️ НАЛАШТУВАННЯ\n\n"
        "Монета: USDT\n"
        "Валюта: UAH\n"
        "Біржі: Bybit / Binance / MEXC / Gate"
    )


print("ZOLOTOY P2P BOT STARTED")

bot.infinity_polling()