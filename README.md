# **Simple Moderation Bot** 🤖

## Table of Contents 📝
- [What is this ❓](#what-is-this-question)
- [Dependencies 📃](#dependencies-page_with_curl)
- [How to Setup ℹ️](#how-to-setup-information_source)
- [Commands ⌨️](#commands-keyboard)

##  What is this :question:

This is a simple Discord Bot that gives you access to basic moderation commands. I made this project to learn more about discord bots and the discord.py library. I decided to make it open source to show what I was able to learn and to allow other people to iterate on it if they wish to do so.

If you encounter any problems with the bot please make an issue [here](https://github.com/JugieNoob/Simple-Discord-Mod-Bot/issues) and i will try my best to solve them.

## Dependencies :page_with_curl:
- [discord.py](https://discordpy.readthedocs.io/en/stable/)
- [dotenv](https://pypi.org/project/python-dotenv/)
- [asyncio](https://pypi.org/project/asyncio)

❗To install the dependencies type ``pip install -r requirements.txt`` into a terminal window. ❗

## How to Setup :information_source:

Please click [here](https://github.com/JugieNoob/Simple-Discord-Mod-Bot/blob/main/Setup.md) to learn how to setup and start the bot.


## Commands :keyboard:

Command|Description|Required Permissions
-|-|-
.help | Shows all the bot's commands. | None
.info | Displays information about the bot. | None
.serverinfo| Displays some information about the current server like the creation date and member count. | None
.ban | Allows users with sufficient permissions to ban other users. | Ban Members
.kick | Allows users with sufficient permissions to kick other users. | Kick Members
.mute | Gives a muted role to the selected user and doesn't allow them to talk in text channels (Requires setup). | Moderate Members
.unmute | Removes the muted role from the selected user. | Moderate Members
.purge | Removes the inputted amount of messages in the current channel. | Manage Messages
