# -*- coding: utf-8 -*-

import getpass
import os
import win32api
import win32gui

import win32con
import wx
from PIL import Image

import bing_gui_wxform
from bing_new import Bing
from left_arrow_img import left_arrow as left_arrow_img
from right_arrow_img import right_arrow as right_arrow_img

user = getpass.getuser()
wallpaper_dir = "D:\\MyDocuments\\" + user + "\\My Documents\My Pictures\\bing//"


def change_wallpaper_from_file_path(file_path):
    k = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, r"Control Panel\Desktop", 0, win32con.KEY_SET_VALUE)
    # 2拉伸适应桌面,0桌面居中
    win32api.RegSetValueEx(k, "WallpaperStyle", 0, win32con.REG_SZ, "2")
    win32api.RegSetValueEx(k, "TileWallpaper", 0, win32con.REG_SZ, "0")
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, file_path,
                                  1 + 2)


class BingWxConcrete(bing_gui_wxform.BingWx):

    def __init__(self, parent=None):
        bing_gui_wxform.BingWx.__init__(self, parent)  # use class.__init__()

        # set the two buttons with images
        self.left_bpButton.SetBitmap(left_arrow_img.getImage().Scale(40, 40).ConvertToBitmap())
        self.right_bpButton.SetBitmap(right_arrow_img.getImage().Scale(40, 40).ConvertToBitmap())

        # init background
        self.bing = Bing(bing_url_parameter_n=8, bing_url_parameter_idx=-1, local_disk=wallpaper_dir)
        self.img_local_addr_list = []  # the local addresses of images
        self.init_background()
        # current image index
        self.img_current_idx = 0
        self.show_wallpaper()

    def __del__(self):
        pass

    def open_from_local(self, event):
        file_wildcard = "bmp files(*.bmp)|*.bmp|jpg files(*.jpg)|*.jpg"
        file_dialog = wx.FileDialog(self, "open", defaultDir=wallpaper_dir, wildcard=file_wildcard)
        if file_dialog.ShowModal() == wx.ID_OK:

            file_name = file_dialog.GetPath()
            if str(file_name).endswith('jpg'):
                file_name = file_name.replace(Bing.JPG_FILE_EXTENSION, Bing.BMP_FILE_EXTENSION)
                Image.open(file_name).save(
                    file_name,
                    Bing.BMP_FILE_EXTENSION)
            change_wallpaper_from_file_path(file_name)
        file_dialog.Destroy()

    def reload(self, event):
        self.bing = Bing(bing_url_parameter_n=8, bing_url_parameter_idx=-1, local_disk=wallpaper_dir)
        self.img_local_addr_list = []  # the local addresses of images
        self.init_background()
        # current image index
        self.img_current_idx = 0
        self.show_wallpaper()

    def exit(self, event):
        wx.Exit()

    def about_message(self, event):
        msg_dialog = wx.MessageDialog(self, user + " 欢迎光临，请站稳", "关于", wx.YES_NO)
        msg_dialog.ShowModal()

    def show_wallpaper(self):
        wall_paper_img = wx.Image(self.img_local_addr_list[self.img_current_idx],
                                  wx.BITMAP_TYPE_ANY)
        try:
            wall_paper_img = wall_paper_img.Scale(640, 360)
            self.img_bitmap.SetBitmap(wall_paper_img.ConvertToBitmap())
        except:
            pass
        img_enddate = self.bing.wallpaper_image_list[
            self.img_current_idx].enddate
        img_enddate = img_enddate[0:4] + "年" + img_enddate[4:6] + "月" + img_enddate[6:] + "日"
        self.description_staticText.SetLabel(
            self.bing.wallpaper_image_list[self.img_current_idx].copyright + "，" + img_enddate)

    def init_background(self):
        if not os.path.isdir(wallpaper_dir):
            os.makedirs(wallpaper_dir)
        self.bing.get_wallpaper_data()
        self.bing.download_wallpaper_to_local_disk()
        img_list = self.bing.wallpaper_image_list
        self.img_local_addr_list = [img.image_file_name_bmp for img in img_list]
        print(self.img_local_addr_list)

    def previous_wallpaper(self, event):
        self.img_current_idx -= 1
        if self.img_current_idx < 0:
            self.img_current_idx = 7
        print("this is previous button clicked!!")
        print(self.img_current_idx)
        self.show_wallpaper()

    def next_wallpaper(self, event):
        self.img_current_idx += 1
        if self.img_current_idx > 7:
            self.img_current_idx = 0
        print("this is next button clicked!!")
        print(self.img_current_idx)
        self.show_wallpaper()

    def change_wallpaper(self, event):
        print("this is change_wallpaper button clicked!!")
        change_wallpaper_from_file_path(self.img_local_addr_list[self.img_current_idx])


# if __name__ == "__main__":
app = wx.App()
bing_concrete = BingWxConcrete()
bing_concrete.Show()
app.MainLoop()
# 打exe包脚本
# pyinstaller -F -w bing_gui_wx.py -i bing128.ico
