import RPi.GPIO as GPIO
import os
import glob
import time
from lcd import LCD
from pi import Pi

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
#points to the location of the temperature data
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
#reads the data from the sensor and converts it into readable data
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_f = float(temp_string) / 1000.0
        print(temp_f)
        temp_c = (temp_f - 32.0) * (5.0 / 9.0)
        print(temp_c)
        return temp_c, temp_f

while True:
        print(read_temp())
        time.sleep(1)



def destroy():
    lcd.destroy()



if __name__=='__main__':
    def loop():
        global lcd
        print("lcd LOADED")
        lcd = LCD()
        lcd.clear()
        lcd.message("Hello")
