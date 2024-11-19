# How to Setup

## Table of Contents

1. [Python Installation :snake:](#python-installation-snake)
2. [Library Installation :memo:](#library-installation-memo)
3. [Running the Bot :robot:](#running-the-bot-robot)


### Python Installation :snake:

- This section of the setup tutorial shows you how to install the latest version of Python. **If you already have python installed there is no need to reinstall it and you may proceed to the next section.**

1. Press [this link](https://www.python.org/downloads/) to go to the python installation page and press the "Download Python" button.

2. After opening the installer, if the checkbox that says "Add python.exe to PATH" is unchecked, make sure to check it.
<img src="/setupimgs/python1.png">

3. Press the "Install Now" button to proceed with the installation.
<img src="/setupimgs/python2.png">

4. After the installation is complete, restart your computer.

### Library Installation :memo:

1. Open the folder that the bot's source code is inside and right click to open the context menu.

2. Click the "Open in Terminal" button to open a new terminal window.
<img src="/setupimgs/library1.png">

3. Once the terminal window opens, enter ``pip install -r requirements.txt`` into the terminal window as shown in the screenshot below.
<img src="/setupimgs/library2.png">

4. Wait for the libraries to install and proceed to the next section (you may leave the terminal window open as it will be used in the next section).


### Running the Bot :robot:

- Opening a terminal window. **Skip this if you already have a terminal window open.**

    1. Open the folder that the bot's source code is inside and right click to open     the context menu.

    2. Click the "Open in Terminal" button to open a new terminal window.
    <img src="/setupimgs/library1.png">


- Running the Bot
    1. Create a ``.env`` file in the bot's directory as shown below.
    
    <img src="/setupimgs/botstart1.png">

    2. Open the ``.env`` file in a text editor and type in ``TOKEN=`` followed by your bot's token. If you do not know how to find your bot's token, please follow [this](https://www.writebots.com/discord-bot-token/) guide.

    <img src="/setupimgs/botstart2.png">

    3. Finally, to start the bot, simply type ``python main.py`` into the terminal window as shown in the screenshot below.

    <img src="/setupimgs/botstart3.png">





🎉 Congratulations! 🎉 You have finished setting up your bot! If everything was done right you should now see your bot online in the server it's in, if you have a problem with the bot, please create an issue [here](https://github.com/JugieNoob/Simple-Discord-Mod-Bot/issues).



