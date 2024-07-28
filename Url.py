import requests
from bs4 import BeautifulSoup
import re

url = 'https://tgchana.site/tme'

try:
    response = requests.get(url)
    response.raise_for_status()  # تحقق من وجود أي أخطاء

    soup = BeautifulSoup(response.content, 'html.parser')

    pattern = re.compile(r'^https://tgchana\.site/tme:.+')
    links = []
    for link in soup.find_all('a', href=True):
        href = link['href']
        if pattern.match(href):
            links.append(href)

    for link in links:
        print(link)

except requests.exceptions.RequestException as e:
    print(f"Error fetching the URL: {e}")