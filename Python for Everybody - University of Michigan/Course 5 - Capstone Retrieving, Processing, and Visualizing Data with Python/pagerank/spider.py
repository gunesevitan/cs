import sqlite3
import ssl
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from urllib.parse import urlparse
from urllib.request import urlopen


# Ignoring SSL Certificate errors
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE


connection = sqlite3.connect('spider.sqlite')
cursor = connection.cursor()

# Creating tables for the crawling process

# Table for holding:
# Page's URL, Page's HTML Code, Error if the page could not be retrieved, Page's Old Rank, Page's New Rank
cursor.execute('''CREATE TABLE IF NOT EXISTS Pages
    (id INTEGER PRIMARY KEY, url TEXT UNIQUE, html TEXT,
     error INTEGER, old_rank REAL, new_rank REAL)''')

# Table for holding:
# Page's links to other pages
cursor.execute('''CREATE TABLE IF NOT EXISTS Links
    (from_id INTEGER, to_id INTEGER)''')

# Table for holding:
# Websites (The root directory)
cursor.execute('''CREATE TABLE IF NOT EXISTS Websites (url TEXT UNIQUE)''')

# If there is a page with URL but HTML code and error is NULL:
# There was a previous crawling process
cursor.execute('SELECT id,url FROM Pages WHERE html is NULL and error is NULL ORDER BY RANDOM() LIMIT 1')
row = cursor.fetchone()

if row is not None:
    # Restarting the previous crawling process
    print("Restarting existing crawl.  Remove spider.sqlite to start a fresh crawl.")
else:
    # Starting a crawling process from start_url
    start_url = input('Enter web url: ')

    # Cutting the last backslash from the start_url, if there is one
    if start_url.endswith('/'):
        start_url = start_url[:-1]

    website = start_url

    # Cutting the child directory from start_url, if there is one
    if start_url.endswith('.htm') or start_url.endswith('.html'):
        pointer = start_url.rfind('/')
        website = start_url[:pointer]

    if len(website) > 1:
        # Inserting website(parent root) to Websites Table
        cursor.execute('INSERT OR IGNORE INTO Websites (url) VALUES ( ? )', (website,))
        # Inserting start_url to Pages table with initial rank 1.0
        cursor.execute('INSERT OR IGNORE INTO Pages (url, html, new_rank) VALUES ( ?, NULL, 1.0 )', (start_url,))
        connection.commit()

# Getting the current website
cursor.execute('''SELECT url FROM Websites''')
websites = list()
for row in cursor:
    websites.append(str(row[0]))

print(websites)

crawl_counter = 0

# Crawl Loop
while True:
    # Asking how many pages to crawl when counter hits 0
    if crawl_counter < 1:
        page_count = input('How many pages to crawl:')
        # Breaking the loop when there is no input
        if len(page_count) < 1:
            break
        crawl_counter = int(page_count)

    crawl_counter = crawl_counter - 1

    # Getting a random row where HTML Code and error is NULL
    cursor.execute('SELECT id,url FROM Pages WHERE html is NULL and error is NULL ORDER BY RANDOM() LIMIT 1')

    row = cursor.fetchone()

    if row is None:
        # Setting loop_counter to 0 and breaking loop when there is no row to fetch
        print("All pages are retrieved.")
        crawl_counter = 0
        break

    from_id = row[0]
    url = row[1]

    print("Crawling ->", "id =", from_id, "| url =", url, end=' ')

    # Deleting all pages this page points to in order to wipe incomplete data
    cursor.execute('DELETE from Links WHERE from_id=?', (from_id,))
    # noinspection PyBroadException
    try:
        # Opening the page and reading
        document = urlopen(url, context=context)
        html = document.read()

        # Checking HTTP Status code (200 means success)
        if document.getcode() != 200:
            # Displaying the error code and inserting it to Pages table
            print("Error on page: ", document.getcode())
            cursor.execute('UPDATE Pages SET error=? WHERE url=?', (document.getcode(), url))

        # Checking content type of the document (only looking for html/text documents)
        if 'text/html' != document.info().get_content_type():
            # Deleting the record from Pages and
            print("Ignoring non text/html page")
            cursor.execute('DELETE FROM Pages WHERE url=?', (url,))
            cursor.execute('UPDATE Pages SET error=0 WHERE url=?', (url,))
            connection.commit()
            continue

        # Printing the length of HTML document
        print('| length = ('+str(len(html))+')', end=' ')

        # Using BeautifulSoup to repair and parse HTML document
        soup = BeautifulSoup(html, "html.parser")

    except:
        print("Unable to retrieve or parse page")
        cursor.execute('UPDATE Pages SET error=-1 WHERE url=?', (url,))
        connection.commit()
        continue

    # Inserting the currently crawling page to Pages table with initial rank 1.0
    cursor.execute('INSERT OR IGNORE INTO Pages (url, html, new_rank) VALUES ( ?, NULL, 1.0 )', (url,))
    # Updating the currently crawling pages html field
    cursor.execute('UPDATE Pages SET html=? WHERE url=?', (memoryview(html), url))
    connection.commit()

    # Getting all <a> tags from BeautifulSoul object because they are links to other pages
    tags = soup("a")
    href_count = 0
    # Processing all <a> tags
    for tag in tags:
        # If href attribute doesn't exist, skipping the current iteration
        href = tag.get('href', None)
        if href is None:
            continue

        # If href attribute exists but is empty, skipping the current iteration
        if len(href) < 1:
            continue

        # If href attribute is an image, skipping the current iteration
        if href.endswith('.png') or href.endswith('.jpg') or href.endswith('.gif'):
            continue

        # Cutting backslash from the href, if exists
        if href.endswith('/'):
            href = href[:-1]

        # Parsing the href, empty string for scheme indicates relative URL"
        parsed_url = urlparse(href)
        if len(parsed_url.scheme) < 1:
            # Making absolute url of the href by joining href and currently crawling page
            href = urljoin(url, href)

        # Cutting the part after # in the href, if exists
        pointer = href.find("#")
        if href.find("#") > 1:
            href = href[:pointer]

        # If href attribute is in the Websites, breaking the loop
        found = False
        for website in websites:
            if href.startswith(website):
                found = True
                break
        if not found:
            continue

        # Inserting the href to Pages table with initial rank 1.0
        cursor.execute('INSERT OR IGNORE INTO Pages (url, html, new_rank) VALUES ( ?, NULL, 1.0 )', (href,))
        href_count = href_count + 1
        connection.commit()

        # Getting the id of the href
        cursor.execute('SELECT id FROM Pages WHERE url=? LIMIT 1', (href,))
        row = cursor.fetchone()
        if row is None:
            print("Couldn't retrieve id of href ->", href)
            continue

        to_id = row[0]

        # Inserting from_id (currently crawling pages id) and to_id (href's id) to Links Table
        cursor.execute('INSERT OR IGNORE INTO Links (from_id, to_id) VALUES ( ?, ? )', (from_id, to_id))

    print("| links found =", href_count)


cursor.close()
