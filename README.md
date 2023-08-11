# battery-refresh

Use a smart socket to automatically refresh your laptop battery.


## Usecase
After a few years of home office, my laptop battery was pretty bad because my work laptop spend 24/7 in a docking
station. To get a bit of capacity back I thought about running a few charge/discharge cycles. This is a common feature
to refresh old batteries (mainly due to better battery circuit calibration) and can e.g. be done with the Thinkvantage
tools on Windows if you own a Thinkpad.

Because I have a Dell XPS, I needed a different approach. And because I have Home Assistant, my idea was to use a smart
socket and just turn it on/off based on the current battery charge level.


## Usage
Open the `main.py` and adapt the variables on top of the script to your setup. The code was created quite late in the
night, so it's not that beautiful, but it get's the job done :D

After that, just plug the charger in the smart socket, conenct your laptop to the charger and start the script. Then let
it run as long as you like.

Depending on the performance of your battery, you probably don't want to set the THRESH_LOW to low, so it won't turn off
before reaching it. Setting THRESH_HIGH to 100 is also not recommended because modern lithium batteries don't like to be
completly full or completly empty.

