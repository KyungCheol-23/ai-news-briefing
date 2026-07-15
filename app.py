from news import get_news
from summary import summarize_news

news = get_news("AI", 2)
print(news)

summary = summarize_news(news)
print(summary)
