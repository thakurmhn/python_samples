#!/usr/bin/env python3.5

# Usage: OWM_API_KEY=dc49c8e46ebdf447ce1c4938ae7daf40 python3.5 weather_api.py 412101

# Script call open weather map api to get weather report for given

# dc49c8e46ebdf447ce1c4938ae7daf40


# request module doc : http://docs.python-requests.org/en/master/

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

url = "http://api.openweathermap.org/data/2.5/weather?zip={0},{1}&appid={2}".format(args.zip, args.country, owm_api_key)

res = requests.get(url)

if res.status_code != 200:  #  status_code is method usied in Request module
    print("Error : problem connectin openweathermap", res.status_code)
    sys.exist(1)

print(res.json())
