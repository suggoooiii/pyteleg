import asyncio
from telegram import Bot, Update
from telegram.ext import Updater, Application, CommandHandler, MessageHandler, CallbackContext, ContextTypes
from products import list_products, add_product

# Load token from environment variable
from dotenv import load_dotenv
import os

load_dotenv('.env')

bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
if not bot_token:
    raise ValueError("No bot token found in configuration file.")
# Use bot_token to set up your bot
print("Bot token is set up successfully!")

bot = Bot(token=bot_token)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Welcome to the mini app! Use /products to see our products.')

async def show_products(update: Update, context: ContextTypes.DEFAULT_TYPE):
    product_list = '\n'.join([f"{i}. {p['name']}: ${p['price']}" for i, p in enumerate(list_products())])
    await update.message.reply_text(f"Products:\n{product_list}")

async def add_product_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        name = context.args[0]
        price = float(context.args[1])
        add_product(name, price)
        await update.message.reply_text(f"Product '{name}' added successfully!")
    except (IndexError, ValueError):
        await update.message.reply_text("Usage: /addproduct <name> <price>")

def main():
    application = Application.builder().token(bot_token).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('products', show_products))
    application.add_handler(CommandHandler('addproduct', add_product_command))

    application.run_polling()

if __name__ == '__main__':
    main()