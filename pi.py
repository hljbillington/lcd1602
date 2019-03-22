import RPi.GPIO as GPIO
import time

class Pi:

    def __init__(self, board, warnings):
        self.board = board
        self.warnings = warnings

    def set_mode(self):
        if self.board == "BCM":
            GPIO.setmode(GPIO.BCM)
            print("board is set to BCM")
        elif self.board == "BOARD":
            GPIO.setmode(GPIO.BOARD)
            print("board set to BOARD")
        else:
            print("board not set")


    def set_warnings(self):
        if self.warnings == "False":
            GPIO.setwarnings(False)
            print("warnings set to false")
        elif self.warnings == "True":
            GPIO.setwarnings(False)
            print("warning set to True")
        else:
            print("no warnings set")


