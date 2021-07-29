import os
import cloudscraper
import time
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests  
from bs4 import BeautifulSoup

scraper = cloudscraper.create_scraper()

bot = Client(
    "Remove FwdTag",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)



START_TXT = """
Hi {}, I'm Forward Tag Remover bot.\n\nForward me some messages, i will remove forward tag from them.\nAlso can do it in channels.
"""

START_BTN = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Source Code', url='https://github.com/samadii/ChannelForwardTagRemover'),
        ]]
    )


@bot.on_message(filters.command(["start"]))
async def start(bot, update):
    text = START_TXT.format(update.from_user.mention)
    reply_markup = START_BTN
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

@bot.on_message(filters.regex(r'https?://[^\s]+') & filters.private)
async def link_handler(c, m):
    headers = {
        "User-agent": 'Mozilla/5.0 (Linux; Android 4.4.2; Hol-U19) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36'}
    URL = f'{m.text}'
    r = scraper.get(URL, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    links = soup.findAll('a')
    print(links)
    await m.reply(f"links}")
    


bot.run()
