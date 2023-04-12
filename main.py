from caller import *
import os
import time
import keyboard
COLOR_RED = '\033[31m'
COLOR_GREEN = '\033[32m'
COLOR_YELLOW = '\033[33m'
COLOR_BLUE = '\033[34m'
COLOR_MAGENTA = '\033[35m'
COLOR_CYAN = '\033[36m'
COLOR_RESET = '\033[0m'

choice = None
while True:
    print("(1:Easy, 2:Medium, 3:Hard, 4:Extreme)")
    choice = input("Enter your choice: ")
    if choice in ("1","2","3","4"):
        break
if choice:    
    word_index = 0
    char_index=0
    words = []
    os.system('clear')
    if "1" in choice:
        words = ParaGraphGeneratorEasy().split()
        CurrentWord = words[word_index]
        words_to_display = word_index + 10
        for i in range(words_to_display):
            if i == word_index:
                for j in range(len(words[i])):
                    if j == char_index:
                        print(COLOR_RED +words[i][j]+ COLOR_RESET,end='')
                    else:
                        print(words[i][j],end='')
            else:
                print(words[i],end=' ')