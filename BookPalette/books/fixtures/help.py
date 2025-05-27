import json

# 파일 로드
with open('bestseller_data.json', encoding='utf-8') as f:
    bestseller_data = json.load(f)
with open('category_groups_with_color.json', encoding='utf-8') as f:
    category_groups = json.load(f)
with open('category_for_fixture.json', encoding='utf-8') as f:
    category_for_fixture = json.load(f)

# 1. cid -> group_name 맵핑
cid_to_group_name = {}
for group in category_groups:
    name = group['name']
    for cid in group['cid_list']:
        cid_to_group_name[cid] = name

# 2. group_name -> category_for_fixture pk 맵핑
name_to_pk = {}
for cat in category_for_fixture:
    name = cat['fields']['name']
    pk = cat['pk']
    name_to_pk[name] = pk

# 3. 변환
books_for_fixture = []
for book in bestseller_data:
    cid = book.get('categoryId')
    group_name = cid_to_group_name.get(cid)
    pk = name_to_pk.get(group_name) if group_name else None

    books_for_fixture.append({
        "title": book.get("title"),
        "author": book.get("author"),
        "category": pk,
        "cover": book.get("cover"),
        "summary": book.get("description"),
        "published_date": book.get("pubDate"),
        "isbn": book.get("isbn13"),
    })

# Django fixture 형식으로 변환
django_fixture = []
for idx, book in enumerate(books_for_fixture, 1):
    django_fixture.append({
        "model": "books.book",
        "pk": idx,
        "fields": book
    })

# 저장
output_path = 'bestseller_books_django_format.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(django_fixture, f, ensure_ascii=False, indent=2)
print(f'Successfully created {output_path} with {len(django_fixture)} books.')
