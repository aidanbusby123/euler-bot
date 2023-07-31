import discord
import openai
import os
openai.api_key = os.getenv('OPENAI_TOKEN')
bot = discord.Client(intents=discord.Intents.all())

def chatgpt_request(prompt, model='gpt-3.5-turbo'):
  response = openai.ChatCompletion.create(
    model = model,
    messages = [{"role" : "user", "content": prompt}],
    temperature = 0.5,
  )
  return response['choices'][0]['message']['content']

@bot.event
async def on_ready():
  print(bot.user)


@bot.event
async def on_message(message):
  if message.author != bot.user:
    if bot.user.mention in message.content:
      prompt = message.content
      response = chatgpt_request(prompt)
      await message.channel.send(response)


bot.run(os.getenv('DISCORD_TOKEN'))
