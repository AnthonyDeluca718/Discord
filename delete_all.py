import discord
import asyncio
from credentials import email, password 

client = discord.Client()

async def delete_messages(channel):
  print(channel.name)
  async for message in client.logs_from(channel, limit=1000000):
    if (message.author == client.user):
      await client.delete_message(message)

async def get_servers():
  await client.wait_until_ready()
  servers = client.servers
  client.close()
  return servers

async def get_channels():
  servers = await get_servers()
  dinofarm = [server for server in servers if server.id == 'channel_id'][0] 
  channels = dinofarm.channels
  return channels

async def delete_all_messages():
  channels = await get_channels()
  print(len(channels))

  for channel in list(channels):
    await delete_messages(channel)

client.loop.create_task(delete_all_messages())
client.run(email, password)