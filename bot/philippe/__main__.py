from .philippe import Philippe
from .server import Server

def main():
  bot = Philippe()
  process = bot.start()
  process.join()

  server = Server(bot)
  server.run()

if __name__ == "__main__":
  main()
