from telegram.ext import *
import os, pyautogui
from controller import *
from telegram import *

class TelegramPcController():

    API_KEY = '1743814674:AAGTkcpXmjnGGGANRegfucaGjPfM7WCDrlA'
    helptext = "You can try\n\n1)Play Sweet but psycho\n2)Change resolution to 1080p\n3)Pause Video\n4)Quit\n5)Shut down\n6)Exit fullscreen"
    helptext = helptext + "\n7)Volume Up\n8)Fast forward to 60%\n"

    def start(self, update, content):
        update.message.reply_text(self.helptext)
        self.InlineButton(update, content)
        update.message.reply_text('Type something...')

    def help1(self, update, content):
        update.message.reply_text(self.helptext)

    def InlineButton(self, update, content):
        button_text = ["Pause", "Play", "Shutdown", "Cancel Shutdown", "Quit"]
        button_reply = ["pause", "play", "shutdown", "cancel shutdown", "quit"]
        buttons = []
        for i in range(len(button_text)):
            btn = [InlineKeyboardButton(button_text[i], callback_data=button_reply[i])]
            buttons.append(btn)
        content.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons), text="Welcome")

    def Query_Handler(self, update, content):
        try:
            self.text = update.callback_query.data
            # print(self.text)
            self.CommandCenter(update, content)
            update.callback_query.answer()     
        except Exception as e:
            print(e)

    def ShutDown(self, time1 = 20):
        cont = "shutdown -s -t %s" % time1
        os.system(cont)
        ans =  "Your PC will be turned off within 20 Seconds, 'Stop Shutdown' to Stop the shutdown"
        return ans
    def CancelShutDown(self):
        cont = "shutdown /a"
        os.system(cont)

    def CommandCenter(self, update, content):
        text = self.text
        if ("shutdown" or "shut down") == text:
            text = str(update.message.text).lower()
            sts = ShutDown()
            update.message.reply_text(sts)
        elif "quit" == text:
            quit()
        elif ("play") == text:
            pyautogui.press("space")
        elif "volume" in text:
            if "down" in text:
                pyautogui.press('volumedown')
                pyautogui.press('volumedown')
                pyautogui.press('volumedown')
            elif "up" in text:
                pyautogui.press('volumeup')
                pyautogui.press('volumeup')
                pyautogui.press('volumeup')
        elif ("fast forward") in text:
            forward_to(text)
        elif ("back forward") in text:
            forward_to(text)
        elif ("pause") == text:
            pyautogui.press("space")
        elif ("play" in text) and ("play" != text):
            YTvideo(text)
        elif "change resolution" in text:
            pass
        elif ("maximize" and "window") in text:
            MaxWindow()
        elif ("fullscreen" in text ) or ("full screen"in text):
            pyautogui.press("f")
        elif ("cancel" and "shutdown") in text:
            CancelShutDown()
            update.message.reply_text("Okay, ShutDown cancelled!")
        elif ("stop" and "shutdown") in text:
            CancelShutDown()
            update.message.reply_text("Okay, ShutDown cancelled!")
        else:
            update.message.reply_text("Sorry, I can't do that!") 
    
    def message_center(self, update, content):
        self.text = str(update.message.text).lower()
        self.CommandCenter()

    def main(self, key = API_KEY):
        updater = Updater(key, use_context=True)
        dp = updater.dispatcher
        dp.add_handler(CommandHandler("start", self.start))
        dp.add_handler(CommandHandler("help", self.help1))
        dp.add_handler(MessageHandler(Filters.text, self.message_center))
        dp.add_handler(CallbackQueryHandler(self.Query_Handler))
        updater.start_polling()
        updater.idle()
if __name__ == '__main__':
    TelegramPcController().main()


