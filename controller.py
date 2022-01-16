import time, pyautogui
import webbrowser as web
from whatkit import playonyt
from os import path
import os

class MainController():

    def __init__(self, text):
        self.text = text
        # self.find_home_loc()
        self.return_text = ""
        self.current_location = os.getcwd()
        # os.chdir(self.home_location)
        self.command_reader()

    def command_reader(self):

        if self.text == "pwd":
            self.print_working_directory()
        elif self.text[:3] == "cd ":
            self.text = self.text.replace("cd ", "")
            self.change_directory()
        elif self.text[:5] == "open ":
            self.text = self.text.replace("open ", "")
            self.open_file()
        elif ("ls" == self.text) or ("dir" == self.text):
            self.list_working_directory()
        else:
            self.return_text = 0

    def change_directory(self):
        dir_list = os.listdir(self.current_location)
        for n, txt in enumerate(dir_list):
            if self.text == txt.lower():
                self.text = txt
            elif self.text == str(n):
                self.text = txt
            else:
                pass
        tmp_location = path.join(self.current_location, self.text)
        tmp_location = path.realpath(tmp_location)
        if path.isdir(tmp_location):
            self.current_location = tmp_location
            os.chdir(self.current_location)
        elif path.isfile(tmp_location):
            self.return_text = f"{self.text} is a file!!"
        else:
            self.return_text = "Invaild location!!" 

        # print(self.home_location)

    def print_working_directory(self):
        self.return_text = self.current_location

    def list_working_directory(self):
        dir_list = os.listdir(self.current_location)

        for n, txt in enumerate(dir_list):
            self.return_text += f"{n}) {txt}\n"

    def open_file(self):
        dir_list = os.listdir(self.current_location)
        for n, txt in enumerate(dir_list):
            if self.text == txt.lower():
                self.text = txt
            elif self.text == str(n):
                self.text = txt
            else:
                pass
        tmp_location = path.join(self.current_location, self.text)
        tmp_location = path.realpath(tmp_location)
        if path.isdir(tmp_location):
            self.return_text = f"{self.text} is a directory!!"
            # os.chdir(self.current_location)
        elif path.isfile(tmp_location):
            os.startfile(tmp_location)
        else:
            self.return_text = "Invaild file!!"

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
