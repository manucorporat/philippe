from setuptools import setup

setup(name='philippe bot',
      version='0.1',
      description='The best self-balancing bot ever created',
      url='http://github.com/manucorporat/philippe',
      author='philippe team',
      license='MIT',
      packages=['philippe'],
      install_requires=[
        'mpu6050-raspberrypi',
        'websockets'
      ],
      zip_safe=False)