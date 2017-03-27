#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 12:14:23 2017

@author: SteveJSmith1

Creates a BeautifulSoup object from a URL
Saves, url, title (if any) and date visited to a csv
to keep a history of sites crawled.
"""

import requests
import csv
import datetime
import bs4




def soupify(url):
    res = requests.get(url)
    visited_on = str(datetime.datetime.now())
    
    try:
        res.raise_for_status()
    except Exception as exc:
        print('There was a problem: %s' % (exc))
        
    data = res.text
    bsobj = bs4.BeautifulSoup(data, "lxml")
    titleobjs = bsobj.select('title')
    if len(titleobjs) == 0:
        title = ' '
    else:
        title = titleobjs[0].getText()
    
    historySave(url, title, visited_on)
    return bsobj



def historySave(url, title, visited_on):
    fields = [url, title, visited_on]
    with open(r'PythonGeneratedHistory.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
    
