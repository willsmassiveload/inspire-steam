from machine import Pin
import time

# LED Pins
red_led = Pin(28, Pin.OUT)
yellow_led = Pin(27, Pin.OUT)

# Button Pin
green_btn = Pin(22, Pin.IN, Pin.PULL_UP)

while True:
    button_status = green_btn.value()
    if(button_status == 1):
        red_led.off()
        print("Button released")
    elif(button_status == 0):
        red_led.on()    
        print("Button pressed")
    time.sleep(1) 
    print(button_status)   