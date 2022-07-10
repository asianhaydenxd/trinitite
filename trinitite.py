import discord
import sms
from ipaddress import IPv4Address

# Get tokens from private folder (not included in git)
with open("private/TOKEN", "r") as tokenfile:
    TOKEN = tokenfile.read()

with open("private/PHONE", "r") as phonefile:
    PHONE = phonefile.read()

with open("private/AIRMORE_IP", "r") as ipfile:
    IP = IPv4Address(ipfile.read())

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
