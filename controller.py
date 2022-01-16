import time, pyautogui
import webbrowser as web
from whatkit import playonyt
from os import path

class MainController():

    def __init__(self, text):
        self.text = text
        # self.find_home_loc()
        self.current_location = self.home_location
        os.chdir(self.home_location)
        self.command_reader()

    def command_reader(self):

        if self.text == "pwd":
            print_working_directory()
        elif self.text[:3] == "cd ":
            self.text = self.text.replace("cd ", "")
            self.change_directory()
            

    def change_directory(self):
        tmp_location = path.join(self.current_location, self.text)
        tmp_location = path.realpath(tmp_location)
        if path.isdir(tmp_location) or path.isfile(tmp_location):
            self.current_location = tmp_location
            print(self.current_location)
        else:
            return "Invaild file or location"


        # print(self.home_location)

    def print_working_directory(self):

        return self.current_location

def find_home_loc():
    home_location = path.expanduser('~')
    try:
        home_loc_file = open("home.txt", 'r')
        tmp_location = home_loc_file.read()
        if path.isdir(home_location):
            home_location = tmp_location
        # else:
        #     print("Invaild home location!!")

        home_loc_file.close()
    except Exception as e:
        home_loc_file = open("home.txt", 'w')
        home_loc_file.write(home_location)
        home_loc_file.close()
    os.chdir(home_location)
    
def YTvideo(song):
    song = (song.lower()).replace("play","")
    link = playonyt(song)
    web.open(link)
    time.sleep(10)
    # print("hi")
    pyautogui.press("f")


if __name__ =='__main__':
    MainController("cd ../../../../Documents/mydir")
    # YTvideo("play tech with tim")
