# Version 2
# Hier wird nur ein F20-F24 Knopfdruck an den angeschlossenen
# Computer gesendet. Wie eine erweiterte Tastatur. Das Programm
# Clippy kann diese aufnehmen und entsprechende Befehle ausführen.

import board
import digitalio
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)

#Taste: 
taste1 = digitalio.DigitalInOut(board.GP16)
taste1.switch_to_input(pull=digitalio.Pull.DOWN)
#Taste:
taste2 = digitalio.DigitalInOut(board.GP17)
taste2.switch_to_input(pull=digitalio.Pull.DOWN)
#Taste:
taste3 = digitalio.DigitalInOut(board.GP18)
taste3.switch_to_input(pull=digitalio.Pull.DOWN)
#Taste:
taste4 = digitalio.DigitalInOut(board.GP19)
taste4.switch_to_input(pull=digitalio.Pull.DOWN)
#Taste:
taste5 = digitalio.DigitalInOut(board.GP20)
taste5.switch_to_input(pull=digitalio.Pull.DOWN)

while True:
    if taste5.value: #TOP
        kbd.send(Keycode.F20)
        time.sleep(0.2)
    elif taste3.value: #JUNGLE
        kbd.send(Keycode.F21)
        time.sleep(0.2)
    elif taste4.value: #MID
        kbd.send(Keycode.F22)        
        time.sleep(0.2)
    elif taste2.value: #SUPPORT
        kbd.send(Keycode.F23)
        time.sleep(0.2)
    elif taste1.value: #BOT
        kbd.send(Keycode.F24)
        time.sleep(0.2)
    
