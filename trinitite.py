import discord
import sms
import os
import dotenv
from ipaddress import IPv4Address

# Load .env into shell env variables
dotenv.load_dotenv()

# Get env variables as constants
TOKEN = os.getenv("TOKEN")
PHONE = os.getenv("PHONE")
IP = IPv4Address(os.getenv("IP"))

# Initialize client
client = discord.Client()

# Initialize Trinitite
trinitite = sms.Trinitite(PHONE, IP)

# Run upon bot startup
@client.event
async def on_ready():
    print(f"{client.user} connected to discord")

@client.event
async def on_message(message):
    if message.author == client.user: return

    if message.content.startswith(":s "):
        for_nils = message.content[3:]
        trinitite.send_msg(for_nils)
        await message.channel.send("Test")

# Run defined client methods with the token
client.run(TOKEN)
