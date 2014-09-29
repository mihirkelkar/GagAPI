import requests
import json
import re

from BeautifulSoup import BeautifulSoup as bs

BASE_URL = "https://9gag.com"

def get_page(page_url = ""):
  try:
    #Solved the inifnite scrolling problem.
    content = requests.get("%s%s" %(BASE_URL, page_url)).text
    return bs(content)
  except:
    return None

def retrieve_articles(number_of_pages = 1):
  extend_url = ""
  all_articles = list()
  while number_of_pages > 0:
    content = get_page(extend_url)
    if content == None:
      return None
    extend_url = content.find('a', attrs={'class' : 'btn badge-load-more-post'})['href']
    print extend_url
    all_articles += content.findAll("article")
    number_of_pages -= 1
    print all_articles[0]
  return all_articles

#Add filters such that the user can go ahead and limit whether
#they want only gifs, images, posts with comments above this number,#posts with comments greater than 
#Make sure that the page number limit is 100. 
 
def annotate(number_of_pages = 1, filter = None):
  final_result = list()
  for ii in retrieve_articles(number_of_pages):
    #TODO : Make the dictionary by getting other elements out. 
    try:
      type = ii.find('span', attrs = {'class' : 'play badge-gif-play hide'}).text
      media_url = ii.find('img', attrs = {'class' : 'badge-item-animated-img'})['src'] 
    except:
      type = 'Image'
      media_url = ii.find('img', attrs = {'class' : 'badge-item-img'})['src']
    post_url = ii['data-entry-url']
    votes = ii['data-entry-votes']
    comments = ii['data-entry-comments']
    title = ii.find('img', attrs={'class':'badge-item-img'})['alt'] 
    print title
    final_result.append({
      "type" : type , 
      "post_url" : post_url,
      "votes" : votes,
      "comments" : comments,
      "title" : title,
      "media_url" : media_url
    })
  return final_result

def main():
  for ii in annotate():
    print ii
    print "============"
  
if __name__ == "__main__":
  main()
