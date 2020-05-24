# internet

This repository contains useful scripts to support the wider suite of repositories.

## script

This script enables the finding of latitude and longitude coordinates from google searches. Place the google searches in a column in an 'input.csv' file, and the 'output.csv' file will contain the latitude and longitude coordinates.

This works by using selenium (and currently google chrome) to perform the search query and then extracting the relavent part of the resulting URL. It requires a version of ChromeDriver which matches the currently locally installed version of Google Chrome to be in the PATH when run (e.g. in the folder where the script is run).
