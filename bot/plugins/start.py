from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.config import Config
from ..screenshotbot import ScreenShotBot


@ScreenShotBot.on_message(filters.private & filters.command("start"))
async def start(c, m, cb=False):
    owner_id = Config.AUTH_USERS[0]
    username = 'AD_BOTZ'
    mention = '[BOTZ](https://t.me/AD_BOTZ)'
    try:
        owner = await c.get_users(owner_id)
        username = owner.username if owner.username else 'Ns_AnoNymous'
        mention = owner.mention(style="md")
    except Exception as e:
        print(e)

    BUTTONS = [[
        InlineKeyboardButton("ð¨ð»âð¦± My Father ð¨ð»âð¦±", url=f"https://t.me/{username}"),
        InlineKeyboardButton("ð° Updates Channel ð°", url="https://t.me/AD_BOTZ")
        ],[
        InlineKeyboardButton("ð¬ For Movie ð¬", url="https://t.me/ADMOVEIAD")
        ],[
        InlineKeyboardButton("Help âï¸", callback_data="help"),
        InlineKeyboardButton("Settings â", callback_data="set+settings")
        ],[
        InlineKeyboardButton("Close ð", callback_data="close")
    ]]

    TEXT = f"ð Hi {m.from_user.mention},\n\nI'm Screenshot Generator Botð. I can provide screenshots, sample video from "
    TEXT += "your video files and also can trim. For more details check help.\n\n"
    TEXT += f"**Maintained By:** {mention}"

    if cb:
        try:
            await m.message.edit(
                text=TEXT,
                reply_markup=InlineKeyboardMarkup(BUTTONS)
            )
        except:
            pass
    else:
        await m.reply_text(
            text=TEXT,
            quote=True,
            reply_markup=InlineKeyboardMarkup(BUTTONS)
        )


# i generally liked to use regex filters for callback 
# but since odysseusmax used lambda i am also using the same
@ScreenShotBot.on_callback_query(
    filters.create(lambda _, __, query: query.data.startswith("home"))
)
async def home_cb(c, m):
    await m.answer()
    await start(c, m, True)


@ScreenShotBot.on_callback_query(
    filters.create(lambda _, __, query: query.data.startswith("close"))
)
async def close_cb(c, m):
    try:
        await m.message.delete()
        await m.message.reply_to_message.delete()
    except:
        pass
