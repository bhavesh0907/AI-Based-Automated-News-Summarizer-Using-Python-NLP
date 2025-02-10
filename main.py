from text_scraper import fetch_news
from summarization_model import summarize_article

def main():
    news_url = input("Enter the news article URL: ")
    article_content = fetch_news(news_url)
    summary = summarize_article(article_content)
    print("\nNews Summary:\n", summary)

if __name__ == "__main__":
    main()
