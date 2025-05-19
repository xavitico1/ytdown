from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from utils.youtube_downloader import YouTubeDownloader
import config

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Welcome to the YouTube Downloader Bot! Send me a YouTube video link to download.')

def download_video(update: Update, context: CallbackContext) -> None:
    if context.args:
        url = context.args[0]
        downloader = YouTubeDownloader()
        try:
            video_file = downloader.download_video(url)
            update.message.reply_text('Video downloaded successfully!')
            context.bot.send_video(chat_id=update.message.chat_id, video=open(video_file, 'rb'))
        except Exception as e:
            update.message.reply_text(f'Error: {str(e)}')
    else:
        update.message.reply_text('Please provide a YouTube video URL.')

def main() -> None:
    updater = Updater(config.BOT_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("download", download_video))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()