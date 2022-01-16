from telegram.ext import *
import os, pyautogui
from controller import *
from telegram import *
import controller
# Dependencies
# pip install telegram
# pip install python-telegram-bot

# change to home directory
controller.find_home_loc()

class TelegramPcController():
    file_api = open("api.txt", "r")
    API_KEY = file_api.read()
    file_api.close()
    helptext = "You can try\n\n1)Play Sweet but psycho\n2)cd music\n3)pwd\n4)open music.mp4\n5)ls\n"
    # helptext = helptext + "\n7)Volume Up\n"
    
    def __init__(self):
        self.multitask_btn = "mult"

    def build_menu(self, buttons, n_cols, header_buttons=None, footer_buttons=None):
        menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
        if header_buttons:
            menu.insert(0, header_buttons)
        if footer_buttons:
            menu.append(footer_buttons)
        return menu
    def build_menu_list(self, buttons, n_cols, header_buttons=None, footer_buttons=None):
        menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
        if header_buttons:
            menu.insert(0, header_buttons)
        if footer_buttons:
            menu.append(footer_buttons)
        return menu
    def start(self, update, content):
        # update.message.reply_text(self.helptext)
        self.InlineButton(update, content)
        self.InlineButton_Hotkeys(update, content)
        # update.message.reply_text('Type something...')

    def help1(self, update, content):
        update.message.reply_text(self.helptext)
        self.InlineButton(update, content)

    def InlineButton(self, update, content):
        button_text = [["Pause", "Play"], ["Volume Down", "Mute","Volume Up"], ["Back Forward", "Fast Forward"], "Fullscreen", "Hotkeys", "Quit", ["Shutdown", "Cancel Shutdown"]]
        button_list = []
        for each in button_text:
            button_row = []
            if type(each) == list:
                for each1 in each:
                    button_row.append(InlineKeyboardButton(each1, callback_data = each1.lower()))
            else:
                button_row.append(InlineKeyboardButton(each, callback_data = each.lower()))
            button_list.append(button_row)
        reply_markup=InlineKeyboardMarkup(button_list) #n_cols = 1 is for single column and mutliple rows
        #bot1.sendMessage(chat_id=update.message.chat_id, text='Choose from the following',reply_markup=reply_markup)
        update.message.reply_text("Options", reply_markup = reply_markup)
        # content.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons), text="Welcome")
    def InlineButton_Hotkeys(self, update, content):
        button_text = [["⬅️", "Multitask", "➡️"], "Switch Tabs", ["Previous Workpace", "Next Workspace"], "Close Tab", "Close Window"]
        button_reply = [["back forward", "multitask", "fast forward"], "ctrl+tab", ["ctrl+win+left", "ctrl+win+right"], "ctrl+f4", "alt+f4"]
        button_list = []
        for n, each in enumerate(button_text):
            button_row = []
            if type(each) == list:
                for n1, each1 in enumerate(each):
                    button_row.append(InlineKeyboardButton(each1, callback_data = button_reply[n][n1]))
            else:
                button_row.append(InlineKeyboardButton(each, callback_data = button_reply[n]))
            button_list.append(button_row)
        reply_markup=InlineKeyboardMarkup(button_list) #n_cols = 1 is for single column and mutliple rows
        #bot1.sendMessage(chat_id=update.message.chat_id, text='Choose from the following',reply_markup=reply_markup)
        update.message.reply_text("Control buttons", reply_markup = reply_markup)
    
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
                #pyautogui.press('volumedown')
                # pyautogui.press('volumedown')
            elif "up" in text:
                pyautogui.press('volumeup')
                # pyautogui.press('volumeup')
                # pyautogui.press('volumeup')
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
        elif "multitask" == text:
            if self.multitask_btn == "mult":
                pyautogui.hotkey("ctrl", "alt", "tab")
                self.multitask_btn = "selt"
            else:
                pyautogui.press("space")
                self.multitask_btn = "mult"
        # elif "ctrl+alt+tab" == text:
        #     pyautogui.hotkey("ctrl", "alt", "tab")
        elif "alt+f4" == text:
            pyautogui.hotkey("alt", "f4")
        elif "ctrl+f4" == text:
            pyautogui.hotkey("ctrl", "f4")
        elif "ctrl+win+right" == text:
            pyautogui.hotkey("ctrl", "win", "right")
        elif "ctrl+win+left" == text:
            pyautogui.hotkey("ctrl", "win", "left")
        elif "hotkeys" == text:
            self.InlineButton_Hotkeys(update, content)
            # self.buttonfun(update, content)
        else:
            reply_controller = controller.MainController(text)
            try:
                return_text = reply_controller.return_text
            except Exception as e:
                return_text = ""
            if return_text == 0:
                update.message.reply_text("Sorry, I can't do that!") 
            elif len(return_text) > 1:
                update.message.reply_text(return_text)
            else:
                pass
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


