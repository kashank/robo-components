import RPi.GPIO as gpio
import time

class Motor:
    pwm_pin = 7 #TODO import this info from a config file
    motor_pin = 9 #TODO import this info from a config file

    gpio.setmode(gpio.BOARD)
    gpio.setup(pwm_pin, gpio.OUT) #TODO import this info from a config file
    gpio.setup(motor_pin, gpio.OUT)
    pwm = gpio.PWM(pwm_pin, 1000)

    gpio.output(pwm_pin, True) #TODO import this info from a config file

    def __init__(self):
        self.pwm.start(100)

    #speed should be between 1-100 and will be rounded to nearest end if not
    def turn(self, speed: int):
        if speed < 1:
            speed=1
        if speed > 100:
            speed =100
            
        gpio.output(self.motor_pin, True)
        gpio.output(self.pwm_pin, speed)

    def stop(self):
        gpio.output(self.motor_pin, False)