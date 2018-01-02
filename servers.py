import discord
import asyncio
from credentials import email, password

client = discord.Client()

async def get_servers():
    await client.wait_until_ready()
    servers = client.servers
    client.close()
    return servers

# async def print_servers():
#     servers = await get_servers()
#     for server in servers:
#         print(server.name)
#         print(server.id)
#     await client.logout()

async def print_channels():
    servers = await get_servers()
    drb = [server for server in servers if server.id == '218820487105478657'][0]
    channels = drb.channels
    for idx, channel in enumerate(channels):
        print(channel.name)
        print(idx)
    await client.logout()

client.loop.create_task(print_channels())
client.run(email, password)
