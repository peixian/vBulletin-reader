vBulletin CLI Reader
=========================

This is a small python program that takes a link to a vBulletin thread, keeps track of how much you've read, and presents you with new posts every time you run `vbr [thread name]`. 

How?
---------------------------
	$ pip install vbulletin-reader
	$ vbr [thread url] [thread name]
	$ vbr [thread name]
	
vbulletin-reader stores your thread location in a nicely wrapped json file in your home directory `~/" by default. 
	
Why?
--------------------------
Realistically, there's only one vBulletin website I keep up with, and that's [The Source](http://www.mtgthesource.com/) for MTG, and there's only one thread in that I care about, which is the [Sneak & Show thread](http://www.mtgthesource.com/forums/showthread.php?27217-Deck-Sneak-and-Show/). I found it annoying to have to open up a webpage and navigate through just to check new posts, so I figured I'd write a quick & dirty python program to get it. 

References
-------------
- http://www.vbulletin.com/vbcms/content.php/367-API-Overview
- http://vb5support.com/resources/api/index.html
- https://stackoverflow.com/questions/9648281/vbulletin-getting-new-posts-on-a-particular-forum-replies-on-a-thread
- http://www.vbulletin.com/vbcms/content.php/352-Method-List
- http://www.vbulletin.com/vbcms/content.php/363-Thread-Post-Related-Methods

License
-------------------
MIT, check the LICENSE file (there's nothing special). 
