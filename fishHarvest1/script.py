#!python3

# ---------------- Packages ---------------- #
import datetime
import os
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# ---------------- Parsing Config Variables ---------------- #


# ---------------- Classes ---------------- #
class Scraper(object):
    def __init__(self, browser):
        self.download_folder = '/Users/affoste/PycharmProjects/SalmonSpy/fishHarvest1/Downloads'

        # Create browser instance
        self.browser_type = browser
        self.create_browser()

    def create_browser(self):
        self.browser = webdriver.Chrome(executable_path="/Users/affoste/Downloads/chromedriver", chrome_options=chrome_profile())

    def scroll_down(self):
        try:
            scroll = 10.0
            while scroll > 0.1:
                self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight/%s);" % scroll)
                scroll -= .09
        except:
            self.wait(10)
            self.scroll_down()

    def delete_element(self, element):
        try:
            self.browser.execute_script('''
            var element = arguments[0];
            element.parentNode.removeChild(element);
            ''', element)
        except:
            pass

    def operate(self):
        # Open main page
        self.browser.get('http://www.adfg.alaska.gov/index.cfm?adfg=commercialbyareabristolbay.harvestsummary')
        self.wait(2)

        # Open iFrame content
        iframe = self.browser.find_element_by_id('maincontentarticle').find_element_by_tag_name('iframe').get_attribute('src')

        name = self.browser.title
        name = name[:name.find(',')]

        # Create needed folders
        os.chdir(self.download_folder)
        # name = self.browser.find_element_by_xpath('//font[@size="4"]').text.replace('-', '').strip()

        if not os.path.exists(os.path.join(self.download_folder, name)):
            os.mkdir(name)
            self.current_folder = os.path.join(self.download_folder, name)
            os.chdir(self.current_folder)
        else:
            self.current_folder = os.path.join(self.download_folder, name)
            os.chdir(self.current_folder)

        while True:
            folders = os.listdir()

            # Visit iFrame page
            self.browser.get(iframe)
            self.close_alert()

            self.wait(2)

            # Click on the dropdown
            self.browser.find_element_by_class_name('promptTextFieldReadOnly').click()

            self.wait(4)

            options = self.browser.find_element_by_class_name('DropDownValueList').find_elements_by_class_name('promptMenuOption')

            for option in options:
                date = option.get_attribute('title')
                date = datetime.datetime.strptime(date, '%m/%d/%Y')
                folder_name = datetime.datetime.strftime(date, '%d%b%Y').upper()
                if folder_name not in folders:
                    os.mkdir(folder_name)
                    self.current_folder = os.path.join(self.current_folder, folder_name)
                    option.click()
                    self.browser.find_element_by_id('gobtn').click()
                    self.wait(7)
                    for i in range(3):
                        self.download_file(i)
                        self.wait(3)
                        for file in os.listdir(self.download_folder):
                            if file.find('.csv') == -1:
                                continue
                            if os.path.isfile(os.path.join(self.download_folder, file)):
                                os.rename(os.path.join(self.download_folder, file), os.path.join(self.current_folder, folder_name + '_' + file))

                    self.current_folder = os.getcwd()
                    break
                else:
                    self.delete_element(option)
                    continue

    def download_file(self, index):
        self.browser.find_elements_by_xpath('//a[text()="Export"]')[index].click()
        self.wait(1)

        element = self.browser.find_elements_by_xpath('//a[@aria-label="Data"]')[index]
        hover = ActionChains(self.browser).move_to_element(element)
        hover.perform()

        self.wait(1)
        self.browser.find_elements_by_xpath('//a[@aria-label="CSV Format"]')[index].click()

        self.wait(2)
        self.browser.find_element_by_xpath('//a[@name="OK"]').click()

    def wait(self, t):
        time.sleep(t)

    def close_alert(self):
        try:
            alert = self.browser.switch_to_alert()
            alert.accept()
        except Exception as e:
            pass

# ---------------- Functions ---------------- #


def firefox_profile(download_folder):
    firefox_profile = webdriver.FirefoxProfile()

    firefox_profile.set_preference('browser.download.folderList', 2)  # custom location
    firefox_profile.set_preference('browser.download.manager.showWhenStarting', False)
    firefox_profile.set_preference('browser.download.dir', download_folder)
    firefox_profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/csv')

    return firefox_profile


def chrome_profile():
    chrome_options = webdriver.ChromeOptions()

    return chrome_options


def obj_dict(obj):
    return obj.__dict__


# ---------------- Start script ---------------- #
if __name__ == '__main__':
    scraper = Scraper('firefox')
    scraper.operate()
    scraper.browser.quit()
