from crawler.ettoday_crawler import crawl_ettoday_news
from database.mysql_handler import save_to_mysql
from storage.csv_handler import save_to_csv
import os

if not os.path.exists("news_files"):
    os.makedirs("news_files")

def main():
    print("開始爬蟲...")

    all_news = crawl_ettoday_news()

    print("開始寫入 MySQL...")
    save_to_mysql(all_news)

    print("開始儲存 CSV...")
    save_to_csv(all_news)

    print("爬取完成！")

if __name__ == "__main__":
    main()