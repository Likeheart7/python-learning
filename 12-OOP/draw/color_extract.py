from colorgram import colorgram


def extract_color(filepath, amount):
    colors = []
    # 从图片中提取颜色
    color_extracted = colorgram.extract(filepath, amount)
    print("提取出颜色种类：", len(color_extracted))
    for color in color_extracted:
        colors.append((color.rgb.r, color.rgb.g, color.rgb.b))
    return colors
