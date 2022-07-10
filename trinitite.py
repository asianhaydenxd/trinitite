import discord

# Get token from private folder (not included in git)
with open("private/TOKEN", "r") as tokenfile:
    TOKEN = tokenfile.read()

# Initialize client
client = discord.Client()

# Run upon bot startup
@client.event
async def on_ready():
    print(f"{client.user} connected to discord")

# Run defined client methods with the token
client.run(TOKEN)
