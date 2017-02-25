#!/usr/bin/env python3

from urllib.request import urlopen
from dateutil.parser import parse as dateParser
import subprocess
import time

def main():
    #Reading raw data from website
    url = "http://www.facet.unt.edu.ar/facetinforma/category/becas/"
    try:
        data = urlopen(url)
        text = data.read().decode('utf-8')
    except:
        return
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
        subprocess.call(['notify-send',"Facet Informa",title])
        f = open("last","w")
        f.write(text)
        f.close()

if __name__ == "__main__":
    while True:
        main()
        time.sleep(300)
