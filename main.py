import os
import asyncio
from aiohttp import web
from telegram import Bot
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

BOT_TOKEN = "8911212441:AAGoJPPURWyQHoxdnKjSScjRz8nu5DEr4ls"
PORT = int(os.environ.get("PORT", 8080))
SERVER_URL = "https://palki-stream-bot.onrender.com"

def start(update, context):
    update.message.reply_text("স্বাগতম! আমাকে যেকোনো মুভি বা ফাইল ফরওয়ার্ড করো, আমি ডিরেক্ট প্লেব্যাক লিংক তৈরি করে দেব।")

def generate_link(update, context):
    message = update.message
    file_id = ""
    
    if message.video:
        file_id = message.video.file_id
    elif message.document:
        file_id = message.document.file_id
    elif message.audio:
        file_id = message.audio.file_id
        
    if file_id:
        direct_link = f"{SERVER_URL}/file/{file_id}"
        message.reply_text(f"তোমার মুভির ডিরেক্ট লিংক:\n{direct_link}")

async def handle_root(request):
    return web.Response(text="Palki Stream Bot is running perfectly!")

async def start_server():
    server = web.Application()
    server.router.add_get("/", handle_root)
    runner = web.AppRunner(server)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", PORT)
    await site.start()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_server())
    
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.video | Filters.document | Filters.audio, generate_link))
    
    updater.start_polling()
    updater.idle()
    
