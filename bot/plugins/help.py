from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from bot.screenshotbot import ScreenShotBot
from bot.config import Config


BUTTONS = [[
    InlineKeyboardButton('π‘ Home π‘', callback_data='home'),
    InlineKeyboardButton('π Close π', callback_data='close')
]]

HELP_TEXT = """
Hi {mention}. Welcome to Screenshot Generator Bot. You can use me to generate:

    1. πScreenshots.
    2. πSample Video.
    3. πTrim Video.

π β I support any kind of **telegram video file** (streaming video or document video files) provided it --has proper mime-type-- and --is not corrupted--.
π β I also support **Streaming URLs**. The URL should be a --streaming URL--, --non IP specific--, and --should return proper response codes--.
Just send me the telegram file or the streaming URL.

See /settings to configure bot's behavior.
Use /set_watermark to set custom watermarks to your screenshots.

**General FAQ.**

π β If the bot dosen't respond to telegram files you forward, first check /start and --confirm bot is alive--. Then make sure the file is a **video file** which satisfies above mentioned conditions.
π β If bot replies __π Sorry! I cannot open the file.__, the file might be --currupted-- or --is malformatted--.

__If issues persists contact my father.__

{admin_notification}
"""
ADMIN_NOTIFICATION_TEXT = (
    "Since you are one of the admins, you can check /admin to view the admin commands."
)


@ScreenShotBot.on_message(filters.private & filters.command("help"))
async def help_(c, m):

    await m.reply_text(
        text=HELP_TEXT.format(
            mention=m.from_user.mention,
            admin_notification=ADMIN_NOTIFICATION_TEXT
            if m.from_user.id in Config.AUTH_USERS
            else "",
        ),
        reply_markup=InlineKeyboardMarkup(BUTTONS),
        quote=True,
    )


@ScreenShotBot.on_callback_query(
    filters.create(lambda _, __, query: query.data.startswith("help"))
)
async def help_cb(c, m):
    await m.answer()
    await m.message.edit(
        text=HELP_TEXT.format(
            mention=m.from_user.mention,
            admin_notification=ADMIN_NOTIFICATION_TEXT
            if m.from_user.id in Config.AUTH_USERS
            else "",
        ),
        reply_markup=InlineKeyboardMarkup(BUTTONS)
    )
