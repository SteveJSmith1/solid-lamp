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



def fetchURL(bsobj, fetch='random'):
    link_list = bsobj.select('p a')
    if len(link_list) == 0:
        print("No URLs found")
        return None
    else:
        if fetch == 'random':
            import random
            choice = random.randint(0, len(link_list) - 1)
            url = link_list[choice].get('href')
        else:
            url = link_list[fetch].get('href')
    return url
  

def getWikiLink(url, fetch='random'):
    
    bsobj = soupify(url)

    new_url = fetchURL(bsobj, fetch=fetch)
    if new_url.startswith('/wiki'):

        return 'https://en.wikipedia.org' + new_url
    else:
        return getWikiLink(url, fetch='random')

  


def wikipediaWalk(url, walk_length, fetch='random'):
    import time
    walk_urls = []
    for i in range(walk_length):
        try:
            print(url)
            url = getWikiLink(url, fetch=fetch)
            if url is not None:
                walk_urls.append(url)
                time.sleep(1)
            else:
                url = getWikiLink(walk_urls[-1], fetch=fetch)
        except:
            continue
    return walk_urls


def walkToPhilosophy(url):
    import time
    walk_urls = []
    walk_urls.append(url)
    while url.endswith('Philosphy') is not True:
        url = getWikiLink(url, fetch=0)
        walk_urls.append(url)
        print(url)
        time.sleep(1)
    
    return len(walk_urls)

"""
Fetch the first link from each wiki page
"""
url = 'https://en.wikipedia.org/wiki/Sheep'

walkToPhilosophy(url)

"""
Fetch the first link from each wiki page
"""
url = 'https://en.wikipedia.org/wiki/Sheep'
walk_length = 30

wikipediaWalk(url, walk_length, fetch=0)

"""
Fetch a random link from each wiki page
"""
url = 'https://en.wikipedia.org/wiki/Sheep'
walk_length = 10

wikipediaWalk(url, walk_length)
   
