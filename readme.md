#Weekly wordpress roundup post generator script

Ok. This is a very ugly version of something that I hope works better later. On TechInAsia.com, we do [weekly roundup posts](http://www.techinasia.com/tag/china-this-week/), and currently that process in manual. The following is a weekend experiment to see how we might remove some of the heavy lifting through automation. 

So far it does the following:

* Find the date for the previous Monday, and get all posts tagged China that have been published since then. (h/t to [ChristopheD](http://stackoverflow.com/questions/1622038/find-mondays-date-with-python) for tip on how to do that)
* Output titles and links as markdown for use roundup post creation. 
* Output description excerpt, which can then be rewritten or modified. 

Improvements to come later:

* Write output to a .md file
* Include post headers, lead image, footer for roundup post
* Maybe make use of OSX's 'summary' service to summarize the entire post? 