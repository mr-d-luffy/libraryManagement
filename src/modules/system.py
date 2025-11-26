# inbuilt modules of python
from json import load
from colorama import Fore
from pygame import mixer
from datetime import datetime


# loading of api file
try:
    api = load(open("api/data.json"))
except(Exception) as e:
    print(Fore.RED, "File Path Error", Fore.RESET)

# syatem class they control system tasks
class system():
    # playsound using this method
    @staticmethod
    def playsound(file):
        """THIS FUNCTION PLAYING A AUDIO FILE
        1.first your systen have pygame module
        2.if you don't have pygame install it
        3.CMD `pip3 install pygame`
        4.import playsoung module
        5.enjoy the playing audio simple format 
        """
        mixer.init()
        mixer.music.load(file)
        mixer.music.play()
        while mixer.music.get_busy():
            pass
        mixer.quit()

    @staticmethod
    def currentDate():
        return str(datetime.now().date())
    
    @staticmethod
    def currentTime():
        return str(datetime.now().time())
    

# testing of functions
if __name__=="__main__":
    s = system()
    print(s.currentDate())

