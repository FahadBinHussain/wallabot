# Wallabot

This Python script is a Discord bot that extracts the title and saves a link to Wallabag from WSJ (Wall Street Journal) articles shared in a specified channel.

# Setup

## Critical prerequisites to install

* run ```pip3 install -r requirements.txt```

* **Rename the file `.env.dev` to `.env`**

## Step 1: Create a Discord bot

1. Go to https://discord.com/developers/applications create an application

![image](https://user-images.githubusercontent.com/75292632/229356888-1afd8d63-ad2f-43f1-9969-100735f2b0f8.png)

2. Build a Discord bot under the application

![image](https://user-images.githubusercontent.com/75292632/229356928-fa826d85-e135-4bbe-8899-9d1d6e6680d4.png)

3. Get the token from bot setting

![image](https://user-images.githubusercontent.com/75292632/229357004-01ec6385-9b9d-45c3-a3ea-a6aba14754d4.png)

4. Store the token to `.env` under the `DISCORD_BOT_TOKEN`

![image](https://user-images.githubusercontent.com/75292632/229357198-27fd0fe6-e5ed-4c48-8d64-31577114bc03.png)

5. Turn ALL INTENT `ON`

![image](https://user-images.githubusercontent.com/75292632/229357231-c31d4b8f-f31a-4959-a615-862e8e6b720f.png)

6. Invite your bot to your server via OAuth2 URL Generator

![image](https://user-images.githubusercontent.com/75292632/229357269-09463d81-d109-49a8-b569-fdf2a2316b4c.png)

## Step 2: Create a wallabag account

1. Go to https://wallabag.nixnet.services/login and create account

![image](https://user-images.githubusercontent.com/75292632/229357604-b05c5a99-75d3-409a-bd0f-d5d60d757740.png)

2. Store the Username and Password to `.env` under the `USERNAME` and `PASSWORD`

![image](https://user-images.githubusercontent.com/75292632/229357690-146a9e02-6fdc-468a-8a19-188040d6ec8c.png)

## Step 3: Official API authentication

### Generate Client ID and Client Secret

1. Go to https://wallabag.nixnet.services/developer

2. Click CREATE A NEW CLIENT

![image](https://user-images.githubusercontent.com/75292632/229357730-a5825ce8-9104-4b36-8c1c-95f053c8f7d1.png)

3. Fill the Name of the client, Click CREATE A NEW CLIENT again

![image](https://user-images.githubusercontent.com/75292632/229357758-f527df0b-2f30-4a8f-bf5c-8e7829c44097.png)

4. Store the Client ID and Client Secret to `.env` under the `CLIENT_ID` and `CLIENT_SECRET`

![image](https://user-images.githubusercontent.com/75292632/229357831-df773463-978a-4332-858c-6e33d5a949cb.png)

5. You're all set for [Step 3](#step-3-run-the-bot-on-the-desktop)

## Step 3: Run the bot on the desktop

1. Open a terminal or command prompt

2. Navigate to the directory where you cloned the wallabot

3. Run `python3 main.py` to start the bot

### Have a good chat!

## Optional: For a specific channel

1. Right-click the channel you want the bot to listen for messages, `Copy  ID`

2. paste it into `.env` under `DISCORD_CHANNEL_ID`
