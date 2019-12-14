import discord
import asyncio
from credentials import email, password

client = discord.Client()

async def get_servers():
    await client.wait_until_ready()
    servers = client.private_channels
    client.close()
    return servers

async def print_stuff():
    servers = await get_servers()
    for server in servers:
        print(server.recipients[0].name)
        # print(server.recipients[1].name)
        print(server.id)
    await client.logout()
    
client.loop.create_task(print_stuff())
client.run(email, password)

# 218820487105478657 drb
# 260623337292693504 dinofarm
