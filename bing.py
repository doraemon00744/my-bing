# -*- coding: utf-8 -*-
import requests
import json
import win32api, win32gui, win32con
import os
from PIL import Image
import re
import getpass
import tkFileDialog
from random import choice

user = getpass.getuser()
if 'lihong' in user:
    wallpaper_dir = "E:\\hongpangzi\\bing"
else:
    wallpaper_dir = "D:\\MyDocuments\\" + user + "\\My Documents\My Pictures\\bing"


def get_wallpaper(index):
    bing_url = "http://cn.bing.com/HPImageArchive.aspx?format=js&idx=" + index + "&n=1"
    r = requests.get(url=bing_url)
    content = r.content.decode(encoding='utf-8')
    js = json.loads(content)
    wallpaper_addr = "http://cn.bing.com" + js['images'][0]['url']
    # wrapper_dir = "E:\\background\\bing"
    re_array = re.search(r".*/(.*)_ZH.*(\.\w*)", wallpaper_addr)
    image_name = re_array.group(1)
    image_type = re_array.group(2)
    image_path = wallpaper_dir + '\\' + image_name + image_type
    image_path_bmp = image_path.replace('.jpg', '.bmp')
    r = requests.get(wallpaper_addr)
    content = r.content
    # content_img = BytesIO(content)
    if not os.path.isdir(wallpaper_dir):
        os.makedirs(wallpaper_dir)
    if os.path.exists(image_path_bmp):
        return image_path_bmp
    else:
        with open(image_path, mode='wb', buffering=0) as f:
            f.write(content)
        img = Image.open(image_path)
        img.save(image_path_bmp, 'BMP')
        return image_path_bmp


def convert_jpg_to_bmp(jpg_path):
    img = Image.open(jpg_path)
    bmp_path = jpg_path.replace('.jpg', '.bmp')
    img.save(bmp_path, 'BMP')
    return bmp_path


def set_wallpaper(image_path):
    k = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, r"Control Panel\Desktop", 0, win32con.KEY_SET_VALUE)
    # 2拉伸适应桌面,0桌面居中
    win32api.RegSetValueEx(k, "WallpaperStyle", 0, win32con.REG_SZ, "2")
    win32api.RegSetValueEx(k, "TileWallpaper", 0, win32con.REG_SZ, "0")
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, image_path, 1 + 2)


def change_wallpaper_from_bing():
    date_list = list(range(-1, 19))
    date = choice(date_list)
    wallpaper_addr = get_wallpaper(str(date))
    set_wallpaper(wallpaper_addr)


file_opt = options = {}
options['defaultextension'] = '.bmp'
options['filetypes'] = [('image files', '.bmp'), ('img files','.jpg')]
options['initialdir'] = wallpaper_dir
# options['initialfile'] = 'myfile.txt'
options['title'] = 'please select a image!'


def select_file_from_local():
    __img_path = tkFileDialog.askopenfilename(**file_opt)
    if '' == __img_path:
        return
    if 'jpg' in __img_path or 'JPG' in __img_path:
        __img_path = convert_jpg_to_bmp(__img_path)
    set_wallpaper(image_path=__img_path)


if __name__ == "__main__":
    img_path = get_wallpaper('0')
    set_wallpaper(image_path=img_path)
