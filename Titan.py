import urllib.request
import json
import os
import requests
import datetime
import ctypes


class Titan:
    def __init__(self):
        # Image URL
        self.url = "http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1"
        self.dynamic_json = json.loads(requests.get(self.url).text)
        self.image_url = "http://www.bing.com" + self.dynamic_json["images"][0]["url"]

        # Paths and naming variables
        self.main_path = str(r"C:\Titan\Downloads")
        self.file_name = datetime.datetime.date(datetime.datetime.now())
        self.full_file_name = "Wallpaper" + str(self.file_name) + str(".jpg")
        self.full_image_path = os.path.join(self.main_path, self.full_file_name)

    try:

        def create_project_dir(self):
            if not os.path.exists(self.main_path):
                os.makedirs(self.main_path)
                os.chmod(self.main_path, 0o666)  # read/write by everyone

        def download_image(self):
            str(urllib.request.urlretrieve(self.image_url, self.full_image_path))

        def set_as_wallpaper(self):
            spi_setdeskwallpaper = 20
            ctypes.windll.user32.SystemParametersInfoW(spi_setdeskwallpaper, 0, self.full_image_path, 3)
    except requests.exceptions.ConnectionError:
        print("Please connect to internet and try again.")


titan = Titan()
titan.create_project_dir()
titan.download_image()
titan.set_as_wallpaper()
