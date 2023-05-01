import os
import random
import time import sleep
from gpiozero import Button

button = Button(2)

sound_array = ['sound1', 'sound2', 'sound3', 'sound4', 'sound5', 'sound6', 'sound7', 'sound8', 'sound9']

while True:
        button.wait_for_press()
        random_sound =random.choice(sound_array)
        os.system("aplay /home/smartcar/smarthorn/sounds/{0}.mp3".format(random_sound))