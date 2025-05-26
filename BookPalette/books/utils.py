# books/utils.py

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    lv = len(hex_color)
    return tuple(int(hex_color[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def color_distance(rgb1, rgb2):
    # 단순 유클리드 거리
    return sum((a-b)**2 for a, b in zip(rgb1, rgb2)) ** 0.5