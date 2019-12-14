import discord
import asyncio
from credentials import email, password
import datetime

client = discord.Client()

channels_to_delete = [1, 2, 3, 4, 6, 7, 10, 11, 13, 14, 15, 16, 21, 22, 24, 25, 26, 27, 29, 31, 34, 36, 39, 42, 43] # default drb channels
# channels_to_delete = [0, 2, 3, 4, 5, 6, 7, 11] # default dinfoarm channels
start_idx = 37

mydate = datetime.datetime(2019, 6, 6)

async def delete_messages(channel):
  print(channel.name)
  async for message in client.logs_from(channel, limit=1000000, after=mydate):
    if (message.author == client.user):
      await client.delete_message(message)

async def get_servers():
  await client.wait_until_ready()
  servers = client.servers
  client.close()
  return servers

async def get_channels():
  servers = await get_servers()
  server = [server for server in servers if server.id == '218820487105478657'][0]
  channels = server.channels
  return channels

async def delete_all_messages():
  channels = await get_channels()

  for idx, channel in enumerate(channels):
    print(idx)
    if (idx >= start_idx):
      await delete_messages(channel)

client.loop.create_task(delete_all_messages())
client.run(email, password)
