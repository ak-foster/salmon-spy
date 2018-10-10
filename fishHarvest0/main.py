from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import os
import glob
import csv

"""
Runs automated browser (not headless).

Fetches data for salmon harvest daily summary (summary only) and saves .csv file to /csv/ directory.

Uses list_of_dates.csv file to save dates for the daily summary csv exports saved.

Will download data if day is found on the website, but not in list_of_dates.csv, making it possible to re-trigger
a download by removing a date from list_of_dates.csv.

"""

dates = []
with open('list_of_dates.csv', newline='') as csvfile:
    file_content = csv.reader(csvfile)
    for date in file_content:
        dates.append(date[0])

folder_exec = os.path.dirname(os.path.realpath(__file__))
chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory": folder_exec + "/csv/", "download.prompt_for_download": False, }
chromeOptions.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chrome_options=chromeOptions, executable_path="/Users/affoste/Downloads/chromedriver")
driver.get("http://www.adfg.alaska.gov/index.cfm?adfg=commercialbyareabristolbay.harvestsummary")


def pushsend(bywhat, what, conte=0, subm=0):
    if bywhat == "id":
        element = driver.find_element_by_id(what)
    elif bywhat == "name":
        element = driver.find_element_by_name(what)
    elif bywhat == "xpath":
        # print(what)
        while True:
            try:
                element = driver.find_element_by_xpath(what)
                break
            except NoSuchElementException:
                pass

    if conte != 0:
        element.send_keys(conte)
    if subm == 1:
        element.send_keys(Keys.RETURN)
    elif subm == 2:
        element.click()


def export_csv(s):
    time.sleep(2)
    pushsend("xpath", "//div[@class='masterCustomChoiceList promptChoiceListBox']/img", 0, 2)
    time.sleep(4)
    dates2 = driver.find_elements_by_xpath("//span[@class='promptMenuOptionText']")
    msd = dates2[s].text

    dates2[s].click()

    pushsend("xpath", "//input[@id='gobtn']", 0, 2)
    time.sleep(5)
    pushsend("xpath", "//a[@name='ReportLinkMenu']", 0, 2)
    pushsend("xpath", "//a[@aria-label='Data']", 0, 2)
    pushsend("xpath", "//a[@aria-label='CSV Format']", 0, 2)
    time.sleep(2)
    pushsend("xpath", "//a[text()='OK']", 0, 2)

    files = glob.glob(r'csv/Run*.csv')
    file_name = "csv/Summary " + msd.replace("/", "-") + ".csv"
    try:
        os.rename(files[0], file_name)
    except:
        print(f"File {file_name} already exist!")
        os.remove(files[0])

    with open('list_of_dates.csv', 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['Date'])
        writer.writerow({"Date": msd[6:] + msd[0:2] + msd[3:5]})


iframe_src = driver.find_element_by_xpath("//*[@id='maincontentarticle']/div[1]/iframe").get_attribute("src")
driver.get(iframe_src)

pushsend("xpath", "//div[@class='masterCustomChoiceList promptChoiceListBox']/img", 0, 2)
time.sleep(2)
dates2 = driver.find_elements_by_xpath("//span[@class='promptMenuOptionText']")
all_dates = []
for x in dates2:
    all_dates.append(x.text[6:] + x.text[0:2] + x.text[3:5])
pushsend("xpath", "//div[@class='masterCustomChoiceList promptChoiceListBox']/img", 0, 2)

for i, gt in enumerate(all_dates):

    if gt not in dates:
        export_csv(i)
