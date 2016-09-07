from PCA9685 import Driver
import time

class Motion:
    driver = Driver()
    pwm_1 = driver.CHANNEL_0  # Motor A direction
    pwm_2 = driver.CHANNEL_1  # Motor A speed
    pwm_3 = driver.CHANNEL_2  # Motor B direction
    pwm_4 = driver.CHANNEL_3  # Motor B speed

    def __init__(self):
        self.driver.setFrequency(1000)

    def int_to_motor_speed(self, speed):
        if speed < 0:
            cleaned_speed = 0 
        elif speed > 100:
            cleaned_speed = 100
        else:
            cleaned_speed= speed
        return 4095 * cleaned_speed / 100 
    
    def forward(self, speed):
        motor_speed = self.int_to_motor_speed(speed)
        self.driver.setOn(self.pwm_1)
        self.driver.setPWM(self.pwm_2, motor_speed)
        self.driver.setOff(self.pwm_3)
        self.driver.setPWM(self.pwm_4, motor_speed)

    def backward(self, speed):
        motor_speed = self.int_to_motor_speed(speed)
        self.driver.setOff(self.pwm_1)
        self.driver.setPWM(self.pwm_2, motor_speed)
        self.driver.setOn(self.pwm_3)
        self.driver.setPWM(self.pwm_4, motor_speed)

    def left(self, speed):
        motor_speed = self.int_to_motor_speed(speed)
        self.driver.setOn(self.pwm_1)
        self.driver.setPWM(self.pwm_2, motor_speed)
        self.driver.setOn(self.pwm_3)
        self.driver.setPWM(self.pwm_4, motor_speed)

    def right(self, speed):
        motor_speed = self.int_to_motor_speed(speed)
        self.driver.setOff(self.pwm_1)
        self.driver.setPWM(self.pwm_2, motor_speed)
        self.driver.setOff(self.pwm_3)
        self.driver.setPWM(self.pwm_4, motor_speed)

    def stop(self):
        self.driver.setPWM(self.pwm_2, 0)
        self.driver.setPWM(self.pwm_4, 0)

