# Data wrangling, Data quality Project

Web-Scale Extraction of Structured Data -- textual extraction


We used two techniques, web crawling and web scraping. Web crawling is an
operation in which a spider retrieves pages from the web and visits all the links in a page recursively
and automatically. Whereas web scraping is the operation of discovering and extracting the content
of the web page itself, for example, extraction of images, text, tables..etc.
For web crawling, we used scrapy library and for web scraping we used trafilatura library. The
least one retrieves only text data from a web page. Since a web page has a lot of textual data, like
the data in the header and footer, we can call it irrelevant data and it has no relation with the
topic exposed in the page. Therefore, trafilatura extracts the mean text of the content of a web
page. We extract the page’s url, title and content (text).