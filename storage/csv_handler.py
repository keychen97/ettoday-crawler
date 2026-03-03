import pandas as pd
import os

def save_to_csv(all_news):
    if not os.path.exists("news_files"):
        os.makedirs("news_files")

    for title, content in all_news:
        safe_title = (
            title.replace("/", "_")
            .replace("\\", "_")
            .replace(":", "_")
            .replace("*", "_")
            .replace("?", "_")
            .replace('"', "_")
            .replace("<", "_")
            .replace(">", "_")
            .replace("|", "_")
        )

        df = pd.DataFrame([[title, content]], columns=["title", "content"])
        df.to_csv(
            f"news_files/{safe_title}.csv",
            index=False,
            header=False,
            encoding="utf-8-sig"
        )

    print("CSV 儲存完成")