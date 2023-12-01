
# 스크래핑
import requests
import bs4

url = "https://www.naver.com"   

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Safari/605.1.15',
           'Content-Type': 'text/html;charset=utf-8'}
res = requests.get(url= url, headers= headers)
res.raise_for_status()
print(res.status_code)

# print(res.text)
with open('b1117.html', 'w', encoding='utf-8') as f:
    f.write(res.text)

soup = bs4.BeautifulSoup(res.text, 'lxml')

print(soup.text)