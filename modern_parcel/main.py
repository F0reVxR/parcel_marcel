from parcel import Parse_Chrome

def main():

    parse = Parse_Chrome(
        link_to_solve='https://issaold.beltelecom.by/main.html',
        link_img_convert_to_text='https://www.prepostseo.com/ru/image-to-text'
    )

    parse.get_screenshot(
        RISTD='modern_parcel/pics/secpic_raw.png'
        )
    
    input = parse.enhance_img(
        RISTD='modern_parcel/pics/secpic_raw.png',
        EISTD='modern_parcel/pics/enhpic.png'
        )
    
    parse.input_keys(input_text=input)

if __name__ == '__main__':

    main()