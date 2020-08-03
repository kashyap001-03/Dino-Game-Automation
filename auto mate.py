import pyautogui
from PIL import Image,ImageGrab
#from numpy import asarray
import time

#for cacuts
def isCollide(data):
    for i in range(526,549):  # this is for to dected the image pixesl at some point given by you
        for j in range(207,230):
            if data[i, j] < 99:
                return True
#for birds
def birdscollide(data):
    for i in range(444, 459):  # this is for to dected the image pixesl at some point given by you
        for j in range(177, 209):
             if data[i, j] < 99:
                 return

def nightbirdscollide(data):
    for i in range(444, 459):  # this is for to dected the image pixesl at some point given by you
        for j in range(177, 209):
             if data[i, j] > 250:
                 return

def nightcollide(data):
    for i in range(526,549):  # this is for to dected the image pixesl at some point given by you
        for j in range(207,230):
            if data[i, j] < 250:
                return True





def hit(key):
    pyautogui.keyDown(key)

#def takescreen():
    #image = ImageGrab.grab().convert('L')
    #return image


if __name__ == "__main__":
    print("Game start in 5 seconds")
    time.sleep(2)
    hit('up')
    while True:
        #image = takescreen()
        image = ImageGrab.grab().convert('L') # here def function u will also written
        data = image.load()  #load image in array from
        if isCollide(data):
            hit('up')
        elif birdscollide(data):
            hit('down')
        elif nightcollide(data):
            hit('up')
        elif nightbirdscollide(data):
            hit('down')
        #draw rectangle for cacutus
'''        
        for i in range(485, 509): #this is for to dected the image pixesl at some point given by you
             for j in range(212,230):
                  data[i,j] = 0  #To change the cordinates of data
        #draw rectangle for birds
        for i in range(485, 509): #this is for to dected the image pixesl at some point given by you
             for j in range(186,192):
                 data[i,j] = 0
'''
    #image.show()