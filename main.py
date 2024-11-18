import discord
from discord.ext import commands
import asyncio
from dotenv import load_dotenv
import os
import asyncio

bot = commands.Bot(".", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')



@bot.command("serverinfo")
async def self(ctx):
    embed = discord.Embed(title="Server Information", description=f"**{ctx.guild.name}**")
    embed.set_thumbnail(url=ctx.guild.icon)
    embed.add_field(name="Owner", value=ctx.guild.owner)
    embed.add_field(name="Created At", value=ctx.guild.created_at.strftime("%d-%m-%Y %H:%M:%S"))
    embed.add_field(name="Member Count", value=ctx.guild.member_count, inline=False)
    await ctx.send(embed=embed)
    
    
@bot.command("ban")
@commands.has_permissions(ban_members=True)
async def self(ctx, user:discord.Member = None, reason = "No Reason Given"):
    if (user != None):
        await user.ban(reason)
        await ctx.send(f"Banned {user} for: {reason}")
    else:
        await ctx.send("Please ping the user you are trying to ban")
        
@bot.command("kick")
@commands.has_permissions(kick_members=True)
async def self(ctx, user:discord.Member = None, reason = "No Reason Given"):
    if (user != None):
        await user.kick(reason)
        await ctx.send(f"Kicked {user} for: {reason}")
    else:
        await ctx.send("Please ping the user you are trying to kick")

@bot.command("mute")
@commands.has_permissions(moderate_members = True) #Timeout permission
async def self(ctx, user:discord.Member = None, reason = "No Reason Given", time:float = 1):
    if (user != None):
        muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
        await user.add_roles(muted_role)
        await ctx.send(f"Muted {user} for: {reason} for {time} minutes")
        await asyncio.sleep(time * 60)
        await user.remove_roles(muted_role)
    else:
        await ctx.send("Please ping the user you are trying to mute")
        
@bot.command("unmute")
@commands.has_permissions(moderate_members = True) #Timeout permission
async def self(ctx, user:discord.Member = None):
    if (user != None):
        muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
        await ctx.send(f"Unmuted {user}!")
        await user.remove_roles(muted_role)
    else:
        await ctx.send("Please ping the user you are trying to unmute")    
    
@bot.command("purge")
@commands.has_permissions(manage_messages = True)
async def self(ctx, amount:int = 0):
    if amount == 0:
        await ctx.send("Please specify an amount of messages to purge.")
    else:
        async for msg in ctx.channel.history(limit=amount + 1):
            await msg.delete()
        else:
            # Send a message to show that the purging is complete
            alert = await ctx.send(f"Purged {amount} message(s)!")
            
            # Delete the alert after 5 seconds
            await asyncio.sleep(5)
            await alert.delete()
    

load_dotenv()
bot.run(os.getenv("TOKEN"))