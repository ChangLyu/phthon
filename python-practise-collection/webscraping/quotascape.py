import requests
import bs4
base_url = 'http://quotes.toscrape.com/page/{}/'
authors=set()
count = 1

while True:
        page = requests.get(base_url.format(count))
        if 'No quotes found!' in page.text:
            break
        page_content= bs4.BeautifulSoup(page.text, 'lxml')

        for author in page_content.select('.author'):
            authors.add(author.text)
        count +=1

print(authors)