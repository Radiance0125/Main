import string
import time
import os

clear = lambda: os.system('cls')

x = list(string.ascii_lowercase)
y = [i for i in "hello world"]
word = ""

def make(target):
    global word
    for i in x:
        time.sleep(0.03)
        clear()
        if i == target:
            print(word + i)
            word += i
            break
        else:
            print(word + i)

for i in y:
    if i == " ":
        word += " "
    else:
        make(i)