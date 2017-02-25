#!/usr/bin/env python3

from urllib.request import urlopen
from dateutil.parser import parse as dateParser

def main():
    #Reading raw data from website
    url = "http://www.facet.unt.edu.ar/facetinforma/category/becas/"
    data = urlopen(url)
    text = data.read().decode('utf-8')

    title = text[text.find("entry-title")+13:]
    title = title[title.find(">")+1:title.find("</a>")]
    

    #Getting ISO 8601 format date
    text = text[text.find("datetime"):text.find("</time")]
    text = text[text.find("\"")+1:text.find("\">")]

    #Datetime object
    date = dateParser(text)

    #Checks last date. If it's the first time sets the last date
    try:
        f = open("last","r")
    except FileNotFoundError:
        f = open("last","w")
        f.write(text)
        f.close()
        f = open("last","r")

    lastdate = dateParser(f.read())

    if date > lastdate:
        print(title)
        f = open("last","w")
        f.write(text)
        f.close()

if __name__ == "__main__":
    main()
