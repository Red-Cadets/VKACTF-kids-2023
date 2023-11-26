from PIL import Image

# Открываем изображение
image_path = "hidden.png"
img = Image.open(image_path)
pixels = img.load()


pos = [
    564,
    872,
    1210,
    178,
    1170,
    128,
    26,
    424,
    10,
    468,
    766,
    712,
    870,
    1176,
    454,
    1150,
    1078,
    400,
    1114,
    1106,
    1206,
    1016,
    1234,
    382,
    138,
    804,
    578,
    412,
    796,
    144,
    148,
    368,
    736,
    724,
]


flag = "*" * len(pos)

for p in range(len(pos)):
    x, y = int(pos[p] / 2), int(pos[p] / 2)
    r, g, b = img.getpixel((x, y))
    pixels[x, y] = (0, 0, ord(flag[p]))

img.save("data.png")
