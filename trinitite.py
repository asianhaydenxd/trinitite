import discord
import sms
import os
import dotenv
from ipaddress import IPv4Address
from discord.ext import commands, tasks

# Load .env into shell env variables
dotenv.load_dotenv()

# Get env variables as constants
TOKEN = os.getenv("TOKEN")
PHONE = os.getenv("PHONE")
IP = IPv4Address(os.getenv("IP"))
CHANNEL = os.getenv("CHANNEL")

# Initialize client
client = discord.Client()

# Initialize Trinitite
trinitite = sms.Trinitite(PHONE, IP)

# Run upon bot startup
@client.event
async def on_ready():
    print(f"{client.user} connected to discord")
    trinitite.send_msg("trinitite notice:::trinitite is initialized")
    get_messages.start()

@client.event
@commands.has_role("Trinitite")
async def on_message(message):
    if message.author == client.user: return

    if message.content.startswith(":s "):
        for_nils = message.content[3:]
        trinitite.send_msg(f"{message.author.name} » {for_nils}")
        await message.channel.send(f"{message.author.name} » {for_nils}")

@tasks.loop(seconds = 5)
async def get_messages():
    channel = client.get_channel(int(CHANNEL))

    def phone_to_name(phone):
        if phone.startswith("+1"):
            return "Hayden"
        return "Nils"

    msgs = trinitite.fetch_msgs()
    
    if msgs:
        await channel.send("\n".join([f"{phone_to_name(msg.name)} » {msg.content}" for msg in msgs]))
    
    if "bye discord" in [msg.content for msg in msgs]:
        trinitite.send_msg("trinitite notice:::trinitite is terminated")
        exit()

# Run defined client methods with the token
client.run(TOKEN)
