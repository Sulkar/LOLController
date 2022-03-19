#benötigt Circuit Python und passende Module
import board
import digitalio
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

kbd = Keyboard(usb_hid.devices)
kbdLayout = KeyboardLayoutUS(kbd)

nachricht1 = "BOT" #Button BOT
nachricht2 = "SUPPORT" #Button SUPPORT
nachricht3 = "MID" #Button MID
nachricht4 = "JUNGLE" #Button JUNGLE
nachricht5 = "TOP" #Button TOP

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
taste4 = digitalio.DigitalInOut(board.GP20)
taste4.switch_to_input(pull=digitalio.Pull.DOWN)
#Taste:
taste5 = digitalio.DigitalInOut(board.GP22)
taste5.switch_to_input(pull=digitalio.Pull.DOWN)

while True:
    if taste1.value:
        kbdLayout.write(nachricht1)
        kbd.send(Keycode.ENTER)
        time.sleep(0.1)
    elif taste2.value:
        kbdLayout.write(nachricht2)
        kbd.send(Keycode.ENTER)
        time.sleep(0.1)
    elif taste3.value:
        kbdLayout.write(nachricht3)
        kbd.send(Keycode.ENTER)
        time.sleep(0.1)
    elif taste4.value:
        kbdLayout.write(nachricht4)
        kbd.send(Keycode.ENTER)
        time.sleep(0.1)
    elif taste5.value:
        kbdLayout.write(nachricht5)
        kbd.send(Keycode.ENTER)
        time.sleep(0.1)
