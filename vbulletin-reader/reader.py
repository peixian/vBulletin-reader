import requests
import html2text
from bs4 import BeautifulSoup
import bs4

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
        print(post)
        post_text =  [text.text if type(text) == bs4.element.Tag else text for text in post.contents]
        post_text = list(filter(None, map(lambda x: x.strip(), post_text)))

        return post_text
    
    def parse_thread(self, thread_link):
        """
        Parses the thread information
        """

        req = requests.get(thread_link)
        if req.status_code == 200:
            data = BeautifulSoup(req.content, "html.parser")
            posts = map(lambda x: x.blockquote, data.find(id="posts").find_all("li", recurisve=False))
            post_messages = map(lambda x: self._parse_post_message(x), posts)

            for post_message in post_messages:
                print(post_message)
        else:
            print("Something's wrong, check the thread link.")



vbr = vBulletin_Reader()
vbr.parse_thread("http://www.mtgthesource.com/forums/showthread.php?27217-Deck-Sneak-and-Show")
