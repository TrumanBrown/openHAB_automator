import json
import logging
import pathlib
import time
import typing
import warnings

import requests
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth2Session
import item

# username linctru@gmail.com
# password TrumanBrown
username = "linctru@gmail.com"
pwd = "TrumanBrown"


class openHAB_node:
    # Constructor
    def __init__(self, url):

        # Passed in data
        self.url = url
        # TODO => There needs to be some verification/sign in

        # A Boolean that will indicate whether or not we have (or are maintaining) a healthy connection
        self.connection_initialized = False
        self.items_parsed = False

        self.__items = {}  # Dict of all devices connected to the gateway

        self.__monitored = []  # List of the names of all devices that are being monitored

    # Method to check for an initial connection to the gateway
    def connect(self, username, pwd):
        try:
            self.session = requests.Session()
            self.session.auth = HTTPBasicAuth(username, pwd)
            self.session.headers['accept'] = 'application/json'
            self.connection_initialized = True
            print("Connection initialized")
            self.__fetch_items()

        except Exception as e:
            self.connection_initialized = False
            print(e)

    # def get_items(self):
    #     item_manifest = self.session.get(self.url + 'items')
    #     for item in item_manifest.json():
    #         print(item)
    #     return item_manifest.json()

    def __fetch_items(self):
        try:
            # This will return a list Json objects for each thing that was found
            item_manifest = self.session.get(self.url + 'items')
            # For each json object in the device_manifest received
            for itemJSON in item_manifest.json():

                # Create a new device which will parse the JSON into a device
                new_item = item.item(self.url, itemJSON)
                self.__items[new_item.title] = new_item
                # print(f"Title: {new_item.title}, state: {new_item.state}, href: {new_item.href}")
                # print(itemJSON)

            self.items_parsed = True

        except Exception as e:
            print(e)
    def getItems(self):
        to_ret=None
        if(self.items_parsed):
            to_ret=self.__items
        return to_ret
    
    
# main method
if __name__ == "__main__":
    
    demoRoom = openHAB_node("https://home.myopenhab.org/rest/")
    demoRoom.connect(username, pwd)
    # print(demoRoom.getItems())
    Spotify_Volume = demoRoom.getItems()['SpotifyPlayerBridge_Volume']
    print(Spotify_Volume.state)
    Spotify_Volume.SetSense("volume", 100)
    print(Spotify_Volume.state)
    
    

def connectTest(url):
    # Initialize a connection w/ a timeout of 1 second

    session = requests.Session()
    session.auth = HTTPBasicAuth(username, pwd)
    session.headers['accept'] = 'application/json'
    r = session.get(url)
    print(r.json())
    return r.json()


def postTest(url, value):
    # Initialize a connection w/ a timeout of 1 second

    session = requests.Session()
    session.auth = HTTPBasicAuth(username, pwd)
    session.headers['accept'] = 'application/json'
    value = value.encode('ascii')
    session.post(url, data=value,headers={'Content-Type': 'text/plain'})



    
    
    
    # print("1. Get Song Name --------------------------------------------------")
    # spotifySong = connectTest('https://home.myopenhab.org/rest/items/SpotifyPlayerBridge_MediaTitle')
    
    # print("2. Get Volume --------------------------------------------------")
    # spotifyVolume = connectTest('https://home.myopenhab.org/rest/items/SpotifyPlayerBridge_Volume')
    
    # print("3. Skip Song --------------------------------------------------")
    # spotifyPlayer = postTest('https://home.myopenhab.org/rest/items/SpotifyPlayerBridge_MediaControl', 'NEXT')
    
    # print("4. Turn volume Up --------------------------------------------------")
    # spotifyPlayer = postTest('https://home.myopenhab.org/rest/items/SpotifyPlayerBridge_Volume', '100')
    
    # print("5. Get Song Name --------------------------------------------------")
    # spotifySong = connectTest('https://home.myopenhab.org/rest/items/SpotifyPlayerBridge_MediaTitle')
    
    # print("6. Get Volume --------------------------------------------------")
    # spotifyVolume = connectTest('https://home.myopenhab.org/rest/items/SpotifyPlayerBridge_Volume')
    
    
