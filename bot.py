import asyncio
from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext
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

def start(update: Update, context: CallbackContext):
    update.message.reply_text('Welcome to the mini app! Use /products to see our products.')

def show_products(update: Update, context: CallbackContext):
    product_list = '\n'.join([f"{i}. {p['name']}: ${p['price']}" for i, p in enumerate(list_products())])
    update.message.reply_text(f"Products:\n{product_list}")

def add_product_command(update: Update, context: CallbackContext):
    try:
        name = context.args[0]
        price = float(context.args[1])
        add_product(name, price)
        update.message.reply_text(f"Product '{name}' added successfully!")
    except (IndexError, ValueError):
        update.message.reply_text("Usage: /addproduct <name> <price>")

# Create an asyncio.Queue instance for the update_queue
update_queue = asyncio.Queue()
updater = Updater(bot_token,update_queue)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('products', show_products))
dispatcher.add_handler(CommandHandler('addproduct', add_product_command))

updater.start_polling()