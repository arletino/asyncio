from src.argparse_set import argparse_set
from src.download_pics import download_pics

def main():
    urls = argparse_set.get_argparse()
    download_pics.main(urls)


if __name__ == '__main__':
    main()