import requests
from bs4 import BeautifulSoup
import os
import time

URL = "https://travel.ettoday.net/category/%E6%96%B0%E5%8C%97/?page={page}"

def crawl_ettoday_news():
    all_news = []
    
    if not os.path.exists("news_files"):
        os.makedirs("news_files")

    for page in range(1, 4):
        print(f"正在爬第 {page} 頁...")

        url = URL.format(page=page)

        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        
        articles = soup.select('h3[itemprop="headline"] a')
        print(f"這頁抓到 {len(articles)} 篇新聞")
        
        for article in articles:
            title = article.text.strip()
            link = article["href"]

            if not link.startswith("http"):
                link = "https://travel.ettoday.net" + link
            print(f"下載中：{title}")
            
            news_response = requests.get(link)
            news_soup = BeautifulSoup(news_response.text, "html.parser")
            
            story = news_soup.select_one("div.story")
            if story is None:
                continue
            
            for img in story.find_all("img"):
                img.decompose()

            for s in story.find_all("strong"):
                s.decompose()
                
            paragraphs = story.find_all("p")
            
            content_list = []
            
            for p in paragraphs:
                text = p.get_text()
                text = text.replace("\xa0", "").replace("\u3000", "")
                text = text.strip()
                
                if text.startswith(("▲", "▲▼")):
                    continue
                if "（圖／" in text:
                    continue
                if "記者" in text and "報導" in text:
                    continue
                if text:
                    content_list.append(text)
                     
            content = "\n".join(content_list)
            
            all_news.append((title, content))
            time.sleep(1)
            
    return all_news