# Simple Moderation Bot 🤖

## Table of Contents
- [What is this?](#what-is-this)
- [Dependencies](#dependencies)
- [How to Setup](#how-to-setup)
- [Commands](#commands)

###  What is this?

This is a simple Discord Bot that gives you access to basic moderation commands. I made this project to learn more about discord bots and the discord.py library. I decided to make it open source to show what I was able to learn and to allow other people to iterate on it if they wish to do so.

### Dependencies 
- [discord.py](https://discordpy.readthedocs.io/en/stable/)
- [dotenv](https://pypi.org/project/python-dotenv/)
- [asyncio](https://pypi.org/project/asyncio)

### How to Setup

Please click here to learn how to setup and start the bot.


### Commands

Command|Description
-|-
.serverinfo| Displays some information about the current server like the creation date and member count.
.ban | Allows users with sufficient permissions to ban other users.
.kick | Allows users with sufficient permissions to kick other users.
.mute | Gives a muted role to the selected user and doesn't allow them to talk in text channels (Requires setup).
.unmute | Removes the muted role from the selected user.
.purge | Removes the inputted amount of messages in the current channel.
