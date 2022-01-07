from telegram.ext import *
import os, pyautogui
from controller import *
from telegram import *

# Dependencies
# pip install telegram
# pip install python-telegram-bot

class TelegramPcController():
    file_api = open("api.txt", "r")
    API_KEY = file_api.read()
    file_api.close()
    helptext = "You can try\n\n1)Play Sweet but psycho\n2)Change resolution to 1080p\n3)Pause Video\n4)Quit\n5)Shut down\n6)Exit fullscreen"
    helptext = helptext + "\n7)Volume Up\n"

    def start(self, update, content):
        # update.message.reply_text(self.helptext)
        self.InlineButton(update, content)
        # update.message.reply_text('Type something...')

    def help1(self, update, content):
        update.message.reply_text(self.helptext)
        self.InlineButton(update, content)

    def InlineButton(self, update, content):
        button_text = ["Pause", "Play", "Volume Up", "Volume Down", "Mute", "Fast Forward", "Back Forward", "Fullscreen", "Hotkeys","Shutdown", "Cancel Shutdown", "Quit"]
        button_reply = ["pause", "play", "volume up", "volume down", "mute","fast forward", "back forward", "fullscreen", "hotkeys", "shutdown", "cancel shutdown", "quit"]
        buttons = []
        for i in range(len(button_text)):
            btn = [InlineKeyboardButton(button_text[i], callback_data=button_reply[i])]
            buttons.append(btn)
        content.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons), text="Welcome")
    def InlineButton_Hotkeys(self, update, content):
        button_text = ["Multitask", "Switch Tabs", "Next Workpace", "Previous Workspace", "Close Window"]
        button_reply = ["ctrl+alt+tab", "ctrl+tab", "ctrl+win+right", "ctrl+win+left", "alt+f4"]
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
            exit()
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
        elif ("fast forward") == text:
            pyautogui.press("right")
        elif ("back forward") == text:
            pyautogui.press("left")
        elif ("pause") == text:
            pyautogui.press("space")
        elif ("play" in text) and ("play" != text):
            YTvideo(text)
        elif "mute" == text:
            pyautogui.press("volumemute")
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
        elif "ctrl+tab" == text:
            pyautogui.hotkey("ctrl", "tab")
        elif "ctrl+alt+tab" == text:
            pyautogui.hotkey("ctrl", "alt", "tab")
        elif "alt+f4" == text:
            pyautogui.hotkey("alt", "f4")
        elif "ctrl+win+right" == text:
            pyautogui.hotkey("ctrl", "win", "right")
        elif "ctrl+win+left" == text:
            pyautogui.hotkey("ctrl", "win", "left")
        elif "hotkeys" == text:
            self.InlineButton_Hotkeys(update, content)
        else:
            update.message.reply_text("Sorry, I can't do that!") 
    
    def message_center(self, update, content):
        self.text = str(update.message.text).lower()
        self.CommandCenter(update, content)

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


