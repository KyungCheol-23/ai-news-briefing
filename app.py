from news import get_news
keyword = input("원하는 키워드를 입력해주세요!")
print(f"입력한 키워드: {keyword}")

articles = get_news("인공지능", 3)

for article in articles:
    print(article["link"])
