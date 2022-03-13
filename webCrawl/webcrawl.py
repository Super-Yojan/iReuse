# This script is used to crawl a site, and store some information including the meta title, meta description, canonical, no of internal links and no of external links
# This script is used to crawl a site, and store some information including the meta title, meta description, canonical, no of internal links and no of external links
import sqlite3
import re
from traceback import print_tb
import requests
import random
from bs4 import BeautifulSoup
import time

start = time.time()

# for rotating through user agents
user_agent_list = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
]

# connect to database
db = sqlite3.connect('site_crawl.db')
cursor = db.cursor()


# get the URL to crawl
url = "https://bestlifeonline.com/easy-diy-home-projects/"
# work: https://diyjoy.com/easy-diy-projects/


db_name = "indexes"

# Create database
cursor.execute("CREATE TABLE IF NOT EXISTS " + db_name +
               " (UID INTEGER PRIMARY KEY AUTOINCREMENT,URL varchar(255),Description varchar(255),Item varchar(225), Time TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
all_urls = []
all_urls.append(url)


def extract_links(soup):
    """"Extract links and link counts from page"""
    links_dirty = soup.find_all('a')
    for link in links_dirty:
        if str(link.get('href')).startswith(url) == True and link.get('href') not in all_urls:
            if '.jpg' in link.get('href') or '.png' in link.get('href') or '#' in link.get('href'):
                continue
            else:
                all_urls.append(link.get('href'))

    return (len(links_dirty))


def insert_data(extracted_data):
    """Insert the crawled data into the database"""
    #print(title,"\n", description,"\n", contents,"\n",no_of_links,"\n", deduped_links)
    print(extracted_data)
    for data in extracted_data:
        url = str(extracted_data[data][0])
        desc = str(extracted_data[data][1] if len(
            extracted_data[data]) > 1 else '')
        item = data
        cursor.execute("INSERT INTO " + db_name +
                       " (URL, Description,Item) VALUES(?,?,?)", (url, desc, item))
        db.commit()


def scraper(url):
    keywords = ""
    keywords = ["recycle", "Recycle", "RECYCLE", "DIY", "diy",
                "reuse", "Reuse", "REUSE", "re-use", "Re-use", "RE-USE", "build", "Build", "make", "Make", "create", "Create", "construct", "Construct", "Create", "create", "Establish", "establish", "Assemble", "assemble", "produce", "Produce", "develop", "Develop", ]
    resp = requests.get(url).content
    soup = BeautifulSoup(resp, 'html.parser')
    temp = soup.find_all("p")
    commonObjects = {'clamp', 'shampoo', 'glow', 'dresses', 'balloon', 'buckle', 'stick', 'teddies', 'pot', 'fork', 'street', 'flag', 'liner', 'video', 'tooth', 'soda', 'sketch', 'magnet', 'band', 'milk', 'seat', 'white', 'helmet', 'puddle', 'mp3', 'beef', 'vase', 'lip', 'fake', 'shovel', 'remote', 'pencil', 'peanuts', 'picture', 'doll', 'cat', 'sponge', 'tote', 'drive', 'pants', 'packing', 'apple', 'hanger', 'bookmark', 'file', 'speakers', 'eraser', 'television', 'checkbook', 'phone', 'playing', 'clothes', 'pillow', 'chair', 'blouse', 'credit', 'clock', 'air', 'watch', 'clay', 'cinder', 'cork', 'press', 'bowl', 'flowers', 'containers', 'container', 'toe', 'drawer', 'coasters', 'blanket', 'spoon', 'CD', 'screw', 'house', 'plastic', 'truck', 'newspaper', 'wrapper', 'sandal', 'needle', 'album', 'tray', 'shoe', 'clippers', 'sand', 'thermometer', 'nail', 'socks', 'wallet', 'plate', 'sun', 'rubber', 'window', 'block', 'charger', 'car', 'desk', 'cup', 'tie', 'freshener', 'basket', 'tape', 'slipper', 'brocolli', 'sauce', 'chain', 'door', 'cups', 'cell', 'key', 'pots', 'shirt', 'ice', 'greeting', 'food', 'computer', 'toilet', 'soap', 'games', 'shade', 'pen', 'lights', 'USB', 'tissue', 'ipod', 'packet', 'tv', 'warmers', 'rusty', 'lamp', 'table', 'soy', 'wagon', 'player', 'carrots', 'bow', 'note', 'sidewalk', 'model', 'towel', 'water', 'twezzers', 'piano', 'lace', 'scotch', 'thread', 'keys', 'bottle', 'tire', 'knife', 'monitor', 'chocolate', 'belt', 'stop', 'keyboard', 'grid', 'fridge', 'cans', 'shawl', 'box', 'perfume', 'bananas', 'spring', 'sofa', 'swing', 'rugs', 'zipper', 'toothbrush', 'money', 'boom', 'ring', 'leg', 'washing', 'book', 'candle', 'cap', 'bracelet', 'face', 'tomato', 'lotion', 'shoes', 'purse', 'button', 'eye', 'picks', 'twister', 'cube', 'brush', 'mop', 'sticky', 'rug', 'chapter',
                     'can', 'jewlery', 'envelope', 'machine', 'totes', 'gloss', 'hair', 'tablet', 'radio', 'wash', 'candy', 'deodorant', 'stockings', 'headphones', 'drill', 'duck', 'floor', 'furniture', 'jar', 'thermostat', 'bag', 'sign', 'conditioner', 'glass', 'couch', 'bed', 'pad', 'controller', 'canvas', 'sailboat', 'cookie', 'outlet', 'mouse', 'paint', 'sharpie', 'frame', 'toothpaste', 'photo', 'mirror', 'pool', 'camera', 'paper', 'bread', 'chalk', 'card', 'tree', 'glasses', 'jugs'}
    data1 = dict()
    # check if <p> is in website
    if temp != "":
        # <p> text in site
        for paragraph in temp:
            print(paragraph)
            # keywords like recycle, reuse, DIY
            for keyword in keywords:
                # checks to see if keyword is in paragraph
                if keyword in str(paragraph):
                    print("found keyword", keyword)
                    # gets common object from common objects set
                    for obj in commonObjects:
                        # checks to see if common object is in the paragraph
                        if obj in str(paragraph):
                            if obj not in data1.keys():
                                data1[obj] = [(url, paragraph.get_text())]
                            else:
                                temp = data1[obj]
                                temp.append((url, paragraph.get_text()))
                                data1[obj] = temp
    else:
        return False
    return data1


link_counter = 0
while link_counter < len(all_urls):
    try:
        print(str(link_counter) + " crawling: " + all_urls[link_counter])
        # Set the headers
        user_agent = random.choice(user_agent_list)
        headers = {'User-Agent': user_agent}
        r = requests.get(all_urls[link_counter], headers=headers)
        print(r.status_code)
        if r.status_code == 200:
            html = r.text
            soup = BeautifulSoup(html, "html.parser")
            no_of_links = extract_links(soup)
            wanted_data = scraper(all_urls[link_counter])
            print(no_of_links)
            insert_data(wanted_data)

        link_counter += 1

    except Exception as e:
        link_counter += 1
        print(str(e))


# for i in all_urls:
#     print(scraper(i))

cursor.close()
db.close()
end = time.time()
print(end - start)
