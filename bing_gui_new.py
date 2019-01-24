import datetime
import getpass
import os
import tkinter as tk
import win32api
import win32gui
from tkinter import *
from tkinter import ttk

import win32con

from bing_new import Bing

root = Tk()
root.title("壁纸宝")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe['borderwidth'] = 2
mainframe['relief'] = 'solid'
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

main_label = ttk.Label(mainframe, text="")
main_label.grid(column=1, row=1, columnspan=2, sticky=N)

ttk.Label(mainframe, text="请选择日期", ).grid(column=1, row=2, sticky=(W, E))


def generate_date_list():
    """create the date list for option menu"""
    d_list = [datetime.datetime.now() + datetime.timedelta(days=d) for d in
              range(-7, -1)]  # generate date list except for today, yesterday and tomorrow
    d_list = [str(d.month) + "月" + str(d.day) + "日" for d in d_list] + ["昨天", "今天", "明天"]
    return [''] + d_list


def generate_date_map():
    """create the date dict from option menu list"""
    d_list = [datetime.datetime.now() + datetime.timedelta(days=d) for d in range(-7, 2)]
    return {str(d.month) + "月" + str(d.day) + "日": (datetime.datetime.now() - d).days for d in d_list}


def generate_date_map_new():
    """create the date dict from option menu list"""
    date_list = generate_date_list()
    date_value_list = list(range(8, -2, -1))
    return dict(zip(date_list, date_value_list))


option_menu_values = generate_date_list()
option_menu_values_map = generate_date_map_new()

option_menu_value = tk.StringVar()
# option_menu_value.set(option_menu_values[1])
option_menu_value.set("今天")
option_menu = ttk.OptionMenu(mainframe, option_menu_value, *option_menu_values)


# def refresh_date_list():
#     global option_menu_values
#     global option_menu_values_map
#     global option_menu
#     if not option_menu_values[1] == str((datetime.datetime.now() - datetime.timedelta(days=7)).month) + "月" + str(
#             (datetime.datetime.now() - datetime.timedelta(days=7)).day) + "日":
#         option_menu_values = generate_date_list()
#         option_menu_values_map = generate_date_map_new()
#         option_menu = ttk.OptionMenu(mainframe, option_menu_value, *option_menu_values)


option_menu.grid(column=2, row=2, sticky=(W, E))
# option_menu.bind('<1>', lambda e: refresh_date_list())

status_value = tk.StringVar()
status_value.set("^.^")
ttk.Label(mainframe, textvariable=status_value, justify="right").grid(column=1, row=8, columnspan=2, sticky=(W, E))


def set_wallpaper(image_path):
    k = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, r"Control Panel\Desktop", 0, win32con.KEY_SET_VALUE)
    # 2拉伸适应桌面,0桌面居中
    win32api.RegSetValueEx(k, "WallpaperStyle", 0, win32con.REG_SZ, "2")
    win32api.RegSetValueEx(k, "TileWallpaper", 0, win32con.REG_SZ, "0")
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, image_path, 1 + 2)


user = getpass.getuser()
wallpaper_dir = "D:\\MyDocuments\\" + user + "\\My Documents\My Pictures\\bing//"


def change_wallpaper(_wallpaper_dir, _option_menu_value):
    """when clicking button, get the context and change wallpaper"""
    if not os.path.isdir(_wallpaper_dir):
        os.makedirs(_wallpaper_dir)
    bing = Bing(bing_url_parameter_idx=option_menu_values_map[_option_menu_value.get()], local_disk=_wallpaper_dir)
    bing.get_wallpaper_data()
    status_value.set(bing.wallpaper_image_list[0].copyright)
    bing.download_wallpaper_to_local_disk()
    set_wallpaper(bing.wallpaper_image_list[0].image_file_name_bmp)


submit_btn = ttk.Button(mainframe, text="点我", command=lambda: change_wallpaper(wallpaper_dir, option_menu_value))
submit_btn.grid(column=1, row=7, columnspan=2, sticky=(W, E))
# submit_btn.bind('<1>', lambda e: threading.Thread(target=progress, name='progress_bar_th').start())


for child in mainframe.winfo_children():
    child.grid_configure(padx=10, pady=10)
    child.columnconfigure(0, weight=1, minsize=10)

root.mainloop()

if __name__ == "__main__":
    pass
    # def generate_date_list():
    #     d_list = [datetime.datetime.now() + datetime.timedelta(days=d) for d in range(-7, 2)]
    #     d_list = [str(d.month) + "月" + str(d.day) + "日" for d in d_list]
    #     return [''] + d_list
    #
    #
    # def generate_date_map(d_list):
    #     return {str(d): i for d in d_list for i in range(8)}
    # t = time.time()
    # print(datetime.datetime.now() + datetime.timedelta(days=10))
    # d_list = [datetime.datetime.now() + datetime.timedelta(days=d) for d in range(-7, 2)]
    # print(d_list)
    # print({str(d.month) + "月" + str(d.day) + "日": (datetime.datetime.now() - d).days for d in d_list})
    # d_list = [str(d.month) + "月" + str(d.day) + "日" for d in d_list]
    # print(d_list)
