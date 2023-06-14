import discord
import re
import requests
import os
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from dotenv import load_dotenv
from keep_alive import keep_alive

load_dotenv()

intents = discord.Intents.all()
client = discord.Client(intents=intents)

# Information needed for Wallabag API authentication
WALLABAG_CLIENT_ID = os.getenv('CLIENT_ID')
WALLABAG_CLIENT_SECRET = os.getenv('CLIENT_SECRET')
WALLABAG_USERNAME = os.getenv('USERNAME')
WALLABAG_PASSWORD = os.getenv('PASSWORD')
DISCORD_CHANNEL_IDS = list(map(int, os.getenv('DISCORD_CHANNEL_IDS').split(',')))
BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')

# Function to save link to Wallabag and return the Wallabag link
def save_link_to_wallabag(link):
    # Refresh the Wallabag access token if it's close to expiring
    if WALLABAG_ACCESS_TOKEN_EXPIRATION - datetime.now() < timedelta(minutes=5):
        refresh_wallabag_access_token()

    try:
        # Use Wallabag API to save the link
        response = requests.post('https://wallabag.nixnet.services/api/entries.json', data={
            'url': link,
            'access_token': WALLABAG_ACCESS_TOKEN
        })

        # Check if the link was successfully saved in Wallabag
        if response.status_code != 200:
            raise Exception('Failed to save link to Wallabag')

        # Extract the Wallabag link id from the API response
        wallabag_link_id = response.json()['id']
        patched_response = requests.patch(f'https://wallabag.nixnet.services/api/entries/{wallabag_link_id}.json', data={
            'public': True,
            'access_token': WALLABAG_ACCESS_TOKEN
        })
        return patched_response.json()['uid']
    except Exception as e:
        print('Error saving link to Wallabag:', e)
        return None

# Function to get the title of the article
def get_article_title(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('meta', {'property': 'og:title'})['content']
        return title
    except Exception as e:
        print('Error retrieving article title:', e)
        return None

def refresh_wallabag_access_token():
    try:
        # Authenticate with Wallabag API to retrieve a new access token
        response = requests.post('https://wallabag.nixnet.services/oauth/v2/token', data={
            'grant_type': 'password',
            'client_id': WALLABAG_CLIENT_ID,
            'client_secret': WALLABAG_CLIENT_SECRET,
            'username': WALLABAG_USERNAME,
            'password': WALLABAG_PASSWORD
        })

        # Check if Wallabag API authentication was successful
        if response.status_code != 200:
            print('Failed to authenticate with Wallabag API')
            exit()

        # Extract the access token from the Wallabag API response
        global WALLABAG_ACCESS_TOKEN
        WALLABAG_ACCESS_TOKEN = response.json()['access_token']
        global WALLABAG_ACCESS_TOKEN_EXPIRATION
        WALLABAG_ACCESS_TOKEN_EXPIRATION = datetime.now() + timedelta(seconds=response.json()['expires_in'])
    except Exception as e:
        print('Error refreshing Wallabag access token:', e)

# Authenticate with Wallabag API to retrieve token
refresh_wallabag_access_token()

@client.event
async def on_message(message):
    # Check if message was sent by the bot itself or not in any of the specified channels
    if message.author.id == client.user.id or message.channel.id not in DISCORD_CHANNEL_IDS:
        return

    # Check if message contains a link from supported websites
    supported_websites = [
        {
            'pattern': r'\bhttps?:\/\/(?:www\.)?nytimes\.com\/[^\s]+\b',
            'name': 'New York Times'
        },
        {
            'pattern': r'\bhttps?:\/\/(?:www\.)?wsj\.com\/[^\s]+\b',
            'name': 'Wall Street Journal'
        },
        {
            'pattern': r'\bhttps?:\/\/(?:www\.)?economist\.com\/[^\s]+\b',
            'name': 'The Economist'
        },
        {
            'pattern': r'\bhttps?:\/\/(?:www\.)?businessinsider\.com\/[^\s]+\b',
            'name': 'Business Insider'
        },
        {
            'pattern': r'\bhttps?:\/\/(?:www\.)?ft\.com\/[^\s]+\b',
            'name': 'Financial Times'
        }
    ]

    for website in supported_websites:
        pattern = website['pattern']
        if re.search(pattern, message.content):
            link = re.findall(pattern, message.content)[0]

            # Save the link to Wallabag and retrieve the Wallabag link
            wallabag_public_url_end = save_link_to_wallabag(link)

            if wallabag_public_url_end is None:
                return

            wallabag_link = f"https://wallabag.nixnet.services/share/{wallabag_public_url_end}"

            # Get the title of the article from the link
            title = get_article_title(wallabag_link)

            if title is None:
                return

            # Format and send the message
            formatted_message = f":newspaper:  |  **{title}**\n\n{wallabag_link}"
            await message.channel.send(formatted_message)

            # Return after processing the first link to avoid sending duplicates
            return

    # If no supported link is found, continue processing other messages
    await client.process_commands(message)

keep_alive()  # Starts a web server to keep the bot online.
client.run(BOT_TOKEN)
