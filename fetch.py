#! python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

url = "http://www.oceanak.adfg.alaska.gov/analytics/saw.dll?PortalPages&PortalPath=%2Fshared%2FCommercial%20Fisheries%2FPublic%20Web%2FRegion%20II%2FSalmon%2FDaily%20Run%20Summary%20Public&NQUser=public_bi_user&NQPassword=No12rules&options=fdr"

# Setting up webdriver
browser = webdriver.Chrome(executable_path="/Users/affoste/Downloads/chromedriver")

# Create new instance of Chrome
browser.get(url)

# Wait for page to load
timeout = 2
WebDriverWait(browser,timeout)

def select_date():
    date_dropdown = browser.find_element_by_class_name('promptTextField promptTextFieldReadOnly')
    date_options = browser.find_element_by_class_name("masterMenuItem promptMenuOption")
    print(len(date_dropdown))
    print(len(date_options))

def submit_click():
    apply_button = browser.find_elements_by_name('gobtn')
    apply_button.click()

select_date()

try:
    export_links = browser.find_elements_by_name('ReportLinkMenu')
    print(len(export_links))
    export_links[0].click()

except:
    print("Not found!")
# browser.close()
