# Wallabot

This Python script is a Discord bot that extracts the title and saves a link to Wallabag from WSJ (Wall Street Journal) articles shared in a specified channel.

# Setup

## Critical prerequisites to install

* run ```pip3 install -r requirements.txt```

* **Rename the file `.env.dev` to `.env`**

## Step 1: Create a Discord bot

1. Go to https://discord.com/developers/applications create an application

2. Build a Discord bot under the application

3. Get the token from bot setting

4. Store the token to `.env` under the `DISCORD_BOT_TOKEN`

5. Turn ALL INTENT `ON`

6. Invite your bot to your server via OAuth2 URL Generator

## Step 2: Create a wallabag account

1. Go to https://wallabag.nixnet.services/login and create account

2. Store the Username and Password to `.env` under the `USERNAME` and `PASSWORD`

## Step 3: Official API authentication

### Generate Client ID and Client Secret

1. Go to https://wallabag.nixnet.services/developer

2. Click CREATE A NEW CLIENT

3. Fill the Name of the client, Click CREATE A NEW CLIENT again

4. Store the Client ID and Client Secret to `.env` under the `CLIENT_ID` and `CLIENT_SECRET`

5. You're all set for [Step 3](#step-3-run-the-bot-on-the-desktop)

## Step 3: Run the bot on the desktop

1. Open a terminal or command prompt

2. Navigate to the directory where you cloned the wallabot

3. Run `python3 main.py` to start the bot

### Have a good chat!

## Optional: For a specific channel

1. Right-click the channel you want the bot to listen for messages, `Copy  ID`

2. paste it into `.env` under `DISCORD_CHANNEL_ID`