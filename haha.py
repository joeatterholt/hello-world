import webbrowser
import time
import random

while True:
    sites = random.choice(['google.com','mastercode.online','youtube.com','weather.com'])
    visit = "http://{}".format(sites)
    webbrowser.open(visit)
    seconds = random.randrange(5, 100)
    time.sleep(seconds)
