import math

def modulo(a, b):
  return math.sqrt((a*a) + (b*b))

def y_rotation(x, z):
  radians = math.atan2(z, x)
  return math.degrees(radians)

def x_rotation(x, y, z):
  radians = math.atan2(y, modulo(x, z))
  return math.degrees(radians)

