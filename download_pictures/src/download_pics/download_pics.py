import threading
from  multiprocessing import Process
import asyncio
import requests
import time
import aiohttp
import aiofiles




urls = [
    'https://hotwalls.ru/wallpapers/2560x1600/zamok_na_holme.jpg', 
    'https://get.wallhere.com/photo/lake-mountain-tree-water-landscape-1076231.jpg',
    'https://get.wallhere.com/photo/1920x1200-px-bridge-bridges-gate-golden-1783391.jpg', 
    'https://w-dog.ru/wallpapers/9/18/450538370098161/priroda-pejzazh-doroga-gory-nebo-oblaka-tuchi-zemlya-trava-zelen-voda-reka-ozero.jpg',
    'https://www.funnyart.club/uploads/posts/2022-12/1671240167_www-funnyart-club-p-krasivie-kartinki-nochnogo-goroda-krasivo-27.jpg'
]


def download_pic(url, filesufix):
    '''Download file'''
    start_time = time.time()
    response = requests.get(url)
    filesufix = filesufix.split('_')[0]
    if response.status_code == 200:
        filename = f'./{filesufix}/{filesufix}_{url.split('/')[-1]}'
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f'Download {url} in {time.time() - start_time:.2f} seconds')
    else:
        print('Wrong url address')


def sync_download(urls=urls):
    '''Download files use usual sync way'''
    for url in urls:
        download_pic(url, sync_download.__name__)


def threading_download(urls=urls):
    '''Download files using threading way'''
    threads = []  
    for url in urls:
        thread = threading.Thread(target=download_pic, args=[url, threading_download.__name__])
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()


def multiprocess_download(urls=urls):
    '''Download files using threading way'''
    processes = []
    for url in urls:
        process = Process(target=download_pic, args=(url, multiprocess_download.__name__))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()



async def async_downloads(urls=urls):
    '''Download files using asyncio way'''
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(async_download(url, async_downloads.__name__))
        tasks.append(task)
    await asyncio.gather(*tasks)

async def async_download(url, filesufix):
    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                filename = f'./{filesufix.split('_')[0]}/{filesufix}_{url.split('/')[-1]}'
                async with aiofiles.open(filename, mode='wb') as f:
                    await f.write(await response.read())
                
        print(f'Download {url} in {time.time() - start_time:.2f} seconds')

def async_loop(urls=urls):
    start_time = time.time()
    loop = asyncio.new_event_loop()
    loop.run_until_complete(async_downloads(urls))
    return time.time() - start_time                  

def main(urls=urls):
    start_time = time.time()
    sync_download(urls)
    sync_time = time.time() - start_time
    start_time = time.time()
    threading_download(urls)
    threading_time = time.time() - start_time
    start_time = time.time()
    multiprocess_download(urls)
    multiprocess_time = time.time() - start_time
    async_time = async_loop(urls)
    print(
        f'Complete time downloads are:\n' 
        f'sync time: {sync_time:.2f}, \n'
        f'threading time: {threading_time:.2f}, \n'
        f'multiprocess time: {multiprocess_time:.2f}, \n'
        f'asyncio time: {async_time:.2f}'
          )
    
if __name__ == '__main__':
    main()