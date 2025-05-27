import json
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Convert bestsellers_30.json to Django fixture format'

    def handle(self, *args, **options):
        # 원본 파일 읽기
        with open('books/fixtures/bestsellers_30.json', 'r', encoding='utf-8') as f:
            books = json.load(f)

        # Django fixture 형식으로 변환
        fixture_data = []
        for i, book in enumerate(books, start=1):
            if isinstance(book, dict) and 'title' in book:  # 유효한 도서 데이터인 경우만 처리
                fixture_book = {
                    "model": "books.book",
                    "pk": i,
                    "fields": {
                        "title": book.get('title', ''),
                        "author": book.get('author', ''),
                        "publisher": book.get('publisher', ''),
                        "pubDate": book.get('pubDate', ''),
                        "isbn13": book.get('isbn13', ''),
                        "description": book.get('description', ''),
                        "categoryId": book.get('categoryId', None),
                        "categoryName": book.get('categoryName', ''),
                        "cover": book.get('cover', '')
                    }
                }
                fixture_data.append(fixture_book)

        # 변환된 데이터 저장
        output_path = 'books/fixtures/bestsellers_30_fixture.json'
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(fixture_data, f, ensure_ascii=False, indent=2)

        self.stdout.write(self.style.SUCCESS(f'Successfully converted to {output_path}'))
