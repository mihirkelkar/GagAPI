Unofficial 9GAG API
================
<center><img src = "http://upload.wikimedia.org/wikipedia/fr/2/28/9gag_new_logo.png" height = "200" width = "200" /></center>
</br>
<h2> One Call to Rule them All</h2>


The below call will fetch you the standard data for all posts on the hot page.

get_posts_from_page()

Specify the following as attributes to get more filtered, pivoted data:
<table>
  <th>
    Criteria for call
  </th>
  <th>
    Function Call
  </th>
  <tr>
    <td>100 scrolls for the hot page</td>
    <td> get_posts_from_page(number_of_pages = 100)
  </tr>
  <tr>
    <td>100 scrolls for the hot page<br>Only gifs</td>
    <td> get_posts_from_page(number_of_pages = 100, media_type = 'gif')
  </tr>
  <tr>
    <td>50 scrolls of the cosplay page</td>
    <td> get_posts_from_page(number_of_pages = 50, page_type = 'cosplay')
  </tr>
  <tr>
    <td>All posts on the hot page for 50 scrolls which have more than 100 comments</td>
    <td> get_posts_from_page(number_of_pages = 50, comments_more_than = 100)
  </tr>
  <tr>
    <td>Posts on 50 scrolls of the trending page with more than 40 votes</td>
    <td> get_posts_from_page(number_of_pages = 50, page_type = 'trending', more_votes_than = 40)
  </tr>
</table>

All filtering criteria can be used in a single function call.

A typical output would look like this:
{

  "votes": 12591,

  "title": "I'm spending holidays in Germany - it was a hard lesson..",

  "comments": 547, "post_url": "http://9gag.com/gag/awbQRAB",
  
  "type": "Image",
  
  "media_url" :   "http://img-9gag-lol.9cache.com/photo/awbQRAB_460s.jpg"

}
