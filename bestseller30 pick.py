import requests
import json

# 알라딘 API 키 설정
API_KEY = 'ttbjungi29041414002'
ENDPOINT = 'http://www.aladin.co.kr/ttb/api/ItemList.aspx'

# API 요청 파라미터 설정
params = {
    'ttbkey': API_KEY,
    'QueryType': 'Bestseller',
    'MaxResults': 30,
    'start': 1,
    'SearchTarget': 'Book',
    'Output': 'js',
    'Version': '20131101'
}

# API 요청 및 응답 처리
response = requests.get(ENDPOINT, params=params)
data = response.json()

# 베스트셀러 도서 목록 추출
bestsellers = []
for item in data.get('item', []):
    book = {
        'title': item.get('title'),
        'author': item.get('author'),
        'publisher': item.get('publisher'),
        'pubDate': item.get('pubDate'),
        'isbn13': item.get('isbn13'),
        'description': item.get('description'),
        'categoryId': item.get('categoryId'),
        'categoryName': item.get('categoryName'),
        'cover': item.get('cover')
    }
    bestsellers.append(book)

# 결과를 JSON 파일로 저장
with open('bestsellers_30.json', 'w', encoding='utf-8') as f:
    json.dump(bestsellers, f, ensure_ascii=False, indent=2)

print(f"총 {len(bestsellers)}권의 베스트셀러 정보를 수집하여 저장하였습니다.")
