from caller import *
import os
import time
from pynput import keyboard


COLOR_RED = '\033[31m'
COLOR_GREEN = '\033[32m'
COLOR_YELLOW = '\033[33m'
COLOR_BLUE = '\033[34m'
COLOR_MAGENTA = '\033[35m'
COLOR_CYAN = '\033[36m'
COLOR_RESET = '\033[0m'
class Typing:
    def __init__(self):
        self.current_key = None  
        self.cursor = 0
        self.current_word = 0
        self.para = None

    def on_press(self,key):
        try:
            self.cursor += 1
            self.current_key = key.char      
        except AttributeError:
            if key == key.backspace:
                if self.cursor > 0:
                    self.curor -= 1
                else:
                    self.cursor = 0
            if key == key.space:
                self.cursor = 0
                self.current_word += 1

    def start_tracking(self):
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()     
           
    def print_para(self):
        pass

    def get_para(self):
        self.para = ParaGraphGeneratorEasy().split()

    

    # choice = None
    # while True:
    #     print("(1:Easy, 2:Medium, 3:Hard, 4:Extreme)")
    #     choice = input("Enter your choice: ")
    #     if choice in ("1","2","3","4"):
    #         break
    # if choice:    
    #     word_index = 0
    #     words = []
    #     os.system('clear')
    #     if "1" in choice:
    #         words = ParaGraphGeneratorEasy().split()

    #         # Tracking starts
    #         CurrentWord = words[word_index]
    #         cursor = 0            
            

        
obj = Typing()
obj.start_tracking()