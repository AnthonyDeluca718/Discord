import discord
import asyncio
from credentials import email, password
import datetime

client = discord.Client()
start_idx = 13

# mydate = datetime.datetime(2019, 6, 6)

async def get_server():
    await client.wait_until_ready()
    servers = client.private_channels
    server = [x for x in servers if x.id == '222972002195996674'][0]
    client.close()
    return server

async def get_messages():
    server = await get_server()
    messages = client.logs_from(server, limit=100000)
    client.close()
    return messages

async def do_stuff():
    messages = await get_messages()
    async for message in messages:
      if (message.author == client.user):
        await client.delete_message(message)
    await client.logout()

client.loop.create_task(do_stuff())
client.run(email, password)
