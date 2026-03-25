import machine
import utime
from machine import I2C, Pin, PWM

# ==========================================
# MINI LCD DRIVER (Built-in to avoid errors)
# ==========================================
class SimpleLCD:
    def __init__(self, i2c, addr=0x27):
        self.i2c = i2c
        self.addr = addr
        self.init_lcd()

    def write_cmd(self, cmd):
        self.i2c.writeto(self.addr, bytes([(cmd & 0xF0) | 0x08 | 0x04]))
        self.i2c.writeto(self.addr, bytes([(cmd & 0xF0) | 0x08]))
        self.i2c.writeto(self.addr, bytes([((cmd << 4) & 0xF0) | 0x08 | 0x04]))
        self.i2c.writeto(self.addr, bytes([((cmd << 4) & 0xF0) | 0x08]))

    def write_data(self, data):
        self.i2c.writeto(self.addr, bytes([(data & 0xF0) | 0x09 | 0x04]))
        self.i2c.writeto(self.addr, bytes([(data & 0xF0) | 0x09]))
        self.i2c.writeto(self.addr, bytes([((data << 4) & 0xF0) | 0x09 | 0x04]))
        self.i2c.writeto(self.addr, bytes([((data << 4) & 0xF0) | 0x09]))

    def init_lcd(self):
        for cmd in [0x33, 0x32, 0x28, 0x0C, 0x06, 0x01]:
            self.write_cmd(cmd)
            utime.sleep_ms(5)

    def clear(self):
        self.write_cmd(0x01)

    def message(self, text):
        for char in text:
            if char == '\n':
                self.write_cmd(0xC0)
            else:
                self.write_data(ord(char))

# ==========================================
# SECURITY SYSTEM CODE
# ==========================================

# 1. Hardware Setup
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
lcd = SimpleLCD(i2c)
buzzer = PWM(Pin(15))
buzzer.duty_u16(0)

# Keypad Setup
row_pins = [Pin(2, Pin.OUT), Pin(3, Pin.OUT), Pin(4, Pin.OUT), Pin(5, Pin.OUT)]
col_pins = [Pin(6, Pin.IN, Pin.PULL_DOWN), Pin(7, Pin.IN, Pin.PULL_DOWN), 
            Pin(8, Pin.IN, Pin.PULL_DOWN), Pin(9, Pin.IN, Pin.PULL_DOWN)]

keys = [['1','2','3','A'],['4','5','6','B'],['7','8','9','C'],['*','0','#','D']]

# 2. System Variables
SECRET_PIN = "123456"
current_input = ""

def beep(f, d):
    buzzer.freq(f)
    buzzer.duty_u16(30000)
    utime.sleep_ms(d)
    buzzer.duty_u16(0)

def get_key():
    for r in range(4):
        row_pins[r].value(1)
        for c in range(4):
            if col_pins[c].value() == 1:
                beep(1000, 100)
                while col_pins[c].value() == 1: utime.sleep_ms(10)
                row_pins[r].value(0)
                return keys[r][c]
        row_pins[r].value(0)
    return None

# 3. Main Logic
lcd.clear()
lcd.message("ENTER PIN:")

while True:
    key = get_key()
    
    if key:
        if key in "0123456789" and len(current_input) < 6:
            current_input += key
            # Show a star for each number
            lcd.clear()
            lcd.message("ENTER PIN:\n" + ("*" * len(current_input)))
            
        if len(current_input) == 6:
            utime.sleep_ms(500)
            lcd.clear()
            
            if current_input == SECRET_PIN:
                lcd.message("ACCESS GRANTED")
                beep(2000, 1000)
            else:
                lcd.message("WRONG PIN!\nALERT! ALERT!")
                for i in range(5):
                    beep(400, 200)
                    utime.sleep_ms(100)
                    beep(800, 200)
            
            utime.sleep(2)
            current_input = ""
            lcd.clear()
            lcd.message("ENTER PIN:")
            
        if key == "*": # Reset button
            current_input = ""
            lcd.clear()
            lcd.message("ENTER PIN:")

    utime.sleep_ms(20)