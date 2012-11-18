#!/usr/bin/env python

"""a script for fetching posts from wordpress, and then autogenerating markdown files for end-of-week-posts."""

from __future__ import division
import xmlrpclib
import datetime
from bs4 import BeautifulSoup
 
MAX_POSTS = 120
#adjust for your own domain
url = 'http://www.YOURDOMAIN.com/xmlrpc.php'
#input your blog username and pw
myusername = ''
mypassword = ''
#write tag to fetch. We use China in our roundups, example: http://is.gd/ANOKr9
tag_to_fetch = 'China'


#for weekly roundup posts, we need to figure out date for when the past week started, i.e. last monday, h/t stack overflow dude: http://is.gd/8tXkU7
today = datetime.date.today()
last_monday = str(today - datetime.timedelta(days=today.weekday()))
lastmonday_fourdigit = last_monday[5:7] + last_monday[8:10]
 
server = xmlrpclib.ServerProxy(url)
result = server.metaWeblog.getRecentPosts(url, myusername, mypassword, MAX_POSTS)


postwordcount = 0

for post in result:
  post_title = post['title']
  post_date = str(post['date_created_gmt'])
  tags = post['mt_keywords']
  categories = post['categories']
  description = post['description']
  desc_minus_image = BeautifulSoup(description).get_text()
  permalink = post['permaLink']
#  print(categories)  
  if tag_to_fetch in tags and post_date[4:8] >= lastmonday_fourdigit:
    print """###[%s](%s) %s/%s""" % (post_title, permalink, post_date[4:6], post_date[6:8])
    print(desc_minus_image[0:222]),"..."
    print("")

   

