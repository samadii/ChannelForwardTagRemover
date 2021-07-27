import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests  
from bs4 import BeautifulSoup

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

@bot.on_message(filters.private)
async def fw(c, m):
    input = m.text
    archive_url = f"https://9xbud.com/{input}"
    r = requests.get(archive_url)   
    soup = BeautifulSoup(r.content,'html5lib')  
    links = soup.findAll('a')  
    video_links = [archive_url + link['href'] for link in links if link['href'].endswith('mp4')]
    await message.reply(f"{video_links}")

@bot.on_message(filters.channel & filters.forwarded)
async def fwdrmv(c, m):
    if m.media and not (m.video_note or m.sticker):
        if m.caption:
            cap = m.caption
        else:
            cap = ""
        await m.copy(
            m.chat.id,
            caption=cap,
        )
        await m.delete()
    else:
        await m.copy(m.chat.id)
        await m.delete()

@bot.on_message(filters.private)
async def fwdrm(c, m):
    if m.media and not (m.video_note or m.sticker):
        if m.caption:
            cap = m.caption
        else:
            cap = ""
        await m.copy(
            m.chat.id,
            caption=cap,
        )
    else:
        await m.copy(m.chat.id)


@bot.on_message(filters.group)
async def fwdr(c, m):
    if m.media and not (m.video_note or m.sticker):
        if m.caption:
            cap = m.caption
        else:
            cap = ""
        await m.copy(
            m.chat.id,
            caption=cap,
        )
    else:
        await m.copy(m.chat.id)


bot.run()
