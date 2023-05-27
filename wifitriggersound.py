
#############################
# Python Horn Sound Player
# Author Michael McCullough
#############################

import os
import sys
import time
import random
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer

sound_array = ['1-21-gigawatts.mp3', 'austin_behave.mp3', 'chewbaca-1.mp3',
               'darthvader_circleiscomplete.mp3', 'doc-88-miles-per-hour.mp3', 
               'fifth-element-meat.mp3', 'knight-all-systems.mp3', 
               'luke-leiya.mp3', 'chewbacca.mp3', 'chewbaca-1.mp3', 'darthvader_circleiscomplete.mp3',
               'mario-1up-wii.wav', 'mario-coin-sound.mp3', 'mario-invincible.mp3', 'mario-jump-sound.mp3', 
               'pikachu-pika.mp3', 'r2d2.mp3', 'robocop-thankyou.mp3',
               'star-trek-theme.mp3', 'terminator-cybernetic.mp3', 'thx.mp3',
               'trek-space-the-final.mp3', 'vader-iam-your-father.mp3','yoda_doordonot.mp3']

array_length = len(sound_array)
if len(sys.argv) > 1 and int(sys.argv[1]) <= array_length-1:
    count = int(sys.argv[1])
else:
    count = random.randint(0, array_length-1)

mixer.init()

def play_sound():
    global count
    
    print("%s"%sound_array[count])
    
    mixer.music.load("./sounds/%s"%sound_array[count])
    mixer.music.play()
    while mixer.music.get_busy():
        time.sleep(1)
        print("playing")

play_sound()