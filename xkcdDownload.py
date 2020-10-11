#! python3

import requests, os, bs4
from requests.exceptions import InvalidURL

os.chdir(filepath/xkcd) # filepath is a place holder for your own filepath
url = 'https://xkcd.com/'
comicNmbr = '2364' # This is the most recent comic that I started with
while not url.endswith('#'):
    res = requests.get(url)
    res.raise_for_status()
    if res.status_code == 200:
        soup = bs4.BeautifulSoup(res.text, "html.parser")
    else:
        print('Invalid Status Code')
        raise UnboundLocalError
    comicElem = soup.select('#comic img')
    if comicElem != []:
        try:
            print('Downloading page %s ...' % url)
            for div in soup.find_all('div', id='comic'):
                anchors = div.find_all('img')
                if anchors:
                    comic = anchors[0]['src']                    
                    comicFile = open(os.path.join('xkcd', (comicNmbr + ' ' + os.path.basename(comic))), 'wb')
                    comicUrl = ('https:' + comic)
                    res = requests.get(comicUrl)
                    print('Downloading image %s ...' % comicUrl)
                    for chunk in res.iter_content(100000):
                        comicFile.write(chunk)
                    comicFile.close()
        except InvalidURL:
            print('SKIPPED Invalid URL %s' % url)
    else:
        print('SKIPPED page %s' % url)
    prevLink = soup.select('a[rel="prev"]')[0]
    comicNmbr = prevLink.get('href').replace('/', '')
    url = 'https://xkcd.com' + prevLink.get('href')
