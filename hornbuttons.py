import os
import time 
import sleep
from gpiozero import Button
from signal import pause
from pygame import mixer

count = 0
relay_pim = 4
relay = gpiozero.OutputDevice(relay_pin, active_high=True, initial_value=False)
button_back = Button(20)
button_forward = Button(21)
button_play = Button(16)
sound_array = ['sound1', 'sound2', 'sound3', 'sound4', 'sound5', 'sound6', 'sound7', 'sound8', 'sound9']
#TODO change to directory of mp3 sounds and build the array from there?
array_length = len(sound_array)

print(relay.value)
print(len(sound_array))

mixer.init()

def stop_sound():
    mixer.music.stop()

def play_sound():
    try:
        stop_sound()
    except Exception:
        print("Sound was unable to stop")
    relay.on() #Turn on the speaker PA
    time.sleep(.5)
    mixer.music.load("/home/smartcar/smarthorn/sounds/{0}.mp3").format(sound_array[count])
    mixer.music.play()
    while mixer.music.get_busy():
        time.sleep(1)
        relay.off()
   
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