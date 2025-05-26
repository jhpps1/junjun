import json

# 원본 json 파일 경로
input_path = 'books/fixtures/category_groups_with_color.json'
# 변환될 django fixture 파일 경로
output_path = 'books/fixtures/category_for_fixture.json'

# 원본 파일 읽기
with open(input_path, encoding='utf-8') as f:
    data = json.load(f)

# django fixture 형식으로 변환
django_fixture = []
for cat in data:
    django_fixture.append({
        "model": "books.category",
        "pk": cat["pk"],
        "fields": {
            "name": cat["name"],
            "color": cat["color"]
        }
    })

# 결과 파일로 저장
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(django_fixture, f, ensure_ascii=False, indent=2)

print(f"변환 완료: {output_path}")
