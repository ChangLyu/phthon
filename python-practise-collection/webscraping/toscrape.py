import requests
import bs4

base_url = 'https://books.toscrape.com/catalogue/category/books_1/page-{}.html'

five_stars_books = []
for page_num in range(1, 51):
    page_content = requests.get(base_url.format(page_num))
    soup = bs4.BeautifulSoup(page_content.text, 'lxml')
    book_elements = soup.select('.product_pod')
    for book_element in book_elements:
        if len(book_element.select('.star-rating.Five')) != 0:
            # we need to check the structure of the html to grad the title we want
            title = book_element.select('a')[1]['title']
            five_stars_books.append(title)

print(five_stars_books)


# try to export to excel
