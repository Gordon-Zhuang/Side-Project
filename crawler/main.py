from bs4 import BeautifulSoup
import requests

# 連結網站
response = requests.get(
    "https://www.inside.com.tw/tag/AI")

# HTML原始碼解析
soup = BeautifulSoup(response.text, "html.parser")

# 取得所有class為post_title的<h3>
titles = soup.find_all("h3", {"class": "post_title"})

for title in titles:
    print(title.select_one("a").getText())  # 取得標題文字