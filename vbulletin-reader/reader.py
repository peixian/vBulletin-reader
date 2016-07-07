import requests
import html2text
from bs4 import BeautifulSoup
import bs4
from termcolor import colored

class vBulletin_Reader(object):

    def __init__(self):
        pass

    def _open_location(self):
        """
        Opens the saved thread location and data
        """
        pass

    def _write_location(self):
        """
        Writes out the saved location data
        """
        pass


    def _parse_post_message(self, post):
        """
        Returns the direct text of the post, avoids the children text
        """
        post_contents = post.blockquote
        post_text =  [text.text if type(text) == bs4.element.Tag else text for text in post_contents]
        post_text = list(filter(None, map(lambda x: x.strip(), post_text)))


        date = post.find_all(class_="date")[0].text
        username = post.find_all(class_="username_container")[0].strong.text
        post = {"username": username, "date": date, "message": post_text}    
        return post
        
    def parse_thread(self, thread_link):
        """
        Parses the thread information
        """

        req = requests.get(thread_link)
        if req.status_code == 200:
            data = BeautifulSoup(req.content, "html.parser")
            post_messages = data.find(id="posts").find_all("li", recursive=False)
            post_messages = list(filter(None, map(lambda x: self._parse_post_message(x), post_messages)))
            
            for post in post_messages[-3:]:
                print("{} - {}\n{}\n".format(colored(post['username'], 'green'), post['date'], colored(post['message'], 'yellow')))

        else:
            print("Something's wrong, check the thread link.")



vbr = vBulletin_Reader()
vbr.parse_thread("http://www.mtgthesource.com/forums/showthread.php?27217-Deck-Sneak-and-Show")
