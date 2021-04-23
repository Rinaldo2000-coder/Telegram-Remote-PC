from telegram.ext import *
import os, pyautogui
from controller import *
API_KEY = '1743814674:AAGTkcpXmjnGGGANRegfucaGjPfM7WCDrlA'
helptext = "You can try\n\n1)Play Vaathi Coming\n2)Change resolution to 1080p\n3)Pause Video\n4)Quit\n5)Shut down\n6)Exit fullscreen"
helptext = helptext + "\n7)Volume Up\n8)FastF forward to 60%\n9)Skip ad\n10)Close ad"
p144="//span[contains(string(),'144p')]"
p240="//span[contains(string(),'240p')]"
p360="//span[contains(string(),'360p')]"
p720="//span[contains(string(),'720p')]"
p1080="//span[contains(string(),'1080p')]"

def start(update, content):
    update.message.reply_text(helptext)
    update.message.reply_text('Type something...')
def help1(update, content):
    update.message.reply_text(helptext)
def ShutDown(time1 = 20):
	cont = "shutdown -s -t %s" % time1
	os.system(cont)
	ans =  "Your PC will be turned off within 20 Seconds, 'Stop Shutdown' to Stop the shutdown"
	return ans
def CancelShutDown():
	cont = "shutdown /a"
	os.system(cont)
def center(update, content):
	text = str(update.message.text).lower()
	if ("shutdown") == text:
		text = str(update.message.text).lower()
		sts = ShutDown()
		update.message.reply_text(sts)
	if ("shut down") == text:
		text = str(update.message.text).lower()
		sts = ShutDown()
		update.message.reply_text(sts)
	elif "quit" == text:
		Quit()
		quit()
	elif ("play") == text:
		pause_play()
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
		pause_play()
	elif ("play" in text) and ("play" != text):
		YTvideo(text)
	elif "change resolution" in text:
		if "1080" in text:
			Quality(pixl = p1080)
		elif "720" in text:
			Quality(pixl = p720)
		elif "480" in text:
			Quality(pixl = p480)
		elif "360" in text:
			Quality(pixl = p360)
		elif "240" in text:
			Quality(pixl = p240)
		else:
			Quality(pixl = p720)
	elif ("maximize" and "window") in text:
		MaxWindow()
	elif ("fullscreen") in text:
		full_screen()
	elif ("full screen") in text:
		full_screen()
	elif ("skip trial") == text:
		pyautogui.click(200 ,710)
		pyautogui.moveTo(500, 500)
	elif text in ("close", "close ad", "close add"):
		overlayadd()
	elif text in ("skip", "skip ad", "skip add"):
		skipAdd()
	elif ("cancel" and "shutdown") in text:
		CancelShutDown()
		update.message.reply_text("Okay, ShutDown cancelled!")
	elif ("stop" and "shutdown") in text:
		CancelShutDown()
		update.message.reply_text("Okay, ShutDown cancelled!")
	else:
		update.message.reply_text("Sorry, I can't do that!")		
def main(key = API_KEY):
    updater = Updater(key, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help1))
    dp.add_handler(MessageHandler(Filters.text, center))
    updater.start_polling()
    updater.idle()
main()

