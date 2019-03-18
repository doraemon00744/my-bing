import requests
from PIL import Image


class Bing:
    JPG_FILE_EXTENSION = "jpg"
    BMP_FILE_EXTENSION = "bmp"

    def __init__(self, bing_url_base="http://bing.com",
                 bing_url_method="/HPImageArchive.aspx",
                 bing_url_parameter_idx=0,
                 bing_url_parameter_n=1,
                 local_disk="E://"):
        self.bing_url_base = bing_url_base
        self.bing_url_method = bing_url_method
        self.bing_url = self.bing_url_base + self.bing_url_method
        self.bing_url_parameter = {
            "format=": "js",
            "idx=": bing_url_parameter_idx,  # control the date
            "n=": bing_url_parameter_n  # control the number of wallpaper
        }
        self.bing_json = {}  # bing return json
        self.wallpaper_image_list = []  # Image object list
        self.local_disk = local_disk

    def get_wallpaper_data(self):
        """get the Image object list from given argument"""
        url = self.bing_url + "?" + "&".join(
            [item[0] + str(item[1]) for item in self.bing_url_parameter.items()])
        print(url)
        self.bing_json = requests.get(url=url).json()
        self.wallpaper_image_list = [
            BingImage(urlbase=image["urlbase"], url=image["url"], image_copyright=image["copyright"],
                      image_startdate=image["startdate"], image_enddate=image["enddate"]) for image in
            self.bing_json['images']]

    def download_wallpaper_to_local_disk(self):
        """download wallpapers to local disk, both jpg and bmp version"""
        for image in self.wallpaper_image_list:
            print(image)
            print(self.bing_url_base + image.url)
            r = requests.get(url=self.bing_url_base + image.url)
            wallpaper_image_file_name = self.local_disk + str(
                image.urlbase.split("=")[-1:][0]) + "." + Bing.JPG_FILE_EXTENSION
            with open(wallpaper_image_file_name, mode='wb')as f:
                f.write(r.content)  # save the original jpg version
            image.image_file_name_bmp = wallpaper_image_file_name.replace(Bing.JPG_FILE_EXTENSION,
                                                                          Bing.BMP_FILE_EXTENSION)
            try:
                Image.open(wallpaper_image_file_name).save(
                    wallpaper_image_file_name.replace(Bing.JPG_FILE_EXTENSION, Bing.BMP_FILE_EXTENSION),
                    Bing.BMP_FILE_EXTENSION)  # convert jpg to bmp and save it
            except Exception as e:
                print("Error:", e)
                continue

class BingImage:

    def __init__(self, urlbase, url, image_copyright, image_startdate, image_enddate):
        self.urlbase = urlbase
        self.url = url
        self.copyright = image_copyright
        self.startdate = image_startdate
        self.enddate = image_enddate
        self.image_file_name_bmp = ""


if __name__ == "__main__":
    # temp = {
    #     "name=": "haha",
    #     "age=": 1
    # }
    #
    # # print("&".join([item[0] + str(item[1]) for item in temp.items()]))
    bing = Bing(bing_url_parameter_n=1)
    bing.get_wallpaper_data()
    bing.download_wallpaper_to_local_disk()

    # bing = Bing()
    # print(bing.__dict__.keys())
    # print(bing.__class__.__bases__)
    # # bing.haha = "hehe"
    # def print_haha(obj):
    #     return obj.bing_url_method
    # Bing.haha = print_haha
    # print(bing.__dict__.keys())
    # print(bing.haha())
