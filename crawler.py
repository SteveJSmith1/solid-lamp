#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 13:02:42 2017

@author: steve

Note to me:
    Use:
        from soupify import soupify
    should be used to create BeautifulSoup object
    and to save link, title and time visited in
    the csv.
"""

from soupify import soupify



def randomURL(bsobj):
    import random
    link_list = bsobj.select('p a')
    if len(link_list) == 0:
        print("No URLs found")
        return None
    else:
        choice = random.randint(0, len(link_list) - 1)
        url = link_list[choice].get('href')
        return url
    

def randomWiki(url):
    
    bsobj = soupify(url)

    new_url = randomURL(bsobj)
    if new_url.startswith('/wiki'):

        return 'https://en.wikipedia.org' + new_url
    else:
        return randomWiki(url)




def wikipediaWalk(url, walk_length):
    import time
    walk_urls = []
    for i in range(walk_length):
        try:
            print(url)
            url = randomWiki(url)
            if url is not None:
                walk_urls.append(url)
                time.sleep(1)
            else:
                url = randomWiki(walk_urls[-1])
        except:
            continue
    return walk_urls

url = 'https://en.wikipedia.org/wiki/Turnip'
walk_length = 20

wikipediaWalk(url, walk_length)

   
