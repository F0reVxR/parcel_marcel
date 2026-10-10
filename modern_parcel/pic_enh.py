import os
from PIL import Image, ImageEnhance

def enhance_pic(path: str, save_directory: str) -> None:
    image = Image.open(os.path.abspath(f'{path}'))

    if image.mode != "RGB":
        image = image.convert("RGB")

    brightness_factor = 1.2
    enhancer_b = ImageEnhance.Brightness(image)
    bright_img = enhancer_b.enhance(brightness_factor)

    contrast_factor = 1.5
    enhancer_c = ImageEnhance.Contrast(bright_img)
    final_img = enhancer_c.enhance(contrast_factor)

    final_img = final_img.convert('1')
    final_img.save(f"{save_directory}")