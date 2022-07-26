import requests
from makefolders import *
from urls import * 

pathurldict = {
    all_album_paths[0] : a1_urls, # /Users/matthewkang/Code/Gradpics_API/PHOTOS/101 -> (str) : [list of 524 urls] -> (list) of strings
    all_album_paths[1] : a2_urls,
    all_album_paths[2] : b1_urls,
    all_album_paths[3] : b2_urls,
    all_album_paths[4] : c1_urls,
    all_album_paths[5] : c2_urls,
    all_album_paths[6] : d1_urls,
    all_album_paths[7] : d2_urls
}

def downloader(url,path):
    img_data = requests.get(url).content
    name = url.split('/')[-1][:4]

    if os.path.exists(path):
        with open(path+f'/{name}.jpg', 'wb') as handler:
            handler.write(img_data)



if __name__ == "__main__":
    print('DOWNLOADING PHOTOS...')
    for path in pathurldict:
        for urls in pathurldict[path]:
            downloader(urls,path)

