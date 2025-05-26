import json
import requests
from datetime import datetime

from django.core.management.base import BaseCommand
from books.models import Category, Book

API_KEY = "ttbjhpark9706021328002"
CATEGORY_JSON_PATH = "books/fixtures/category_groups_with_color.json"

class Command(BaseCommand):
    help = "알라딘 Open API 매뉴얼 기반, 카테고리별로 CID를 순서대로 조회하며 도서 3권까지 자동 등록"

    def handle(self, *args, **kwargs):
        with open(CATEGORY_JSON_PATH, encoding="utf-8") as f:
            categories = json.load(f)

        total_created = 0
        total_existing = 0
        total_errors = 0
        total_fail = 0

        for cat in categories:
            category_obj = Category.objects.get(pk=cat["pk"])
            cids = cat.get("cid_list", [])

            found_books = []
            used_cid = None

            for cid in cids:
                url = (
                    f"http://www.aladin.co.kr/ttb/api/ItemList.aspx?"
                    f"ttbkey={API_KEY}&QueryType=CategoryBest&MaxResults=10&start=1&SearchTarget=Book"
                    f"&CategoryId={cid}&output=js&Version=20131101"
                )
                try:
                    res = requests.get(url, timeout=10)
                    data = res.json()
                except Exception as e:
                    self.stdout.write(self.style.WARNING(f"{cat['name']} cid {cid} 요청 실패: {e}"))
                    continue

                item_list = data.get("item", [])
                self.stdout.write(self.style.WARNING(
                    f"{cat['name']} ({cid}) item 갯수: {len(item_list)}"
                ))

                if item_list:
                    found_books = item_list[:3]  # 최대 3권만
                    used_cid = cid
                    break  # 찾으면 멈춤

            if not found_books:
                self.stdout.write(self.style.ERROR(
                    f"‼️ {cat['name']} ({cat['pk']}) 카테고리: 모든 CID에서 도서 데이터 없음"
                ))
                total_fail += 1
                continue

            created = 0
            existing = 0
            errors = 0

            for item in found_books:
                title = item.get("title", "")[:200]
                author = item.get("author", "")[:100]
                cover = item.get("cover", "")
                summary = item.get("description", "")
                pubdate = item.get("pubDate", "")
                published_date = None
                if pubdate and len(pubdate) == 8:
                    try:
                        published_date = datetime.strptime(pubdate, "%Y%m%d").date()
                    except:
                        published_date = None
                isbn = item.get("isbn13", "")[:20] if item.get("isbn13") else None

                try:
                    obj, is_created = Book.objects.get_or_create(
                        title=title,
                        author=author,
                        category=category_obj,
                        defaults={
                            "cover": cover,
                            "summary": summary,
                            "published_date": published_date,
                            "isbn": isbn,
                        }
                    )
                    if is_created:
                        self.stdout.write(self.style.SUCCESS(f"INSERT: {title} | {author}"))
                        created += 1
                        total_created += 1
                    else:
                        self.stdout.write(self.style.WARNING(f"EXISTING: {title} | {author}"))
                        existing += 1
                        total_existing += 1
                except Exception as e:
                    self.stdout.write(self.style.ERROR(
                        f"ERROR: {title} | {author} | isbn={isbn} | {e}"
                    ))
                    errors += 1
                    total_errors += 1

            self.stdout.write(self.style.SUCCESS(
                f"{cat['name']} (CID: {used_cid}) → 신규:{created}, 중복:{existing}, 에러:{errors}"
            ))

        self.stdout.write(self.style.SUCCESS(
            f"\n총 신규 등록: {total_created}, 기존 중복: {total_existing}, 에러: {total_errors}, 도서 없는 카테고리: {total_fail}"
        ))
        self.stdout.write(self.style.SUCCESS("알라딘 자동입력 종료"))
