from parcel import Parse_Chrome

parse = Parse_Chrome(
    link_to_solve='https://issaold.beltelecom.by/main.html',
    link_img_convert_to_text='https://www.prepostseo.com/ru/image-to-text'
)

captcha_pic = parse.Img(
    raw_img_store_directory='modern_parcel/pics/secpic_raw.png',
    enh_img_store_directory='modern_parcel/pics/enhpic.png'
)

captcha_pic.get_screenshot()
captcha_pic.enhance_img()

