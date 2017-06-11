from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
button1 = 31
button2 = 33
button3 = 35
button4 = 37
sleeptime = .3

GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while (1):
    if GPIO.input(button1) == 0:
        print ("Button 1 was pressed")
        sleep(sleeptime)
    if GPIO.input(button2) == 0:
        print ("Button 2 was pressed")
        sleep(sleeptime)
    elif GPIO.input(button3) == 0:
        print ("Button 3 was pressed")
        sleep(sleeptime)
    elif GPIO.input(button4) == 0:
        print ("Button 4 was pressed")
        sleep(sleeptime)
