from lcd import LCD
from time import sleep

if __name__ == '__main__':
    print("loaded")
#    lcd = LCD(pin_rs=27, pin_e=22, pins_db = [25, 24, 23, 18])
    lcd=LCD()
    print("lcd object created")
    lcd.clear()
    print('lcd cleared')
    sleep(2)
    lcd.message("Working \n Hello world")
    print('message displayed')
