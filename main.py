import os

from PIL import Image, ImageDraw, ImageFont

HEIGHT = 179  # кроп по высоте


# Отвечает за формирование размеров текста
def WH(name, surname, font):
    ascent, descent = font.getmetrics()

    space = descent - (font.getmask(name).getbbox()[3] - ascent)
    width = font.getmask(name).getbbox()[2]
    height = font.getmask(name).getbbox()[3]
    width = font.getmask(surname).getbbox()[2] if width < font.getmask(surname).getbbox()[2] \
        else width
    height += font.getmask(surname).getbbox()[3] + space

    return width, height, space


# Отвечает за отрисовку текста ФИО
def draw_text(name, surname, font, fill):
    offset = (20, 0)  # отступ текста от верхнего левого края
    margins = (10, 10)  # поля вокруг текста
    width, height, space = WH(name, surname, font)
    img = Image.new('RGBA',
                    (width + offset[0] + margins[0] * 2,
                     height + offset[1] + margins[1] * 2),
                    (255, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.multiline_text(offset, f'{name}\n{surname}', font=font, fill=fill, spacing=26)

    return img, space


def mount_watermark(name, surname, img_logo, headline, fill):
    img_text, space = draw_text(name, surname, headline, fill)
    img_finish = Image.new('RGBA', (img_logo.size[0] + img_text.size[0],
                                    img_logo.size[1]),
                           (255, 0, 0, 0))
    img_finish.paste(img_logo, (0, 0))
    height = 168 - 17
    img_finish.paste(img_text, (img_logo.size[0], int(height)))

    fixed_height = HEIGHT

    height_percent = (fixed_height / float(img_finish.size[1]))
    width_size = int((float(img_finish.size[0]) * float(height_percent)))
    img_finish = img_finish.resize((width_size, fixed_height))
    return img_finish


def checkDir():
    if not os.path.isfile("input.txt"):
        open('input.txt', 'w')
        raise "Отсуствует файл input.txt"
    if not os.path.exists("result"):
        os.mkdir("result")
    if not os.path.exists("result/logo_post"):
        os.mkdir("result/logo_post")
    if not os.path.exists("result/logo_watermark"):
        os.mkdir("result/logo_watermark")


def createPostImage(headline, logo):
    with open("input.txt", "r+", encoding="utf-8") as file:
        for stroke in file:
            text = stroke.strip().split()
            name, surname = text[0], text[1]
            img_finish = mount_watermark(name, surname, logo, headline, '#C4C4C4')

            img_finish.save(f'result/logo_post/post_{name}_{surname}.png', 'PNG')


def createWatermarkImage(headline, logo):
    with open("input.txt", "r+", encoding="utf-8") as file:
        for stroke in file:
            text = stroke.strip().split()
            name, surname = text[0], text[1]
            img_finish = mount_watermark(name, surname, logo, headline, '#FFFFFF')

            img_finish.save(f'result/logo_watermark/watermark_{name}_{surname}.png', 'PNG')


if __name__ == "__main__":
    checkDir()
    # установка шрифта и заготовок логотипов
    headline = ImageFont.truetype("fonts/futurademic.ttf", 240)
    logo_watermark = Image.open('patterns/watermark.png')
    logo_post = Image.open('patterns/post.png')

    createPostImage(headline, logo_post)
    createWatermarkImage(headline, logo_watermark)
