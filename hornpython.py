
#############################
# Python Horn Sound Player
# Author Michael McCullough
#############################

import os
import time
import gpiozero
from gpiozero import Button
import random
from signal import pause
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer

relay_pin = 4
relay = gpiozero.OutputDevice(relay_pin, active_high=False, initial_value=True)
relay.off()

button_back = Button(20)
button_forward = Button(21)
button_play = Button(16)

sound_array = ['1-21-gigawatts.mp3', 'austin_behave.mp3', 'chewbaca-1.mp3',
               'darthvader_circleiscomplete.mp3', 'doc-88-miles-per-hour.mp3', 
               'fifth-element-meat.mp3', 'knight-all-systems.mp3', 
               'luke-leiya.mp3', 'chewbacca.mp3', 'chewbaca-1.mp3', 'darthvader_circleiscomplete.mp3',
               'mario-1up-wii.wav', 'mario-coin-sound.mp3', 'mario-invincible.mp3', 'mario-jump-sound.mp3', 
               'pikachu-pika.mp3', 'r2d2.mp3', 'robocop-thankyou.mp3',
               'star-trek-theme.mp3', 'terminator-cybernetic.mp3', 'thx.mp3',
               'trek-space-the-final.mp3', 'vader-iam-your-father.mp3','yoda_doordonot.mp3']

array_length = len(sound_array)

count = 0
count2 = 0

mixer.init()

def stop_sound():
    mixer.music.stop()

def play_sound():
    global count
    global count2
    # print(count+1)
    
    print("%s"%sound_array[count])
    
    mixer.music.load("./sounds/%s"%sound_array[count])
    
    relay.on() #Turn on the speaker PA
    time.sleep(.5)
    mixer.music.play()
    
    count2 = random.randint(0, array_length-1)
    
    if(count2 == count):
        print('There was a duplicate. Spin again.')
        count2 = random.randint(0, array_length-1)
    count = count2

    while mixer.music.get_busy():
        time.sleep(.5)
    relay.off()

def selec_next(button):
    global count
    if (count < array_length-1):
            count = count + 1
            print(count+1)
    try:
        stop_sound()
    except Exception:
        print("Sound was unable to stop")

    

def select_prev(button):
    global count
    if (count > 0):
        count = count - 1
        print(count+1)
    try:
        stop_sound()
    except Exception:
        print("Sound was unable to stop")

button_forward.when_pressed = selec_next
button_back.when_pressed = select_prev
button_play.when_pressed = play_sound

pause()
