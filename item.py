# Device Class
# Purpose: Define an IoT device (known as a WebThing) with the senses and actuations

### External Imports ###
import sys
import stripe
import json
import urllib.request
import requests
import threading
import websockets
import asyncio
import queue


class item:

    # Constructor
    def __init__(self, url, raw_json):

        self.title = "null"
        # ## Threading constructor
        # threading.Thread.__init__(self, target=self.__thread_runner)
        # self._stop_event = threading.Event()

        # ## Passed in Data
        self.url = url
        self.raw_json = raw_json
        self.state = "null"
        # self.security_key   = security_key

        # ## Important device meta data
        # self.was_parsed     = False         ## A boolean to indicate if we could properly parse the JSON or not

        # ## Device Information
        # self.title          = "null"        ## Title of the device found
        # self.context        = "null"        ## Base url of the device which can be further refined by the schemas objects
        # self.type           = []            ## @types which is a list of type's originated from the schema that this device has
        # self.description    = "null"        ## String decsribing the device (often empty)
        # self.href           = "null"        ## Link extension on top of the base where we can query the device
        # self.base           = "null"        ## Base URL used for hosting all things [https://____.io/things]
        # self.id             = "null"        ## Fully qualified URL for the device (combines the base url and the href)

        # ## Device Core Properties
        # self.senses         = []    ## These include ANY properties found
        # self.actuations     = []    ## These include ANY actions found
        # self.events         = []    ## These include ANY events found

        # ## Misc device information that is not that relevant to API side
        # self.floorplan              = [-1.0, -1.0]  ## X and Y floorplan position that describes where the thing is located on a potential floor plan
        # self.layout_index           = -1            ## An index into the types list to show which type should be used on the UI display
        # self.security_definitions   = None          ## This will hold the JSON for security defintions, currently I am not parsing or using
        # self.security               = "null"        ## The name of the security type being used by this thing
        # self.links                  = []            ## List of links correlating to this thing

        # ## Parse the JSON into the information required
        self.__parse_json()

        # ## Websocket/device monitoring related information
        # self.is_monitored       = False         ## A boolean value to indicate if we have a websocket open and are monitoring the device
        # self.refresh_rate       = 3             ## This is the rate at which we will be waiting for a receive packet from a device while monitoring
        # self.websocket_queue    = []            ## A list of strings that we receive from the websocket
        # self.__device_state     = None          ## A device state object to hold the current device state if we are in a websocket monitoring
        # self.past_device_states = []            ## A list of past device states for each time we re-initialize a monitoring

        # ## Device Status Information
        # self.connected          = False

        # Method to parse an individual things JSON into: [Meta-Data, senses, actuations and events]
    def __parse_json(self):

        # Get device information
        self.title = self.raw_json.get('name')
        self.href = self.raw_json.get('link')
        self.state = self.raw_json.get('state')
        self.was_parsed = True
        
    def SetSense(self, sense, value):
        self.state = value
        
