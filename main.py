import logging
import time

import psutil
from homeassistant_api import Client

# URL to the API of your HASS
URL = "http://homeassistant.local/api"

# Long lived access tocken which you can get in your user account in HASS
TOKEN = ""

# Name of your smart socket in HASS
SWITCH_NAME = "switch.128524_relay"

# Lower and upper limit which should trigger the socket
THRESH_LOW = 7
THRESH_HIGH = 97

logging.basicConfig(format="%(asctime)s %(levelname)-8s %(message)s", level=logging.INFO, datefmt="%Y-%m-%d %H:%M:%S")


def switch_on(client):
    switch = client.get_domain("switch")
    switch.turn_on(entity_id=SWITCH_NAME)


def switch_off(client):
    switch = client.get_domain("switch")
    switch.turn_off(entity_id=SWITCH_NAME)


client = Client(URL, TOKEN)
switch_off(client)
logging.info("Let's go!")

while True:
    battery = psutil.sensors_battery()
    percent = int(battery.percent)

    if percent <= THRESH_LOW:
        logging.info("Starting to charge")
        switch_on(client)
    elif percent >= THRESH_HIGH:
        logging.info("Stopping charging")
        switch_off(client)

    time.sleep(60)
