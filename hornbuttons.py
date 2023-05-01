
#############################
# Python Horn Sound Player
# Author Michael McCullough
#############################

import os
import time 
import sleep
from gpiozero import Button
from signal import pause
from pygame import mixer

count = 0
relay_pin = 4
relay = gpiozero.OutputDevice(relay_pin, active_high=True, initial_value=False)

button_back = Button(20)
button_forward = Button(21)
button_play = Button(16)

sound_array = ['1-21-gigawatts', 'doc-88-miles-per-hour', 
               'mario-coin-sound', 'mario-1up-wii', 
               'mario-invincible-sound', 'mario-jump-sound', 
               'pikachu-pika', 
               'luke-leiya', 'r2d2', 'yoda_doordonot', 'vader-iam-your-father', 'chewbacca', 
               'chewbaca-1', 'darthvader_circleiscomplete', 
               'clint-eastwood', 'knight-all-systems', 'knight-rider-theme'
               'trek-space-the-final', 'star-trek-theme', 
               'terminator-cybernetic', 'robocop-thankyou', 
               'thx', 'fifth-element-meat', 'austin_behave']

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

    relay.on() #Turn on the speaker PA
    time.sleep(.5)
    mixer.music.load("./sounds/{0}.mp3").format(sound_array[count])
    mixer.music.play()
    while mixer.music.get_busy():
        time.sleep(1)
        relay.off()
   
def selec_next(button):
    try:
        stop_sound()
    except Exception:
        print("Sound was unable to stop")

    if (count < array_length):
        count = count + 1

def select_prev(button):
    try:
        stop_sound()
    except Exception:
        print("Sound was unable to stop")

    if (count > 0):
        count = count - 1

button_forward.when_pressed = selec_next
button_back.when_pressed = select_prev
button_play.when_pressed = play_sound