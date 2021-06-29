import requests
import bs4
result = requests.get('https://en.wikipedia.org/wiki/Machine_learning')
soup = bs4.BeautifulSoup(result.text, 'lxml')
items = soup.select('.toctext')
for item in items:
    print(item.text)
    

count = 0
for image in soup.select('.thumbimage'):
    image= requests.get('http:'+image['src'])
    f=open('./assets/images/image_'+str(count)+'.jpg','wb')
    f.write(image.content)
    count +=1