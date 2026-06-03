import os
from pyrogram import Client, filters
from pyrogram.types import Message

API_ID = 38551568
API_HASH = "96164399da97ec3aedb1d4572cb1c950"
BOT_TOKEN = "8911212441:AAGoJPPURWyQHoxdnKjSScjRz8nu5DEr4ls"

app = Client("palki_stream_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

PORT = int(os.environ.get("PORT", 8080))
SERVER_URL = os.environ.get("SERVER_URL", "https://palki-stream-bot.onrender.com")

@app.on_message(filters.command("start"))
async def start_command(client, message: Message):
    await message.reply_text("স্বাগতম! আমাকে যেকোনো মুভি বা ফাইল ফরওয়ার্ড করো, আমি ডিরেক্ট প্লেব্যাক লিংক তৈরি করে দেব।")

@app.on_message(filters.document | filters.video | filters.audio)
async def generate_link(client, message: Message):
    file_id = ""
    if message.video:
        file_id = message.video.file_id
    elif message.document:
        file_id = message.document.file_id
    elif message.audio:
        file_id = message.audio.file_id
        
    if file_id:
        direct_link = f"{SERVER_URL}/file/{file_id}"
        await message.reply_text(f"তোমার মুভির ডিরেক্ট লিংক:\n{direct_link}")

if __name__ == "__main__":
    app.run()
  
