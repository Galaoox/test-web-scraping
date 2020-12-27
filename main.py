from bs4 import BeautifulSoup
import requests
import urllib.request
import os

link = input("IMDB Post link: ")
# Read html data
html = requests.get(link).text

# SOUP
soup = BeautifulSoup(html, 'html.parser')

title = soup.find("div", class_="title_wrapper").find("h1").text
title = title.strip()
# Rating example to search a property different to class in html
rating = soup.find('span', {"itemprop" : "ratingValue"}).text
summary: str = soup.find('div', class_="summary_text").text
summary = summary.strip()
posterLink = soup.find("div", class_="poster").find("img")["src"]

# Download poster
urllib.request.urlretrieve(posterLink, 'poster' +'.'+ posterLink.split(".")[-1])

print("title: ", title)
print("rating: ",rating)
print("summary: ",summary)


