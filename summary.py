from google import genai
from dotenv import load_dotenv
import os

# .env 파일 읽기
load_dotenv()

# Gemini API 연결
client = genai.Client(
    api_key=os.getenv("gemini_api_key")
)


def summarize_news(news_list):
    """
    뉴스 목록을 받아 3줄 요약을 반환한다.

    Args:
        news_list (list[dict]): get_news()가 반환한 뉴스 리스트

    Returns:
        str: Gemini가 생성한 뉴스 요약
    """

    articles = ""

    for news in news_list:
        articles += f"""
제목: {news['title']}
내용: {news['description']}

"""

    prompt = f"""
너는 뉴스 브리핑 AI다.

다음 뉴스들을 읽고 핵심만 3줄 정도로 요약해줘.

{articles}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text