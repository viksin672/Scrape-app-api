<h1>Scrape-app-api<h1>
<hr>
<p>Web scraping is a term used to describe the use of a program or algorithm to extract and process large amounts of data from the web. Whether you are a data scientist, engineer, or anybody who analyzes large amounts of datasets, the ability to scrape data from the web is a useful skill to have. Let's say you find data from the web, and there is no direct way to download it, web scraping using Python is a skill you can use to extract the data into a useful form that can be imported.</p>
<hr>
<h3>Web Scraping using Beautiful Soup</h3>
<ul>
  <li>import pandas as pd</li>
  <li>import numpy as np</li>
  <li>import matplotlib.pyplot as plt</li>
  <li>import seaborn as sns</li>
  <li>from urllib.request import urlopen</li>
  <li>from bs4 import BeautifulSoup</li>
  <li>url = "http://www.xyz.com"</li>
  <li>html = urlopen(url)</li>
  <li>soup = BeautifulSoup(html, 'lxml')</li>
  <li>type(soup)</li>
  <li>bs4.BeautifulSoup</li>
  
</ul>
<p>The soup object allows you to extract interesting information about the website you're scraping such as getting the title of the page as shown below.</p>
  <p># Get the title
title = soup.title
print(title)</p>
