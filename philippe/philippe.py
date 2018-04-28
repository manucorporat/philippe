
from multiprocessing import Pipe
from .engine import Engine
from multiprocessing import Process

class Philippe:
  def __init__(self):
    self.conn, self.child_conn = Pipe()

  def start(self):
    p = Process(target=initEngine, args=(self.child_conn, ))
    p.start()
    return p

  def command(self, command):
    self.conn.send(command)

  def go(self, velocity):
    self.command("go:{}".format(velocity))

def initEngine(pipe):
  engine = Engine(pipe)
  engine.run()
