import os

fps = 30.0
keydown = 3
keyup = 4
i = 0

os.system("sleep 5")

while i <= 800: 
    os.system("xdotool keydown space")
    os.system("sleep " + str(keydown / fps))
    os.system("xdotool keyup space")
    os.system("sleep " + str(keyup / fps))
    i += 1
