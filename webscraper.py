import requests
from bs4 import BeautifulSoup

response = requests.get('https://edition.cnn.com/travel/article/scenic-airport-landings-2020/index.html')

soup = BeautifulSoup(response.content, 'html.parser')

title = soup.title.get_text(strip=True)

updated_date = soup.find('meta', property='article:modified_time')['content']

byline_element = soup.find('meta', attrs={'name': 'author'})
byline = byline_element['content'] if byline_element else 'Byline not found'

paragraphs = soup.find_all('p')

content = "\n".join([p.get_text(strip=True) for p in paragraphs])

print("Title:", title)
print("Updated Date:", updated_date)
print("Byline:", byline)
print("Content:", content)
