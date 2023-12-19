# -*- coding: utf-8 -*-
"""
@Author: hejie
@Date: 2023-12-19 15:34:58
@LastEditTime: 2023-12-19 21:19:43
@LastEditors: hejie
@Description: 
"""
import os
import time
from concurrent.futures import ThreadPoolExecutor, Future
import subprocess

class Downloader:

    def __init__(self, out_folder: str, workers: int = None):
        self._out_folder = out_folder
        if not os.path.isdir(out_folder):
            os.makedirs(out_folder)
        self._pool = ThreadPoolExecutor(max_workers=workers or 4)

    def run(self, url: str, file_name: str = 'outfile') -> Future:
        return self._pool.submit(self._run, url, file_name)
    
    def _run(self, m3u8_url: str, file_name: str):
        print(m3u8_url)
        f = os.path.join(self._out_folder, file_name)
        command = ['ffmpeg', '-i', m3u8_url, '-c', 'copy', file_name]
        try:
            subprocess.check_call(command)
        except subprocess.CalledProcessError as e:
            print("failed to download {}".format(m3u8_url))

    def shutdown(self, wait: bool = True):
        return self._pool.shutdown(wait)