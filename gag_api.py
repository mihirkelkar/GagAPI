import mechanize
import re
import json

from BeautifulSoup import BeautifulSoup as bs
def parser(type):
  browser = mechanize.Browser()
  browser.addheaders = [("User-agent", "Mozilla/5.0")]
  browser.set_handle_robots(False)
  html_page = browser.open("http://9gag.com/%s" %type)
  content = bs(html_page)
  articles_top_ten = content.findAll("article")
  return articles_top_ten

def get_json(type):
  articles = parser(type)
  #print articles
  json_list = [make_dict(ii) for ii in articles]
  return json.dumps(json_list)
  
def make_dict(ii):
  temp = {}
  temp["data-entry-id"] = ii["data-entry-id"]
  temp["data-entry-url"] = ii["data-entry-id"]
  temp["total-votes"] = ii["data-entry-votes"]
  temp["total-comments"] = ii["data-entry-comments"]
  temp["image"] = ii["data-entry-thumbnail-url"]
  temp["data-caption"] = ii.h2.a.text
  return temp

def get_hot_posts():
  return get_json('hot') 

def get_trending_posts():
  return get_json('trending')

def get_fresh_posts():
  return get_json('fresh')

def get_nsfw_posts():
  return get_json('nsfw')

def get_gif_posts():
  return get_json('gif')

def get_girl_posts():
  return get_json('girl')

def get_meme_posts():
  return get_json('meme')

def get_geeky_posts():
  return get_json('geeky')

def get_cute_posts():
  return get_json('cute')

def get_cosplay_posts():
  return get_json('cosplay')

def get_comic_posts():
  return get_json('comic')

def get_timely_posts():
  return get_json('timely')

def get_food_posts():
  return get_json('food')
