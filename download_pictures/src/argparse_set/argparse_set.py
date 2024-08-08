import argparse


DESCRIPTION ='Download files from urls'
DATE_HELP ='Input list urls for download file'
TEST_HELP = 'Show working script with default urls'
URLS = [
    'https://hotwalls.ru/wallpapers/2560x1600/zamok_na_holme.jpg', 
    'https://get.wallhere.com/photo/lake-mountain-tree-water-landscape-1076231.jpg',
    'https://get.wallhere.com/photo/1920x1200-px-bridge-bridges-gate-golden-1783391.jpg', 
    'https://w-dog.ru/wallpapers/9/18/450538370098161/priroda-pejzazh-doroga-gory-nebo-oblaka-tuchi-zemlya-trava-zelen-voda-reka-ozero.jpg',
    'https://www.funnyart.club/uploads/posts/2022-12/1671240167_www-funnyart-club-p-krasivie-kartinki-nochnogo-goroda-krasivo-27.jpg'
]

def get_argparse():
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument( # Required parameter 'date'
        'urls',  
        help=DATE_HELP, 
        nargs='*'
        )
    parser.add_argument( # Optional parameter 'year'
            '-t',
            '--test', 
            type=str,
            default=URLS, 
            nargs='?',
            help=TEST_HELP
            )
    args = parser.parse_args()
    print(args)
    if args.urls:
        return args.urls
    elif args.test:
        return args.test
    else:
        msg = f'Input args is wrong {args}'
        print(parser.parse_args(['-h']))
        parser.error()
