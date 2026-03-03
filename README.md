# Ettoday News Crawler

一個用 Python 編寫的爬蟲專案，專門抓取 Ettoday 旅遊新聞，並支援存到 MySQL 資料庫和匯出成 CSV 檔案。

## 功能特色

- 爬取 Ettoday 新北旅遊新聞的標題與內容
- 清理文字格式與圖片標籤
- 存入 MySQL 資料庫，方便後續查詢與分析
- 匯出 CSV 檔，方便資料備份與閱讀

## 安裝說明

建議使用虛擬環境：

```bash
python -m venv .venv
source .venv/bin/activate    # Linux/macOS
.venv\Scripts\activate       # Windows
```

## 安裝套件
```bash
pip install -r requirements.txt
```

## 使用方法

執行主程式：

```bash
python main.py
```

程式會：
抓取新聞資料
寫入 MySQL
匯出 CSV 檔到 news_files 資料夾
資料庫設定
資料庫連線設定請在 config/settings.py 的 DB_CONFIG 中調整，
也可以使用 .env 環境變數設定：

```bash
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=你的密碼
DB_NAME=ettoday_news
```

## 專案結構
.
├── crawler/          # 爬蟲程式碼
├── database/         # 資料庫操作程式碼
├── storage/          # CSV 匯出程式碼
├── config/           # 設定檔與環境變數
├── news_files/       # 儲存新聞 CSV 檔案
├── main.py           # 主程式入口
└── README.md         # 專案說明檔

## 授權
MIT License

## 聯絡方式

有問題歡迎提 issue 或 email: keychenwork2018@gmail.com
