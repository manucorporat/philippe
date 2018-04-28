#!/usr/bin/env python

from .philippe import Philippe
from .server import Server

def main():
  bot = Philippe()
  bot.start()

  server = Server(bot)
  server.run()

if __name__ == "__main__":
  main()
