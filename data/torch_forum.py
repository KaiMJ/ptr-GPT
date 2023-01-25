# Scrap pytorch forum using beautiful soup
import requests
from bs4 import BeautifulSoup

# Get the page
page = requests.get("https://discuss.pytorch.org/t/cnn-sometimes-starts-outputting-only-zeros-and-does-not-learn-during-training/170911")
# page = requests.get("https://www.google.com/")

multiply = lambda x: x * 2


# Parse the page
soup = BeautifulSoup(page.content, 'html.parser')

posts = soup.find_all('div', "post")
original_posts = posts[0]
original_content = original_posts.findChildren()

reply_posts = posts[1:]
title = soup.find('div', {"id": "topic-title"}).find('a').text

reply = soup.find_all('div', 'post')[1]
reply_content = reply.findChild().findNextSiblings()

# set data with title and spread reply content
data = [title + '\n'] + [i.text for i in original_content] + ["\n"] +  [i.text for i in reply_content]


print(data)
# Write the title to a file
with open('title.txt', 'w') as f:
    f.write('\n'.join(data))