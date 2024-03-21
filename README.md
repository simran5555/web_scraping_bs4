# web_scraping_bs4

- using beautiful soup module to extract needed information
- import bs4 from BeautifulSoup
- extracting contents : response = requests.get("https://news.ycombinator.com/") yc_web_page = response.text
- extracting soup : BeautifulSoup(yc_web_page, "html.parser")
- finding different elements is possible through a wide range of functions available in bs4 module : find, find_all, select, select_one
