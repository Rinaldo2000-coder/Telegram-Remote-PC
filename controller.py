import selenium as sl
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from whatkit import playonyt
import time, pyautogui
path = 'chromedriver.exe'
path1 = r'C:\Program Files (x86)\chrome_driver\edge90\msedgedriver.exe'
options = Options()
options.add_argument('start_maximized')
options.add_experimental_option("useAutomationExtension", False)
options.add_argument('--disable-infobars')
driver = webdriver.Chrome(options = options, executable_path = path)
pyautogui.click(1035, 115)
pyautogui.moveTo(500,500)
p144="//span[contains(string(),'144p')]"
p240="//span[contains(string(),'240p')]"
p360="//span[contains(string(),'360p')]"
p720="//span[contains(string(),'720p')]"
p1080="//span[contains(string(),'1080p')]"

def MaxWindow(driver =driver):
    try:
        driver.maximize_window()
    except:
        pass
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
def Quality(pixl, driver = driver):
    try:
        driver.find_element_by_css_selector('button.ytp-button.ytp-settings-button').click()
        driver.find_element_by_xpath("//div[contains(text(),'Quality')]").click()
        quality = driver.find_element_by_xpath(pixl)
        quality.click()
    except:
        pass
def YTvideo(song, driver = driver, pixl = p1080):
    song = (song.lower()).replace("play","")
    link = playonyt(song)
    driver.get(link)
    Quality(pixl)
    try:
        driver.fullscreen_window()
    except:
        pass
def pause_play(driver = driver):
	for i in range(50):
	    try:
	        pause_xpath = '//*[@id="movie_player"]/div['+ str(i) +']/div[2]/div[1]/button'
	        pause = driver.find_element_by_xpath(pause_xpath)
	        pause.click()
	        break
	    except:
	    	pass
def full_screen(driver = driver):
	status = ""
	for i in range(50):
	    try:
	        flu_xpath = '//*[@id="movie_player"]/div['+ str(i) +']/div[2]/div[2]/button[10]'
	        driver.find_element_by_xpath(flu_xpath).click()
	        break
	    except:
	        pass
	    if i == 49:
	    	status = "failed"
	if status == "failed":
		driver.fullscreen_window()
def Quit(driver = driver):
    driver.close()
    driver.quit()
    quit()
if __name__ =='__main__':
    YTvideo("play tech with tim")
    time.sleep(30)
    full_screen()
    time.sleep(5)
    full_screen()
    time.sleep(5)
    pause_play()
    time.sleep(5)
    pause_play()
