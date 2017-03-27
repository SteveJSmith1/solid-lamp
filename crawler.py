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



def getRandomURL(bsobj):
    
    link_list = bsobj.select('a')
    if len(link_list) == 0:
        print("No URLs found")
        return None
    else:
        import random
        choice = random.randint(0, len(link_list) - 1)
        url = link_list[choice].get('href')
        
    return url
  

def getRandomWikiURL(url):
    bsobj = soupify(url)
    new_url = getRandomURL(bsobj)
    while new_url.startswith('/wiki') is not True:
        new_url = getRandomURL(bsobj)
    
    checks = [':', '#', '?']
    
    while any(char in new_url for char in checks):
        
        new_url = getRandomWikiURL(new_url)
        
    return 'https://en.wikipedia.org' + new_url
    

  


def wikipediaWalk(url, walk_length):
    import time
    walk_urls = []
    walk_urls.append(url)
    
    for i in range(walk_length):
        try:
            print(url)
            url = getRandomWikiURL(url)
            if url is not None:
                if url in walk_urls:
                    url = getRandomWikiURL(walk_urls[-1])
                else:
                    walk_urls.append(url)
                    time.sleep(1)
            else:
                url = getRandomWikiURL(walk_urls[-1])
        except:
            continue
    return walk_urls



"""
Fetch the first link from each wiki page
"""
url = 'https://en.wikipedia.org/wiki/Sheep'
walk_length = 10

urls = wikipediaWalk(url, walk_length)



   
