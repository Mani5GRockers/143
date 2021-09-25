import shutil, psutil
import signal
import os
import asyncio

from pyrogram import idle
from sys import executable

from telegram import ParseMode
from telegram.ext import CommandHandler
from telegraph import Telegraph
from wserver import start_server_async
from bot import bot, app, dispatcher, updater, botStartTime, IGNORE_PENDING_REQUESTS, IS_VPS, PORT, alive, web, OWNER_ID, AUTHORIZED_CHATS, telegraph_token
from bot.helper.ext_utils import fs_utils
from bot.helper.telegram_helper.bot_commands import BotCommands
from bot.helper.telegram_helper.message_utils import *
from .helper.ext_utils.bot_utils import get_readable_file_size, get_readable_time
from .helper.telegram_helper.filters import CustomFilters
from bot.helper.telegram_helper import button_build
from .modules import authorize, list, cancel_mirror, mirror_status, mirror, clone, watch, shell, eval, torrent_search, delete, speedtest, count, leech_settings


def stats(update, context):
    currentTime = get_readable_time(time.time() - botStartTime)
    total, used, free = shutil.disk_usage('.')
    total = get_readable_file_size(total)
    used = get_readable_file_size(used)
    free = get_readable_file_size(free)
    sent = get_readable_file_size(psutil.net_io_counters().bytes_sent)
    recv = get_readable_file_size(psutil.net_io_counters().bytes_recv)
    cpuUsage = psutil.cpu_percent(interval=0.5)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    stats = f'<b>╭──「  🚦 BOT STATISTICS 🚦 」 </b>\n' \
            f'<b>│</b>\n' \
            f'<b>├  ⏰ Bot Uptime :</b> <code>{currentTime}</code>\n' \
            f'<b>├  🗄 Total Disk :</b> <code>{total}</code>\n' \
            f'<b>├  🗂 Total Used :</b> <code>{used}</code>\n' \
            f'<b>├  📂 Total Free :</b> <code>{free}</code>\n' \
            f'<b>│</b>\n' \
            f'<b>├  📝 Data Usage 📝</b>\n' \
            f'<b>│</b>\n' \
            f'<b>├  📥 Total Download :</b> <code>{recv}</code>\n' \
            f'<b>├  📤 Total Upload :</b> <code>{sent}</code>\n' \
            f'<b>├  🖥️ CPU :</b> <code>{cpuUsage}%</code>\n' \
            f'<b>├  🚀 RAM :</b> <code>{memory}%</code>\n' \
            f'<b>├  🗄 DISK :</b> <code>{disk}%</code>\n' \
            f'<b>╰──「 👨‍💻 @Mani5GRockers 」</b>'
    sendMessage(stats, context.bot, update)


def start(update, context):
    buttons = button_build.ButtonMaker()
    buttons.buildbutton("Ⓜ️ ᴍɪʀʀᴏʀ ɢʀᴏᴜᴘ Ⓜ️", "https://t.me/awsmirrorzone")
    buttons.buildbutton("🦸 Chat ᴍɪʀʀᴏʀ ɢʀᴏᴜᴘ 🦸‍♂️", "https://awslink.in/awsmirrorzone-support")
    buttons.buildbutton("⚙️ AWS BOT List ⚙️", "http://t.me/mani5grockersbot")
    buttons.buildbutton("🌐 Website 🌐", "https://bitly.awslink.in/mani5grockers")
    reply_markup = InlineKeyboardMarkup(buttons.build_menu(2))
    if CustomFilters.authorized_user(update) or CustomFilters.authorized_chat(update):
        start_string = f'''
★ This bot can mirror all your links to Drive!

👲 Modded By: @Mani5GRockers

★ Type /{BotCommands.HelpCommand} to get a list of available commands
'''
        if update.message.chat.type == "private" :
            sendMessage(f"👤 Hey I'm AWS MIRROR BOT 👤\n\n➩ JOIN GROUP List 🏆 \n\n ✅ JOIN AWS MIRROR ZONE ✅ \n\n ✥════ @awsmirrorzone ════✥ \n\n ✅ AWS MIRROR ZONE Discussion ✅ \n\n ✥════ @aws_public_chat ════✥ \n\n👩‍⚕ Bot Developer by 👨‍⚕️   👇\n\n✥════ @Mani5GRockers ════✥ \n\n /help - How To use This Group", context.bot, update)
        else :
            sendMarkup(start_string, context.bot, update, reply_markup)
    else :
        sendMarkup(
            '🔒 Oops! not a Authorized user.\n🔐 Please contact Bot developer 👉 <b>@Mani5GRockers</b>.',
            context.bot,
            update,
            reply_markup,
        )


def restart(update, context):
    restart_message = sendMessage("Restarting, Please wait!", context.bot, update)
    # Save restart message object in order to reply to it after restarting
    with open(".restartmsg", "w") as f:
        f.truncate(0)
        f.write(f"{restart_message.chat.id}\n{restart_message.message_id}\n")
    fs_utils.clean_all()
    alive.terminate()
    web.terminate()
    os.execl(executable, executable, "-m", "bot")


def ping(update, context):
    start_time = int(round(time.time() * 1000))
    reply = sendMessage("Starting Ping", context.bot, update)
    end_time = int(round(time.time() * 1000))
    editMessage(f'{end_time - start_time} ms', reply)


def log(update, context):
    sendLogFile(context.bot, update)


help_string_telegraph = f'''
    \n🎀 AWS MIRROR ZONE Help 🎀 
<br><br>
    ✥═══ @awsmirrorzone ═══✥
<br><br>
<b>★ /{BotCommands.HelpCommand}</b>: To get this message
<br><br>
<b>★ /{BotCommands.MirrorCommand}</b> [download_url][magnet_link]: Start mirroring the link to Google Drive.
<br><br>
<b>★ /{BotCommands.TarMirrorCommand}</b> [download_url][magnet_link]: Start mirroring and upload the archived (.tar) version of the download
<br><br>
<b>★ /{BotCommands.ZipMirrorCommand}</b> [download_url][magnet_link]: Start mirroring and upload the archived (.zip) version of the download
<br><br>
<b>★ /{BotCommands.UnzipMirrorCommand}</b> [download_url][magnet_link]: Starts mirroring and if downloaded file is any archive, extracts it to Google Drive
<br><br>
<b>★ /{BotCommands.QbMirrorCommand}</b> 🧲 [magnet_link]: Start Mirroring using qBittorrent, Use <b>/{BotCommands.QbMirrorCommand} s</b> to select files before downloading
<br><br>
<b>★ /{BotCommands.QbTarMirrorCommand}</b> 🧲 [magnet_link]: Start mirroring using qBittorrent and upload the archived (.tar) version of the download
<br><br>
<b>★ /{BotCommands.QbZipMirrorCommand}</b> 🧲 [magnet_link]: Start mirroring using qBittorrent and upload the archived (.zip) version of the download
<br><br>
<b>★ /{BotCommands.QbUnzipMirrorCommand}</b> 🧲 [magnet_link]: Starts mirroring using qBittorrent and if downloaded file is any archive, extracts it to Google Drive
<br><br>
<b>★ /{BotCommands.LeechCommand}</b> [download_url][magnet_link]: Start leeching to Telegram, Use <b>/{BotCommands.LeechCommand} s</b> to select files before leeching
<br><br>
<b>★ /{BotCommands.TarLeechCommand}</b> [download_url][magnet_link]:  Start leeching to Telegram and upload it as (.tar)
<br><br>
<b>★ /{BotCommands.ZipLeechCommand}</b> [download_url][magnet_link]: Start leeching to Telegram and upload it as (.zip)
<br><br>
<b>★ /{BotCommands.UnzipLeechCommand}</b> [download_url][magnet_link]: Start leeching to Telegram and if downloaded file is any archive, extracts it to Telegram
<br><br>
<b>★ /{BotCommands.QbLeechCommand}</b> 🧲 [magnet_link]: Start leeching to Telegram using qBittorrent, Use <b>/{BotCommands.QbLeechCommand} s</b> to select files before leeching
<br><br>
<b>★ /{BotCommands.QbTarLeechCommand}</b> 🧲 [magnet_link]: Start leeching to Telegram using qBittorrent and upload it as (.tar)
<br><br>
<b>★ /{BotCommands.QbZipLeechCommand}</b> 🧲 [magnet_link]: Start leeching to Telegram using qBittorrent and upload it as (.zip)
<br><br>
<b>★ /{BotCommands.QbUnzipLeechCommand}</b> 🧲 [magnet_link]: Start leeching to Telegram using qBittorrent and if downloaded file is any archive, extracts it to Telegram
<br><br>
<b>★ /{BotCommands.CloneCommand}</b> [drive_url]: Copy file/folder to Google Drive
<br><br>
<b>★ /{BotCommands.CountCommand}</b> [drive_url]: Count file/folder of Google Drive Links
<br><br>
<b>★ /{BotCommands.DeleteCommand}</b> [drive_url]: Delete file from Google Drive (Only Owner & Sudo)
<br><br>
<b>★ /{BotCommands.WatchCommand}</b> [youtube-dl supported link]: Mirror through youtube-dl. Click <b>/{BotCommands.WatchCommand}</b> for more help
<br><br>
<b>★ /{BotCommands.TarWatchCommand}</b> [youtube-dl supported link]: Mirror through youtube-dl and tar before uploading
<br><br>
<b>★ /{BotCommands.ZipWatchCommand}</b> [youtube-dl supported link]: Mirror through youtube-dl and zip before uploading
<br><br>
<b>/{BotCommands.LeechWatchCommand}</b> [youtube-dl supported link]: Leech through youtube-dl 
<br><br>
<b>★ /{BotCommands.LeechTarWatchCommand}</b> [youtube-dl supported link]: Leech through youtube-dl and tar before uploading 
<br><br>
<b>★ /{BotCommands.LeechZipWatchCommand}</b> [youtube-dl supported link]: Leech through youtube-dl and zip before uploading 
<br><br>
<b>★ /{BotCommands.LeechSetCommand}</b>: Leech Settings 
<br><br>
<b>★ /{BotCommands.SetThumbCommand}</b>: Reply photo to set it as Thumbnail
<br><br>
<b>★ /{BotCommands.CancelMirror}</b>: Reply to the message by which the download was initiated and that download will be cancelled
<br><br>
<b>★ /{BotCommands.CancelAllCommand}</b>: Cancel all running tasks
<br><br>
<b>★ /{BotCommands.ListCommand}</b> [search term]: Searches the search term in the Google Drive, If found replies with the link
<br><br>
<b>★ /{BotCommands.StatusCommand}</b>: Shows a status of all the downloads
<br><br>
<b>★ /{BotCommands.StatsCommand}</b>: Show Stats of the machine the bot is hosted on
<br><br>
<b>★ /{BotCommands.TsHelpCommand}</b> 🧲 help for Torrent 🔍 search:  1337x, piratebay, tgx, yts, eztv, nyaa.si, sukebei, torlock, rarbg, ts  ★
<br><br>
'''
help = Telegraph(access_token=telegraph_token).create_page(
        title='AWS MIRROR ZONE BOT Help',
        author_name='❤️ Mani5GRockers ❤️',
        author_url='https://github.com/Mani5GRockers',
        html_content=help_string_telegraph,
    )["path"]

help_string = f'''
    \n🎀 AWS MIRROR ZONE Help 🎀
    
    ✥══ @awsmirrorzone ══✥
    
★ /{BotCommands.PingCommand}: Check how long it takes to Ping the Bot

★ /{BotCommands.AuthorizeCommand}: Authorize a chat or a user to use the bot (Can only be invoked by Owner & Sudo of the bot)

★ /{BotCommands.UnAuthorizeCommand}: Unauthorize a chat or a user to use the bot (Can only be invoked by Owner & Sudo of the bot)

★ /{BotCommands.AuthorizedUsersCommand}: Show authorized users (Only Owner & Sudo)

★ /{BotCommands.AddSudoCommand}: Add sudo user (Only Owner)

★ /{BotCommands.RmSudoCommand}: Remove sudo users (Only Owner)

★ /{BotCommands.RestartCommand}: Restart the bot

★ /{BotCommands.LogCommand}: Get a log file of the bot. Handy for getting crash reports

★ /{BotCommands.SpeedCommand}: Check Internet Speed of the Host

★ /{BotCommands.ShellCommand}: Run commands in Shell (Only Owner)

★ /{BotCommands.ExecHelpCommand}: Get help for Executor module (Only Owner)

★ /{BotCommands.TsHelpCommand}: Get help for Torrent search module

   ✥══ @Mani5GRockers ══✥
'''

def bot_help(update, context):
    button = button_build.ButtonMaker()
    button.buildbutton("Other Commands", f"https://telegra.ph/{help}")
    reply_markup = InlineKeyboardMarkup(button.build_menu(1))
    sendMarkup(help_string, context.bot, update, reply_markup)

'''
botcmds = [
        (f'{BotCommands.HelpCommand}','Get Detailed Help'),
        (f'{BotCommands.MirrorCommand}', 'Start Mirroring'),
        (f'{BotCommands.TarMirrorCommand}','Start mirroring and upload as .tar'),
        (f'{BotCommands.ZipMirrorCommand}','Start mirroring and upload as .zip'),
        (f'{BotCommands.UnzipMirrorCommand}','Extract files'),
        (f'{BotCommands.QbMirrorCommand}','Start Mirroring using qBittorrent'),
        (f'{BotCommands.QbTarMirrorCommand}','Start mirroring and upload as .tar using qb'),
        (f'{BotCommands.QbZipMirrorCommand}','Start mirroring and upload as .zip using qb'),
        (f'{BotCommands.QbUnzipMirrorCommand}','Extract files using qBitorrent'),
        (f'{BotCommands.CloneCommand}','Copy file/folder to Drive'),
        (f'{BotCommands.CountCommand}','Count file/folder of Drive link'),
        (f'{BotCommands.DeleteCommand}','Delete file from Drive'),
        (f'{BotCommands.WatchCommand}','Mirror Youtube-dl support link'),
        (f'{BotCommands.TarWatchCommand}','Mirror Youtube playlist link as .tar'),
        (f'{BotCommands.ZipWatchCommand}','Mirror Youtube playlist link as .zip'),
        (f'{BotCommands.CancelMirror}','Cancel a task'),
        (f'{BotCommands.CancelAllCommand}','Cancel all tasks'),
        (f'{BotCommands.ListCommand}','Searches files in Drive'),
        (f'{BotCommands.StatusCommand}','Get Mirror Status message'),
        (f'{BotCommands.StatsCommand}','Bot Usage Stats'),
        (f'{BotCommands.PingCommand}','Ping the Bot'),
        (f'{BotCommands.RestartCommand}','Restart the bot [owner/sudo only]'),
        (f'{BotCommands.LogCommand}','Get the Bot Log [owner/sudo only]'),
        (f'{BotCommands.TsHelpCommand}','Get help for Torrent search module')
    ]
'''

def main():
    fs_utils.start_cleanup()
    if IS_VPS:
        asyncio.get_event_loop().run_until_complete(start_server_async(PORT))
    # Check if the bot is restarting
    if os.path.isfile(".restartmsg"):
        with open(".restartmsg") as f:
            chat_id, msg_id = map(int, f)
        bot.edit_message_text("✅ Restarted successfully!", chat_id, msg_id)
        os.remove(".restartmsg")
    elif OWNER_ID:
        try:
            text = "<b>♻️ Bot Restarted!</b>"
            bot.sendMessage(chat_id=OWNER_ID, text=text, parse_mode=ParseMode.HTML)
            if AUTHORIZED_CHATS:
                for i in AUTHORIZED_CHATS:
                    bot.sendMessage(chat_id=i, text=text, parse_mode=ParseMode.HTML)
        except Exception as e:
            LOGGER.warning(e)
    # bot.set_my_commands(botcmds)
    start_handler = CommandHandler(BotCommands.StartCommand, start, run_async=True)
    ping_handler = CommandHandler(BotCommands.PingCommand, ping,
                                  filters=CustomFilters.authorized_chat | CustomFilters.authorized_user, run_async=True)
    restart_handler = CommandHandler(BotCommands.RestartCommand, restart,
                                     filters=CustomFilters.owner_filter | CustomFilters.sudo_user, run_async=True)
    help_handler = CommandHandler(BotCommands.HelpCommand,
                                  bot_help, filters=CustomFilters.authorized_chat | CustomFilters.authorized_user, run_async=True)
    stats_handler = CommandHandler(BotCommands.StatsCommand,
                                   stats, filters=CustomFilters.authorized_chat | CustomFilters.authorized_user, run_async=True)
    log_handler = CommandHandler(BotCommands.LogCommand, log, filters=CustomFilters.owner_filter | CustomFilters.sudo_user, run_async=True)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(ping_handler)
    dispatcher.add_handler(restart_handler)
    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(stats_handler)
    dispatcher.add_handler(log_handler)
    updater.start_polling(drop_pending_updates=IGNORE_PENDING_REQUESTS)
    LOGGER.info("Bot Started!")
    signal.signal(signal.SIGINT, fs_utils.exit_clean_up)

app.start()
main()
idle()
