# Python job finder for Indeed

## Overview

I made this script for personal use to find jobs that match my skills.

This python script will launch indeed on a browser using selenium and search for jobs based on the parameters you provide.
the main function running script in find_jobs.py will create a csv list of jobs that match the parameters you provide. I have added some of the main parameters that I use to search for jobs. You can add more parameters to the search by adding them the methods get_url & main in indeed_web_scraper.py

## Directions for use

- The script will not work if you do not have the correct version of chromedriver installed. You can download the correct version of chromedriver from https://chromedriver.chromium.org/downloads
- You can use other browsers but will have to edit indeed_web_scraper.py to use the correct driver.
- The script will not work if you do not have the correct version of selenium installed. You can download the correct version of selenium from https://pypi.org/project/selenium/

## Known issues

- Prone to timeouts if there are too many jobs as the script is having to click on each one to read the description. I have added an exception to timeouts to try and avoid this but it is not perfect.
- If the script does not work right away try closing the window and running it again. It may be that the page has not loaded yet. This one could happen several times before it works.

### Credit to this repo for the base code:

- https://github.com/israel-dryer/Indeed-Job-Scraper/blob/master/indeed-job-scraper-selenium.ipynb
