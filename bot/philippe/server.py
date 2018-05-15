import asyncio
import websockets


class Server:
  def __init__(self, bot):
    self.bot = bot
    self.server = websockets.serve(self.loop, '0.0.0.0', 8765)

  def run(self):
    asyncio.get_event_loop().run_until_complete(self.server)
    asyncio.get_event_loop().run_forever()

  async def loop(self, websocket):
    cmd = await websocket.recv()
    self.bot.command(cmd)
    print(cmd)