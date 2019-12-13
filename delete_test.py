import discord
import asyncio
from credentials import email, password
import datetime

mydate = datetime.datetime(2017,12, 1)
print(mydate)

client = discord.Client()

async def get_servers():
  await client.wait_until_ready()
  servers = client.servers
  client.close()
  return servers

async def get_channels():
  servers = await get_servers()
  print( client.user )
  server = [server for server in servers if server.id == 'insert_id'][0]
  channels = server.channels
  return channels1

async def delete_messages():
  channels = await get_channels()
  current = list(channels)[17] # index of the channel
  print(current.name)
  async for message in client.logs_from(current, limit=1000000, after=mydate):
    if (message.author == client.user):
      await client.delete_message(message)
  await client.logout()

client.loop.create_task(delete_messages())
client.run(email, password)
z
