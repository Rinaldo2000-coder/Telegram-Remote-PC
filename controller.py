import time, pyautogui
import webbrowser as web
from whatkit import playonyt

def overlayadd():
    pyautogui.click(904, 645)
def skipAdd():
	pyautogui.click(1301, 638)
def forward_to(inp):
	num = ""
	for i in list(inp):
		try:
			i = int(i)
			num += str(i)
		except:
			pass
	if len(num) > 0:
		num = int(num)
		if num > 100:
			num = 95
		elif num < 5:
			num = 5
	else:
		if "fast" in inp:
			num = 95
		elif "back" in inp:
			num = 5
	num = num/100
	x_co = 1315 * num
	pyautogui.click(x_co, 710)
	pyautogui.moveTo(500,500)

def YTvideo(song):
    song = (song.lower()).replace("play","")
    link = playonyt(song)
    web.open(link)
    time.sleep(10)
    # print("hi")
    pyautogui.press("f")


if __name__ =='__main__':
    YTvideo("play tech with tim")
