import feedparser
from urllib.parse import quote

def get_news(keyword, max_result = 10): # 기사 검색기
    """
     keyword와 관련된 뉴스의 제목과 링크를 반환

    Args:
        keyword (str): 검색 키워드
        max_results (int): 가져올 기사 개수

    Returns:
        list[dict]: entries를 모아둔 리스트
    """
    keyword = quote(keyword)

    url = (
        f"https://news.google.com/rss/search?q={keyword}"
        "&hl=ko&gl=KR&ceid=KR:ko"
    )

    feed = feedparser.parse(url)

    news = []

    for item in feed.entries[:max_result]:
        news.append({
            "title": item.title,
            "description": item.description,    #나중에 요약 부분은 삭제
            "link": item.link
        })
    
    return news

import trafilatura

def get_article(link): # 기사 본문추출기
    """
    기사 링크에서 본문을 추출

    Args:
        link (str): 기사 링크
    
    Returns:
        str: 기사 본문
    """
    download = trafilatura.fetch_url(link)
    
    if download is None:
        return None
    
    text = trafilatura.extract(download)
    return text