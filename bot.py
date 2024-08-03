python
     from telegram import Update, ForceReply
     from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
     import requests

     TOKEN = '7230016979:AAEmwchs6_snJjoDZZMP3u60SA8WHt3ZKLs'
     SERVER_URL = 'https://your-heroku-app.herokuapp.com'

     def start(update: Update, context: CallbackContext) -> None:
         update.message.reply_text('Hello! I am ArtGenBot. Send me a command to get started.')

     def handle_message(update: Update, context: CallbackContext) -> None:
         text = update.message.text
         if update.message.photo:
             # Save the photo and send it to the server
             photo_file = update.message.photo[-1].get_file()
             photo_file.download('temp_photo.jpg')
             files = {'file': open('temp_photo.jpg', 'rb')}
             response = requests.post(f"{SERVER_URL}/upload/", files=files)
             update.message.reply_text(f"File uploaded. ID: {response.json().get('file_id')}")
         else:
             update.message.reply_text('Command not recognized.')

     def main() -> None:
         updater = Updater(TOKEN)

         dispatcher = updater.dispatcher

         dispatcher.add_handler(CommandHandler("start", start))
         dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
         dispatcher.add_handler(MessageHandler(Filters.photo, handle_message))

         updater.start_polling()
         updater.idle()

     if __name__ == '__main__':
         main()