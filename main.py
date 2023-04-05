import discord
import re
import requests
import os
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.all()
client = discord.Client(intents=intents)

# Information needed for wallabag API authentication
WALLABAG_CLIENT_ID = os.getenv('CLIENT_ID')
WALLABAG_CLIENT_SECRET = os.getenv('CLIENT_SECRET')
WALLABAG_USERNAME = os.getenv('USERNAME')
WALLABAG_PASSWORD = os.getenv('PASSWORD')
DISCORD_CHANNEL_IDS = list(map(int, os.getenv('DISCORD_CHANNEL_IDS').split(',')))
BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')

# Function to save link to wallabag and return the wallabag link
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

        # Check if link was successfully saved in wallabag
        if response.status_code != 200:
            raise Exception('Failed to save link to Wallabag')

        # Extract the wallabag link id from the API response
        wallabag_link_id = response.json()['id']
        patched_response = requests.patch('https://wallabag.nixnet.services/api/entries/{wallabag_link_id}.json'.format(wallabag_link_id=wallabag_link_id) , data={

            'public': True,
            'access_token': WALLABAG_ACCESS_TOKEN

        })
        return patched_response.json()['uid']
    except Exception as e:
        print('Error saving link to Wallabag:', e)
        return None

    # see = patched_response.json()
    # print(see)

# Function to get the title of the article
def get_article_title(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.find('meta', {'property': 'og:title'})['content']
    return title

def refresh_wallabag_access_token():
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

# Authenticate with Wallabag API to retrieve token
refresh_wallabag_access_token()

@client.event
async def on_message(message):
    # Check if message was sent by the bot itself or not in any of the specified channels
    if message.author.id == client.user.id or message.channel.id not in DISCORD_CHANNEL_IDS:
      return

    # Check if message contains a WSJ link
    regex = [r'\bhttps?:\/\/(?:www\.)?nytimes\.com\/[^\s]+\b', r'\bhttps?:\/\/(?:www\.)?wsj\.com\/[^\s]+\b', r'\bhttps?:\/\/(?:www\.)?economist\.com\/[^\s]+\b', r'\bhttps?:\/\/(?:www\.)?businessinsider\.com\/[^\s]+\b', r'\bhttps?:\/\/(?:www\.)?ft\.com\/[^\s]+\b']
    for pattern in regex:
      if re.search(pattern, message.content):
          link = re.findall(pattern, message.content)[0]

          # Save link to Wallabag and retrieve Wallabag link
          wallabag_public_url_end = save_link_to_wallabag(link)
  
          wallabag_link = f"https://wallabag.nixnet.services/share/{wallabag_public_url_end}"
  
          # Get the title of the article from the link
          title = get_article_title(wallabag_link)
  
          # Format and send the message
          formatted_message = f":newspaper:  |  **{title}**\n\n{wallabag_link}"
          await message.channel.send(formatted_message)

client.run(BOT_TOKEN)
