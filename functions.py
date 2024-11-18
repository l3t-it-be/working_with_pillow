from PIL import Image, ImageDraw, ImageFont
from PIL.ImageFile import ImageFile


def new_photo(name: str, num1: int, num2: int) -> ImageFile:
    image = Image.open(name)
    w, h = image.size
    return image.resize((w // num1, h // num2))


img = new_photo('ideal_working_place.jpg', 2, 2)

img_2 = new_photo('python.png', 4, 4)

img.paste(img_2, (20, 5), img_2)

draw = ImageDraw.Draw(img)
font = ImageFont.truetype('MultiTypeGamer Chess.otf', 40)
draw.text((320, 35), 'Hello World!', font=font, fill='coral')

img.save('hello_world.jpg')
img.show()
