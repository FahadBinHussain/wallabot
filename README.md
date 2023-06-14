# Wallabot

This Python script is a Discord bot that extracts the title and saves a link to Wallabag from WSJ (Wall Street Journal) articles shared in a specified channel.

# Setup

## Critical prerequisites to install

* run ```pip3 install -r requirements.txt```

* **Rename the file `.env.dev` to `.env`**

## Step 1: Create a Discord bot

1. Go to https://discord.com/developers/applications create an application

[![image-17.png](https://i.postimg.cc/rp6J7h8D/image-17.png)](https://postimg.cc/QFb1TJKD)

2. Build a Discord bot under the application

[![image.png](https://i.postimg.cc/zv5J5JDz/image.png)](https://postimg.cc/TL78JvWF)

3. Click Reset Token and then copy the token

[![image.png](https://i.postimg.cc/sgBCkBPP/image.png)](https://postimg.cc/18Zd63j4)

4. Turn ALL INTENT `ON`

[![image.png](https://i.postimg.cc/RF48ZqtD/image.png)](https://postimg.cc/3yf9L8nX)

5. Invite your bot to your server via OAuth2 URL Generator

[![image.png](https://i.postimg.cc/yd3PBHQb/image.png)](https://postimg.cc/ZBZ3F1h8)

## Step 2: Create a wallabag account

1. Go to https://wallabag.nixnet.services/login and create account

[![image-28.png](https://i.postimg.cc/G90LR997/image-28.png)](https://postimg.cc/JHqVcrNZ)

2. Store the Username and Password to `.env` under the `USERNAME` and `PASSWORD`

[![image.png](https://i.postimg.cc/hGGfpzmT/image.png)](https://postimg.cc/PCBXqq25)

## Step 3: Official API authentication

### Generate Client ID and Client Secret

1. Go to https://wallabag.nixnet.services/developer

2. Click CREATE A NEW CLIENT

[![image.png](https://i.postimg.cc/Zn6RCrkt/image.png)](https://postimg.cc/q6M0F6Mj)

3. Fill the Name of the client, Click CREATE A NEW CLIENT again

[![image.png](https://i.postimg.cc/wjqvjy0Z/image.png)](https://postimg.cc/ppSx0TNJ)

4. Store the Client ID and Client Secret to `.env` under the `CLIENT_ID` and `CLIENT_SECRET`

[![image.png](https://i.postimg.cc/3NQr5dkL/image.png)](https://postimg.cc/349Q2rCp)

5. You're all set for [Step 3](#step-3-run-the-bot-on-the-desktop)

## Step 3: Run the bot on the desktop

1. Open a terminal or command prompt

2. Navigate to the directory where you cloned the wallabot

3. Run `python3 main.py` to start the bot

### Have a good chat!

## Optional: For a specific channel

1. Right-click the channel you want the bot to listen for messages, `Copy  ID`

[![image.png](https://i.postimg.cc/NGRf87nZ/image.png)](https://postimg.cc/c64S0Y0c)

2. paste it into `.env` under `DISCORD_CHANNEL_ID`

[![image.png](https://i.postimg.cc/3JB8VrYB/image.png)](https://postimg.cc/YhvBmH4G)
