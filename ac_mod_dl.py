#!/usr/bin/python
import wget
import os
from urllib.error import HTTPError

BASE_URL = 'https://www.haoyufang.site:8892/download/public/ACmod/'
CAR_URL = BASE_URL + 'cars/'
TRACK_URL = BASE_URL + 'tracks/'

def download(url: str) -> None:
    try:
        if os.path.exists(os.path.basename(url)):
            return
        wget.download(url)
    except HTTPError:
        return

def download_tracks() -> None:
    with open('tracks.txt','r') as tracks_fp:
        for line in tracks_fp:
            track_filename = tracks_fp.readline().strip()
            if track_filename:
                print(track_filename)
                download(TRACK_URL + track_filename)
                print()

def download_cars() -> None:
    with open('cars.txt','r') as cars_fp:
        for line in cars_fp:
            car_filename = cars_fp.readline().strip()
            if car_filename:
                print(car_filename)
                download(CAR_URL + car_filename)
                print()

def main() -> None:
    download_tracks()
    download_cars()

if __name__ == '__main__':
    main()
