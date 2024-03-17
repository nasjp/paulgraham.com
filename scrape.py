import os
import requests
from bs4 import BeautifulSoup

def save_article(url, directory="articles"):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 記事のタイトルをファイル名として使用
    title = soup.find('title').text
    filename = f"{title}.txt".replace(" ", "_").replace("/", "_")

    # docsディレクトリが存在しない場合は作成
    if not os.path.exists(directory):
        os.makedirs(directory)

    # 記事の内容をファイルに保存
    with open(os.path.join(directory, filename), 'w', encoding='utf-8') as file:
        file.write(soup.get_text())

# このURLからコンテンツをスクレイピング
url = "https://www.paulgraham.com/articles.html"
save_article(url)