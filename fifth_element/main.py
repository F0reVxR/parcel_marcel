import time

from parselline import FParser

def main():

    parser = FParser(link='https://5element.by/catalog/571-buterbrodnicy')
    parser.accept_cookies()
    try:
        while True:
            parser.get_all_links()
            parser.click_next_page()
    except Exception as e:
        print(e)
    print(parser.links_list)


    
if __name__ == '__main__':
    main()