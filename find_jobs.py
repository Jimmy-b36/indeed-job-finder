from indeed_web_scraper import main

#enter keywords here that you want to avoid in the job description
keywords = ['degree', 'bsc']
# search terms here
searchTerm = 'developer'
# location here
searchLocation = 'Vancouver, BC'

radius = ''
# exact = '0
# 5km = '5'
# 10km = '10'
# 15km = '15'
# default is 25km
# 50km = '50'
# 100km = '100'
remote = ''
# remote = 'attr(DSQF7)' 
# temporarily remote = 'attr(VAMUB)'
age = '' 
# last 24 hr = '1'
# last 3 days = '3'
# last 7 days = '7'
# last 14 days = '14'
language = ''
# javascript = 'attr(JB2WC)'
# python = 'attr(X62BT)'
# java 'attr(EVPJU)'
# React 'attr(84K74)'
# There are more but you'll have to find them manually on indeed.ca in the url just look for attr(XXXXX) where XXXXX is the language you want



main(keywords, searchTerm, searchLocation, remote, age, language, radius)