import os
import time 
import sleep
from gpiozero import Button
from signal import pause
from pygame import mixer

button_back = Button(20)
button_forward = Button(21)
button_play = Button(2)
count = 0
sound_array = ['sound1', 'sound2', 'sound3', 'sound4', 'sound5', 'sound6', 'sound7', 'sound8', 'sound9']
array_length = len(sound_array)

print(len(sound_array))

mixer.init()

def stop_sound():
    mixer.music.stop()

def play_sound():
    try:
        stop_sound()
    except Exception:
        print("Sound was unable to stop")

    mixer.music.load("/home/smartcar/smarthorn/sounds/{0}.mp3").format(sound_array[count])
    mixer.music.play()
    while mixer.music.get_busy():
        time.sleep(1)
   
def selec_next(button):
    try:
        stop_sound()
    except Exception:
        print("Sound was unable to stop")

    print(button.pin)
    if (count < array_length):
        count = count + 1

def select_prev(button):
    try:
        stop_sound()
    except Exception:
        print("Sound was unable to stop")

    print(button.pin)
    if (count > 0):
        count = count - 1

def play_sound_old(button):
    print(button.pin)
    currentsound = sound_array[count]

button_forward.when_pressed = selec_next
button_back.when_pressed = select_prev
button_play.when_pressed = play_sound

#TODO setup the relays and delays / actions