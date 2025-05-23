import json
import colorsys

def generate_n_colors(n):
    colors = []
    for i in range(n):
        hue = i / n
        lightness = 0.55
        saturation = 0.68
        rgb = colorsys.hls_to_rgb(hue, lightness, saturation)
        rgb = tuple(int(255 * x) for x in rgb)
        hex_color = '#{:02X}{:02X}{:02X}'.format(*rgb)
        colors.append(hex_color)
    return colors

# 카테고리 JSON 파일명 지정 (필요에 맞게)
INPUT_FILENAME = "category_groups.json"
OUTPUT_FILENAME = "category_groups_with_color.json"

# 1. 111개 색상 자동 생성
auto_colors = generate_n_colors(111)

# 2. 카테고리 파일 불러오기
with open(INPUT_FILENAME, "r", encoding="utf-8") as f:
    categories = json.load(f)

# 3. 색상 할당
for idx, cat in enumerate(categories):
    cat["color"] = auto_colors[idx]

# 4. 결과 저장
with open(OUTPUT_FILENAME, "w", encoding="utf-8") as f:
    json.dump(categories, f, ensure_ascii=False, indent=2)

print(f"✔ {len(categories)}개 카테고리에 색상 자동 배정 완료! 결과: {OUTPUT_FILENAME}")
