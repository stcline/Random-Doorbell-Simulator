#This script asks the user to input the minimum and maximum number of seconds between doorbell rings. It then simulates a doorbell ringing at random intervals between the minimum and maximum number of seconds. The script will run until the user presses Ctrl-C to stop it.

import time
import random
import vlc
p = vlc.MediaPlayer("<filepath to the project directory>\doorbell_sound.mp3")

def doorbell_sim():
    min_time = int(input("Enter the minimum number of seconds between doorbell rings: "))
    max_time = int(input("Enter the maximum number of seconds between doorbell rings: "))
    while True:
        print("Ding dong!")
        p.play()
        time.sleep(random.randint(min_time, max_time))
        p.stop()
