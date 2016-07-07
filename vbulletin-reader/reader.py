import requests
import html2text
from bs4 import BeautifulSoup
import bs4
from termcolor import colored
import os.path
import json

class vBulletin_Reader(object):

    def __init__(self, thread_link, thread_name):
        self.thread = thread_link
        self.thread_name = thread_name

    def _open_location(self):
        """
        Opens the saved thread location and data
        """
        pass

    def _write_location(self):
        """
        Writes out the saved location data
        """
        file_loc = 'vbr.json'
        if (os.path.isfile(file_loc)):
            with open(file_loc, "r+") as location_data:
                self.loc_data = json.load(location_data)
                self.loc_data[self.thread_name]["last_read"] = self.post_messages[-1]["postcounter"]
                json.dump(self.loc_data, location_data)
        else:
            thread_info = {'url': self.thread, 'last_read': self.post_messages[-1]['postcounter']}
            data = {self.thread_name: thread_info}
            with open(file_loc, "w") as location_data:
                json.dump(data, location_data)
            


    def _message_format(self, post_text):
        """
        Takes in a list of str's, combines them into one large str, and formats for blockquotes
        """
        msg = '\n\n'.join(post_text)
        return msg
    
    def _parse_post_message(self, post):
        """
        Returns the direct text of the post, avoids the children text
        """
        post_contents = post.blockquote
        post_text =  [text.text if type(text) == bs4.element.Tag else text for text in post_contents]
        post_text = list(filter(None, map(lambda x: x.strip(), post_text)))

        post_text = self._message_format(post_text)
        date = post.find_all(class_="date")[0].text
        username = post.find_all(class_="username_container")[0].strong.text
        postcounter = post.find_all(class_="postcounter")[0].text
        post = {"username": username, "date": date, "message": post_text, 'postcounter': postcounter}    
        return post
        
    def parse_thread(self):
        """
        Parses the thread information
        """

        req = requests.get(self.thread)
        if req.status_code == 200:
            data = BeautifulSoup(req.content, "html.parser")
            post_messages = data.find(id="posts").find_all("li", recursive=False)
            post_messages = list(filter(None, map(lambda x: self._parse_post_message(x), post_messages)))

            
            #for post in post_messages[-3:]:
            #    print("{} - {} - Post {}\n{}\n".format(colored(post['username'], 'green'), post['date'], post["postcounter"], colored(post['message'], 'yellow')))
            self.post_messages = post_messages
            self._write_location()
        else:
            print("Something's wrong, check the thread link.")



vbr = vBulletin_Reader('http://www.mtgthesource.com/forums/showthread.php?27217-Deck-Sneak-and-Show', "sneak")
vbr.parse_thread()
