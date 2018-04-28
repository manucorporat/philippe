from mpu6050 import mpu6050
from time import sleep
from .pid import PID
import math
import RPi.GPIO as GPIO
from .utils import x_rotation, y_rotation, distance

PWA_FREQ = 100

PIN_GPIO_LEFT = 1
PIN_GPIO_RIGHT = 2

PIN_PWM_LEFT = 1
PIN_PWM_RIGHT = 2

#K and K1 --> Constants used with the complementary filter
K = 0.98
K1 = 1 - K

TIME_DIFF = 0.02
ITerm = 0

class Engine():

  def __init__(self, pipe):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(PIN_GPIO_LEFT, GPIO.OUT)
    GPIO.setup(PIN_GPIO_RIGHT, GPIO.OUT)

    self.leftPWM = GPIO.PWM(PIN_PWM_LEFT, PWA_FREQ)
    self.rightPWM = GPIO.PWM(PIN_PWM_RIGHT, PWA_FREQ)

    self.sensor = mpu6050(0x68)
    self.pid = PID(P=-78.5, I=1.0, D=1.0)
    self.pipe = pipe
    self.last_x = 0
    self.gyro_offset_x = 0
    self.gyro_offset_y = 0
    self.gyro_total_x = 0
    self.gyro_total_y = 0

    self.leftPWM.start(0)
    self.rightPWM.start(0)

  def run(self):
    while True:
      self.step()
      sleep(TIME_DIFF)

  def setLWheel(self, vel):
    GPIO.output(PIN_GPIO_LEFT, vel < 0)
    self.leftPWM.ChangeDutyCycle(math.fabs(vel) * 100.0)

  def setRWheel(self, vel):
    GPIO.output(PIN_GPIO_RIGHT, vel < 0)
    self.rightPWM.ChangeDutyCycle(math.fabs(vel) * 100.0)

  def balance(self):
    accel_data = self.sensor.get_accel_data()
    gyro_data = self.sensor.get_gyro_data()

    accelX = accel_data['x']
    accelY = accel_data['y']
    accelZ = accel_data['z']

    gyroX = gyro_data['x']
    gyroY = gyro_data['y']

    gyroX -= self.gyro_offset_x
    gyroY -= self.gyro_offset_y

    gyro_x_delta = (gyroX * TIME_DIFF)
    gyro_y_delta = (gyroY * TIME_DIFF)

    self.gyro_total_x += gyro_x_delta
    self.gyro_total_y += gyro_y_delta

    rotation_x = x_rotation(accelX, accelY, accelZ)

    # Complementary Filter
    self.last_x = K * (self.last_x + gyro_x_delta) + (K1 * rotation_x)

    # setting the PID values. Here you can change the P, I and D values according to yiur needs
    return self.pid.step(self.last_x)

  def step(self):
    output = self.balance()

    self.setLWheel(output)
    self.setRWheel(output)
