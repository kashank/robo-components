import RPi.GPIO as gpio
import time

class Motor:
    pwm_pin = 7 #TODO import this info from a config file
    motor_pin = 9 #TODO import this info from a config file

    gpio.setmode(gpio.BOARD)
    gpio.setup(pwm_pin, gpio.OUT) #TODO import this info from a config file
    gpio.setup(motor_pin, gpio.OUT)

    gpio.output(pwm_pin, True) #TODO import this info from a config file

    def turn(self, speed):
        gpio.output(self.motor_pin, True)
        gpio.output(self.pwm_pin, speed)

    def stop(self):
        gpio.output(self.motor_pin, False)