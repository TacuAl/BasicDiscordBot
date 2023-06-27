import discord
from gnews import GNews
import os
from keep_alive import keep_alive
from discord.ext import commands
from datetime import datetime
from music import Player 

intents = discord.Intents.default()

bot = commands.Bot(command_prefix="?", intents=intents)

google_news = GNews()

@bot.event
async def on_ready():
  print(f"{bot.user.name} is ready!")

async def setup():
  await bot.wait_until_ready()
  bot.add_cog(Player(bot))

bot.loop.create_task(setup())

@bot.command()
async def Time(ctx):
  await ctx.send('{} The time is : {}'.format(ctx.author.mention,datetime.now()))

@bot.command() 
@commands.has_permissions(ban_members = True) 
async def Ban(ctx, member:discord.Member, *, reason):
  await member.send('You have been banned by {} for {}'.format(ctx.author.name, reason)) 
  await member.ban() 

@bot.command() 
@commands.has_permissions(kick_members= True) 
async def Kick(ctx,member:discord.Member, *, reason ):
  await member.send('You have been kicked by {} for {}'.format(ctx.author.name, reason)) 
  await member.kick()

@bot.command() 
@commands.has_permissions(ban_members = True)
async def ShowBannedMembers(ctx):
  banned_users = await ctx.guild.bans()
  for ban_entry in banned_users:
    user = ban_entry.user
    await ctx.send('{}#{}'.format(user.name,user.discriminator))

@bot.command() 
@commands.has_permissions(ban_members = True)
async def Unban(ctx, *,member):
  banned_users = await ctx.guild.bans()
  member_name,member_discriminator = member.split('#')
  for ban_entry in banned_users:
    user = ban_entry.user
    if(user.name,user.discriminator) == (member_name,member_discriminator):
      await ctx.guild.unban(user)

@bot.command()
async def News(ctx, *,topic):
  news = google_news.get_news(topic)
  for i in range (3):
    await ctx.send('{} \n {}'.format(news[i]['title'],news[i]['url']))

keep_alive()
bot.run('OTEzNjc2NjkyNjAwNTI0ODMx.YaB9ug.4mAOfNBeOIcXYXoWitQOCxsw3fQ')
