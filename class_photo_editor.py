from PIL import Image, ImageDraw, ImageFont
from PIL.ImageFile import ImageFile


class PhotoEditor:
    def __init__(self, photo_path: str) -> None:
        try:
            self.image = Image.open(photo_path)
        except FileNotFoundError:
            raise FileNotFoundError(f'Файл изображения {photo_path} не найден')
        except Exception as e:
            raise Exception(f'Ошибка при открытии изображения {e}')

    def resize(self, num1: int = 1, num2: int = 1) -> ImageFile:
        if (
            not isinstance(num1, int)
            or not isinstance(num2, int)
            or num1 <= 0
            or num2 <= 0
        ):
            raise ValueError(
                'num1 и num2 должны быть положительными целыми числами'
            )

        w, h = self.image.size
        new_size = (w // num1, h // num2)

        self.image = self.image.resize(new_size)
        return self.image

    def paste_photo(
        self,
        photo_path,
        num1: int = 1,
        num2: int = 1,
        from_w: int = 0,
        from_h: int = 0,
    ) -> ImageFile:
        pasted_photo = PhotoEditor(photo_path)
        pasted_photo = pasted_photo.resize(num1, num2)

        self.image.paste(pasted_photo, (from_w, from_h), pasted_photo)
        return self.image

    def add_text(
        self,
        text: str,
        font_path: str,
        font_size: int,
        color: str,
        from_w: int = 0,
        from_h: int = 0,
    ) -> ImageFile:
        draw = ImageDraw.Draw(self.image)
        font = ImageFont.truetype(font_path, font_size)

        draw.text((from_w, from_h), text, font=font, fill=color)
        return self.image


img = PhotoEditor('ideal_working_place.jpg')
img.resize(2, 2)
img.paste_photo('python.png', 4, 4, 20, 5)
img = img.add_text(
    'Hello World!', 'MultiTypeGamer Chess.otf', 40, 'coral', 320, 35
)
img.save('hello_world.jpg')
img.show()
