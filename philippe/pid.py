class PID:
  def __init__(self, P, I, D):
    self.KP = P
    self.KI = I
    self.KD = D
    self.target = 0

    self.lastError = 0
    self.integrator = 0

  def setTarget(self, newTarget):
    self.target = newTarget
    self.integrator = 0

  def step(self, currentValue):
    error = currentValue - self.target

    output = (self.KP * error + self.KI * self.integrator + self.KD * (error - self.lastError))

    self.lastError = error
    self.integrator += error
    return output
