from mpu6050 import mpu6050
from time import sleep
from .pid import PID
import math
import RPi.GPIO as GPIO
from .utils import y_rotation

PWA_FREQ = 100

ENGINE_PWM = 12

ENGINE_RIGHT_DIR = 27
ENGINE_LEFT_DIR = 22

#K and K1 --> Constants used with the complementary filter
K = 0.98
K1 = 1 - K

TIME_DIFF = 0.02
ITerm = 0

class Engine():

  def __init__(self, pipe):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(ENGINE_LEFT_DIR, GPIO.OUT)
    GPIO.setup(ENGINE_RIGHT_DIR, GPIO.OUT)
    GPIO.setup(ENGINE_PWM, GPIO.OUT)

    self.wheelPWM = GPIO.PWM(ENGINE_PWM, PWA_FREQ)

    self.sensor = mpu6050(0x68)
    self.pid = PID(P=20, I=0, D=0)
    self.pipe = pipe
    self.last_x = 0
    gyro_data = self.sensor.get_gyro_data()
    self.gyro_offset_x = gyro_data['x']
    self.gyro_offset_y = gyro_data['y']
    self.gyro_offset_z = gyro_data['z']
    self.gyro_total_y = 0
    # self.gyro_total_z = 0

    self.wheelPWM.start(0)
    GPIO.output(ENGINE_LEFT_DIR, False)
    GPIO.output(ENGINE_RIGHT_DIR, False)

  def run(self):
    while True:
      self.step()
      sleep(TIME_DIFF)

  def setWheel(self, vel):
    GPIO.output(ENGINE_LEFT_DIR, vel > 0)
    GPIO.output(ENGINE_RIGHT_DIR, vel < 0)
    self.wheelPWM.ChangeDutyCycle(min(math.fabs(vel), 100))

  def balance(self):
    accel_data = self.sensor.get_accel_data()
    gyro_data = self.sensor.get_gyro_data()

    accelX = accel_data['x']
    accelZ = accel_data['z']
    # print("accel x:{:+.2f} y:{:+.2f} z:{:+.2f}".format(accel_data['x'], accel_data['y'], accel_data['z']))

    gyroY = gyro_data['y'] - self.gyro_offset_y
    # print("giro x:{:+.2f} y:{:+.2f} z:{:+.2f}".format(gyroX, gyroY, gyroZ))

    gyro_y_delta = (gyroY * TIME_DIFF)
    self.gyro_total_y += gyro_y_delta
    rotation_x = y_rotation(accelX, accelZ)
    # print("giro angle:{:+.2f} giro:{:+.2f}".format(rotation_x, gyro_y_delta))

    # Complementary Filter
    self.last_x = K * (self.last_x + gyro_y_delta) + (K1 * rotation_x)

    # setting the PID values. Here you can change the P, I and D values according to yiur needs
    self.pid.update(self.last_x)
    return self.pid.output

  def step(self):
    output = self.balance()
    print("output {}".format(output))

    self.setWheel(output)
    #self.setLWheel(output)
    #self.setRWheel(output)
