import os

from PIL import Image, ImageDraw, ImageFont


def WH(name, surname, font):
    ascent, descent = font.getmetrics()

    space = descent - (font.getmask(name).getbbox()[3] - ascent)
    width = font.getmask(name).getbbox()[2]
    height = font.getmask(name).getbbox()[3]
    width = font.getmask(surname).getbbox()[2] if width < font.getmask(surname).getbbox()[2] \
        else width
    height += font.getmask(surname).getbbox()[3] + space

    return width, height, space


def draw_text(name, surname, font):
    offset = (20, 0)  # отступ текста от верхнего левого края
    margins = (10, 10)  # поля вокруг текста
    width, height, space = WH(name, surname, font)
    img = Image.new('RGBA',
                    (width + offset[0] + margins[0] * 2,
                     height + offset[1] + margins[1] * 2),
                    (255, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.multiline_text(offset, f'{name}\n{surname}', font=font, fill='#C4C4C4', spacing=26)

    return img, space


def mount_watermark(name, surname, headline):
    img_text, space = draw_text(name, surname, headline)
    img_finish = Image.new('RGBA', (img_logo.size[0] + img_text.size[0],
                                    img_logo.size[1]),
                           (255, 0, 0, 0))
    img_finish.paste(img_logo, (0, 0))
    height = 168 - 17
    img_finish.paste(img_text, (img_logo.size[0], int(height)))

    fixed_height = 179

    height_percent = (fixed_height / float(img_finish.size[1]))
    width_size = int((float(img_finish.size[0]) * float(height_percent)))
    img_finish = img_finish.resize((width_size, fixed_height))
    return img_finish


if os.path.exists("logo"):
    pass
else:
    os.mkdir("logo")

if os.path.isfile("input.txt"):
    pass
else:
    open("input.txt", "w+")

headline = ImageFont.truetype("./futurademic.ttf", 240)
img_logo = Image.open('watermark_pattern.png')
with open("input.txt", "r+", encoding="utf-8") as file:
    for stroke in file:
        name, surname = stroke.strip().split()
        img_finish = mount_watermark(name, surname, headline)
        # img_finish.show()
        img_finish.save(f'logo/logo_{name}_{surname}.png', 'PNG')
