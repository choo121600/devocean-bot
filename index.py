import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = os.getenv('CHANNEL_ID')


class MyClient(discord.Client):
	async def on_ready(self):
		channel = self.get_channel(int(CHANNEL_ID))
		await channel.send('DEVOCEAN 봇이 정상적으로 실행되었습니다.')

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(TOKEN)