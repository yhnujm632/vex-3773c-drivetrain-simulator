import time

class Debug:
    def __init__(self, a=None, b=None):
        pass
    def log(strin=None):
        print(strin)

class Brain:
    screen = ""
    def __init__(self):
        pass

class FontType:
    MONO20 = ""
    def __init__(self):
        pass



class Motor:
    def __init__(self):
        pass
    def set_velocity(self, value, type=0):
        pass
    def spin(self, direction):
        pass
    def stop(self):
        pass
class Piston:
    def __init__(self):
        pass
    def set(self, bool):
        pass

RPM = 2
PERCENT = 0
FORWARD = 1
REVERSE = -1
MM = 0.1
SECONDS = 1
MS = 0.001
DEGREES = 0

def wait(value, unit):
    time.sleep(value * unit)
