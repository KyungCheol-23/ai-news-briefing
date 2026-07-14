from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def summarize_news(news_list):
    """
    뉴스 목록을 받아 3줄 요약 반환
    """

    articles = ""

    for news in news_list:
        articles += f"""
제목: {news['title']}
내용: {news.get('summary', '')}

"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": "너는 뉴스 브리핑 AI야. 핵심만 쉽게 요약해."
            },
            {
                "role": "user",
                "content": f"""
다음 뉴스들을 3줄로 요약해줘.

{articles}
"""
            }
        ]
    )

    return response.choices[0].message.content