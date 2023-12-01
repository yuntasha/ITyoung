
# doc string

import re
import requests

UserAgent = 'User-Agent'
MyAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Safari/605.1.15'
ContentType = 'Content-Type'
ContentTypeText = 'text/html;charset=utf-8'

url = 'https://news.v.daum.net/v/20211129144552297'

headers = {
    UserAgent: MyAgent,
    ContentType: ContentTypeText
}

res = requests.get(url, headers=headers)
res.raise_for_status() # 이거 시험문제
print(res.status_code) # 이거 시험문제

with open('result.html', 'w', encoding='utf-8') as f:
    f.write(res.text)

results = re.findall(r'[\w\.-]+@[\w\.-]+', res.text) # 이거 시험문제
results = list(set(results))
print(results)