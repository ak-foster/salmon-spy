#! python3
import inspect
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException
import sys

import logging
from requests import Session
from requests.auth import HTTPBasicAuth
from zeep import Client, Settings, xsd
from zeep.transports import Transport
from zeep.wsse.username import UsernameToken


username = 'public_bi_user'
password = 'No12rules'
logging.basicConfig(
    filename="my.log",
    level=logging.WARNING,
    format="\n%(asctime)s:%(levelname)s:%(message)s"
)

session = Session()
session.auth = HTTPBasicAuth(username, password)
transport_with_basic_auth = Transport(session=session)
wsse = UsernameToken(username, password)
settings = Settings(strict=False, xml_huge_tree=True)

client = Client(wsdl='http://www.oceanak.adfg.alaska.gov/analytics/saw.dll/wsdl/v12', wsse=wsse, settings=settings, transport=transport_with_basic_auth)
# client.wsdl.dump()
#service-m = client.bind('sawsoap:MetadataService', '')

#sessionid = service.logon(name='public_bi_user', password='No12rules')

sa_list = client.service.MetadataService.getSubjectAreas()
print(sa_list)

for sa in sa_list:
    print('\t%s'%sa.name)
    sa_contents=client.service['MetadataService'].describeSubjectArea(sa.name,'IncludeTablesAndColumns',sessionid)

for table in sa_contents.tables:
    print('\t\t%s' % table.name)
    for col in table.columns:
        print('\t\t\t%s' % col.name)

"""
url = "http://www.oceanak.adfg.alaska.gov/analytics/saw.dll?PortalPages&PortalPath=%2Fshared%2FCommercial%20Fisheries%2FPublic%20Web%2FRegion%20II%2FSalmon%2FDaily%20Run%20Summary%20Public&NQUser=public_bi_user&NQPassword=No12rules&options=fdr"

# Setting up webdriver
opts = Options()
opts.add_argument('--headless')
opts.add_argument('--disable-gpu')
browser = webdriver.Chrome( chrome_options=opts, executable_path="/Users/affoste/Downloads/chromedriver")

# Create new instance of Chrome
browser.get(url)

# Wait for page to load
EC.title_is('Oracle BI Interactive Dashboards - Daily Run Summary Public')

timeout = 2

def select_date():
    date_dropdown = browser.find_element_by_class_name('promptDropDownButton')
    print("dropdown found...")
    print(type(date_dropdown))
    date_dropdown.click()
    print("dropdown clicked")
    date_options = browser.find_elements_by_class_name("promptMenuOptionText")
    print(f"found something with {len(date_options)} options...")
    wait = WebDriverWait(browser, 2)
    wait.until(EC.visibility_of_any_elements_located((By.CLASS_NAME, "masterMenuItem")))
    print("I waited 2 seconds or the element was visible")
    date_menu = browser.find_elements_by_class_name('masterMenuItem')
    print(f"found menu with {len(date_menu)} dates")
    date_menu[2].click()
    print("menu clicked")

def submit_click():
    apply_button = browser.find_elements_by_name('gobtn')
    apply_button.click()

try:
    select_date()
    #
    export_links = browser.find_elements_by_name('ReportLinkMenu')
    print(len(export_links))
    export_links[0].click()
    #

except:  # catching all exceptions
    e = sys.exc_info()[0]
    logging.error(f"Caught Error: {e}")
    print(f"Error:  {e}")

finally:
    browser.close()
"""