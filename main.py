import discord
from discord.ext import commands
import asyncio
from dotenv import load_dotenv
import os
from datetime import datetime
import time

bot = commands.Bot(".", intents=discord.Intents.all(), help_command=None)
starttime = time.time()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    global botuser
    botuser = bot.user
# Bot sends a message if an error occurs
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command not found.")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have the required permissions to use this command.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Missing required argument.")
    else:
        await ctx.send("An error occurred: " + str(error))

# Help Menu
helpembed = discord.Embed(title="Help Menu ❓", description=f"Use {bot.command_prefix}help (command) to get information about a command.")
helpembed.add_field(name="help", value="Shows all bot commands (you're using it right now)")
helpembed.add_field(name="serverinfo", value="Displays basic information about the server")
helpembed.add_field(name="ban", value="Bans the pinged user.")
helpembed.add_field(name="kick", value="Kicks the pinged user.")
helpembed.add_field(name="mute", value="Mutes the pinged user.")
helpembed.add_field(name="unmute", value="Unmutes the pinged user.")
helpembed.add_field(name="purge", value="Purges the amount of messages entered.")
helpembed.add_field(name="info", value="Displays info about the bot.")


# Info Menu
infoembed = discord.Embed(title="Info Menu :information_source:")
infoembed.add_field(name="Bot Start Time", value=datetime.fromtimestamp(starttime))
infoembed.add_field(name="Bot Creator", value="[Jugie](https://github.com/JugieNoob)", inline=False)
infoembed.add_field(name="Bot Source Code", value="[Github](https://github.com/JugieNoob/Simple-Mod-Bot)", inline=False)


@bot.command("help")
async def self(ctx, arg:str = ""):
    if arg.lower() == "serverinfo":
        await ctx.send("```Displays basic information about the server such as the server creation date and the current member count.```")
    elif arg.lower() == "ban":
        await ctx.send(f"```Bans the pinged user from the server.\n{bot.command_prefix}ban (user)\nRequired Permissions: Ban Members```")
    elif arg.lower() == "kick":
        await ctx.send(f"```Kicks the pinged user from the server.\n{bot.command_prefix}kick (user)\nRequired Permissions: Kick Members```")
    elif arg.lower() == "mute":
        await ctx.send(f"```Gives the pinged user the muted role.\n{bot.command_prefix}mute (user)\nRequired Permissions: Moderate Members```")
    elif arg.lower() == "unmute":
        await ctx.send(f"```Removes the muted role from the pinged user.\n{bot.command_prefix}unmute (user)\nRequired Permissions: Moderate Members```")
    elif arg.lower() == "purge":
        await ctx.send(f"```Removes the amount of messages entered in the current channel.\n{bot.command_prefix}purge (amount)\nRequired Permissions: Manage Messages```")
    elif arg.lower() == "info":
        await ctx.send(f"```Displays some information about the bot.```")
    elif arg.lower() == "help":
        await ctx.send(f"```Shows all the available commands.```")
    else:
        helpembed.set_thumbnail(url=botuser.avatar)
        helpembed.set_footer(text=f"{botuser}: Help")
        await ctx.send(embed=helpembed)
    

@bot.command("info")
async def self(ctx):
    infoembed.set_thumbnail(url=botuser.avatar)
    helpembed.set_footer(text=f"{botuser}: Info")
    await ctx.send(embed=infoembed)


@bot.command("serverinfo")
async def self(ctx):
    # Creates an embed with server information
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
        # Bans the pinged user
        await user.ban(reason)
        await ctx.send(f"Banned {user} for: {reason}")
    else:
        await ctx.send("Please ping the user you are trying to ban")
        
@bot.command("kick")
@commands.has_permissions(kick_members=True)
async def self(ctx, user:discord.Member = None, reason = "No Reason Given"):
    if (user != None):
        # Kicks the pinged user
        await user.kick(reason)
        await ctx.send(f"Kicked {user} for: {reason}")
    else:
        await ctx.send("Please ping the user you are trying to kick")

@bot.command("mute")
@commands.has_permissions(moderate_members = True) #Timeout permission
async def self(ctx, user:discord.Member = None, reason = "No Reason Given", time:float = 1):
    if (user != None):
        # Gives the muted role to the pinged user
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