import math

def distance(a, b):
  return math.sqrt((a*a) + (b*b))

def y_rotation(x, y, z):
  radians = math.atan2(x, distance(y, z))
  return -math.degrees(radians)

def x_rotation(x, y, z):
  radians = math.atan2(y, distance(x, z))
  return math.degrees(radians)

