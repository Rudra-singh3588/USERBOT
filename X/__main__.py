import importlib
from pyrogram import idle
from uvloop import install


from X.modules import ALL_MODULES
from X import BOTLOG_CHATID, LOGGER, LOOP, aiosession, app, bots, ids, bot1
from X.helpers import join
from X.helpers.misc import create_botlog, heroku

BOT_VER = "3.0.0"
CMD_HANDLER = ["." "?" "!" "*"]
MSG_ON = """
✧✧ LETS GO 😗
▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭

➥ HELLO HELLO 🥀 ** `{}`
➥ BOT STARTED
▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭
➥ 𝐎ᴡɴᴇʀ :- @rudra_rajput_ll
➥ 𝐆ʀᴘ :- @supra_bots
➥ 𝐂ʜᴀɴ :- @moii_contact
▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭
"""


async def main():
    await app.start()
    print("𝐋𝐎𝐆: 𝐅𝐨𝐮𝐧𝐝𝐞𝐝 𝐁𝐨𝐭 𝐭𝐨𝐤𝐞𝐧 𝐁𝐨𝐨𝐭𝐢𝐧𝐠..")
    for all_module in ALL_MODULES:
        importlib.import_module("X.modules" + all_module)
        print(f"𝐃ɪᴄᴛᴀᴛᴏʀ 𝐔sᴇʀ𝐁ᴏᴛ 𝐒ᴜᴄᴄᴇssғᴜʟʟʏ 𝐈ᴍᴘᴏʀᴛᴇᴅ {all_module} ")
    for bot in bots:
        try:
            await bot.start()
            ex = await bot.get_me()
            await join(bot)
            try:
                await bot.send_message(BOTLOG_CHATID, MSG_ON.format(BOT_VER, CMD_HANDLER))
            except BaseException:
                pass
            print(f"𝐘ᴏᴜʀ 𝐃ɪᴄᴛᴀᴛᴏʀ 𝐔sᴇʀ𝐁ᴏᴛ 𝐒ᴛᴀʀᴛᴇᴅ 𝐀s{ex.first_name} | {ex.id} ")
            ids.append(ex.id)
        except Exception as e:
            print(f"{e}")
    if not str(BOTLOG_CHATID).startswith("-100"):
        await create_botlog(bot1)
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    LOGGER("X").info("SUPRA USERBOT STARTED✨")
    install()
    heroku()
    LOOP.run_until_complete(main())
