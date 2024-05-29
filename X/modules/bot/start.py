import random
from X import app
from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from config import OWNER_ID as owner 

@app.on_callback_query()
def pmowner(client, callback_query):
    user_id = owner
    message = "SUPRAXUSERBOT"
    client.send_message(user_id, message)
    client.answer_callback_query(callback_query.id, text="Message sent")

logoX = [
    "https://telegra.ph/file/b158ac35348e622a3d299.jpg"
]

alive_logo = random.choice(logoX)

@app.on_message(filters.command("start") & filters.private)
async def start(app, message):
    chat_id = message.chat.id
    file_id = alive_logo
    caption = "нɛℓℓσ, мʏ Μᴀsᴛᴇʀ ❣️\nИιcɛ Ƭσ Μɛɛт 𝗬σʋ 🤗 !!\nI ɢʋɛƨƨ, тнαт ʏσʋ κиσω мɛ, Ʋнн ʏσʋ ∂σи'т, иρ..\nƜɛℓℓ.\n\n𝗔 Pᴏᴡᴇʀғᴜʟ 𝗔ƨƨɪᴛᴀɴᴛ \n\n 𝐏ᴏᴡᴇʀᴇᴅ 𝐁ʏ 🦋 [SUPRA✨](t.me/Rudra_rajput_ll)\n\nYᴏᴜ Cᴀɴ Cʜᴀᴛ Wɪᴛʜ Mʏ Mᴀsᴛᴇʀ Tʜʀᴏᴜɢʜ Tʜɪs Bᴏᴛ.\nIғ Yᴏᴜ Wᴀɴᴛ Yᴏᴜʀ Oᴡɴ Assɪᴛᴀɴᴛ Yᴏᴜ Cᴀɴ Dᴇᴘʟᴏʏ Fʀᴏᴍ Bᴜᴛᴛᴏɴ Bᴇʟᴏᴡ."
    reply_markup = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("𝐒𝗎𝗉𝗉𝗈𝗋𝗍", url="https://t.me/supra_bots"),
            InlineKeyboardButton("𝐂𝗁𝖺𝗇𝗇𝖾𝗅", url="https://t.me/moii_contact"),
            InlineKeyboardButton("𝐎𝗐𝗇𝖾𝗋", url="https://t.me/RUDRA_RAJPUT_LL"),
            InlineKeyboardButton("𝐑𝖾𝗉𝗈", url="https://github.com/Rudra-singh3588/USERBOT"),
        ],
    ])

    await app.send_photo(chat_id, file_id, caption=caption, reply_markup=reply_markup)
