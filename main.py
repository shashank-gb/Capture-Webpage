import eel
from selenium import webdriver
import httplib2
import os
import sys
import re
import random

eel.init('web')


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)


class wss:
    def browser_opening(self, flag):

        if flag == "True":
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--headless')
            print("browser is opened")
            self.driver = webdriver.Chrome(resource_path('./driver/chromedriver.exe'), options=chrome_options)
            return "Processing..."
        else:
            return "✖ Not Connected to Internet"

    def checking_url(self, url, flag):

        if flag == "True":

            print(url)

            h = httplib2.Http('.cache')

            try:
                response, content = h.request(url, 'HEAD')

                if response.status == 200:
                    res = obj.taking_screenshot(url)
                    return res
                elif response.status == 403:
                    return "403 Forbidden: You are not accessed to visit this website"

            except httplib2.ServerNotFoundError as e:
                return str(e)

            except httplib2.HttpLib2Error as e:
                return str(response.status), " ", str(e), " Enter Valid URL"

        else:
            return "✖ Not Connected to Internet"

    def taking_screenshot(self, url):

        self.driver.get(url)

        ele = self.driver.find_element_by_tag_name('body')
        real_height = ele.size['height']

        self.driver.set_window_size(1920, real_height)
        print("screenshot captured")

        img_name = re.findall('[\.](.*?)[\.]', url)
        if not img_name:
            img_name = str(random.randint(10 ** (5 - 1), (10 ** 5) - 1))
        else:
            img_name = img_name[0]

        self.driver.save_screenshot(os.path.join(os.path.expanduser("~/Desktop/"), img_name + ".png"))
        # self.driver.save_screenshot(os.path.join(os.path.expanduser("~/Desktop/img.png")))
        self.driver.close()
        return "Screenshot Saved Successfully in your Desktop.."


obj = wss()


@eel.expose
def open_browser(flag):
    res = obj.browser_opening(flag)
    return res


@eel.expose
def check_url(address, flag):
    res = obj.checking_url(address, flag)
    return res


@eel.expose
def screenshot(url):
    res = obj.taking_screenshot(url)
    return res


eel.start('index.html', size=(900, 350))
