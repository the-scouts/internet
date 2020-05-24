#
# Script
#
# Script requires an 'input.csv' file with postcodes (or searchable google maps parameters). Also requires
# an chromedriver.exe (source:https://chromedriver.chromium.org/downloads). The version of chromedriver.exe must match
# your locally installed version of Chrome.
#
# Requires the following python packages:
#   - selenium [verified works with v3.141.0]
#
# @TODO: Adapt script to work with other browsers depending on local device environment
# @TODO: Enhance script to take command line arguments for the name of the input file
from selenium import webdriver
import time
import csv

postcodes = []
with open("input.csv", "r", encoding="utf-8-sig") as f:
    reader = csv.reader(f, dialect='excel')
    for line in reader:
        postcodes.append(line[0])

driver = webdriver.Chrome()
coords = []
for postcode in postcodes:
    try:
        request_url = "https://www.google.com/maps/?q=" + postcode.replace(" ", "+")
        driver.get(request_url)
        url = driver.current_url
        while url == request_url:
            url = driver.current_url
            time.sleep(1)
        parts = url.split("!")
        longitude = parts[-1][2:]
        latitude = parts[-2][2:]
        coords.append([postcode, latitude, longitude])
    except:
        coords.append([postcode])

with open("output.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(coords)
