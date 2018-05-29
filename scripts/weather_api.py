#!/usr/bin/env python3.5

import os
import requests
import sys

from argparse import ArgumentParser

parser = ArgumentParser(description='Get the current infromation of weather on your zip code')
parser.add_argument('zip', help='zip/postal code to get information for')
parser.add_argument('--country', default='in')

# Get arguments
args = parser.parse_args()

owm_api_key = os.getenv("OWM_API_KEY")
if not owm_api_key:
    print("Error: Please check OWM_API_KEY env is set properly")
    sys.exit(1)

url = "http://api.openweathermap.org/data/2.5/weather?{0},{1}&appid={2}".format(args.zip, args.country, owm_api_key)

res = requests.get(url)
print(res)
