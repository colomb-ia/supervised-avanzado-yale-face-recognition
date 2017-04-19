import os, sys, urllib, stat
import zipfile, time
from selenium import webdriver

#check OS version: 'linux2' ,'win32' or 'darwin'(MAC)
version = sys.platform
if version == 'linux2':
    if sys.maxsize > 2**32: #it is then 64 bits
        webdriver_url = 'https://chromedriver.storage.googleapis.com/2.29/chromedriver_linux64.zip'
    else:
        webdriver_url = 'https://chromedriver.storage.googleapis.com/2.29/chromedriver_linux32.zip'
elif version == 'win32':
    webdriver_url = 'https://chromedriver.storage.googleapis.com/2.29/chromedriver_win32.zip'
elif version == 'darwin':
    webdriver_url = 'https://chromedriver.storage.googleapis.com/2.29/chromedriver_mac64.zip'
else:
    raise ValueError("No supported OS")

#Download now driver
chromedrive = urllib.URLopener()
chromedrive.retrieve(webdriver_url, "chromedriver.zip")

#Extract it, chmod to +x and delete zip
zip_ref = zipfile.ZipFile("chromedriver.zip", 'r')
zip_ref.extractall()
st = os.stat('chromedriver')
os.chmod("chromedriver", st.st_mode | stat.S_IEXEC | stat.S_IXGRP | stat.S_IXOTH)
zip_ref.close()
os.remove("chromedriver.zip")

#Configure selenium
chromedriver =  os.getcwd()+'/chromedriver'
os.environ["webdriver.chrome.driver"] = chromedriver

chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : os.getcwd()}
chromeOptions.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=chromeOptions)

#Donwload
TRAINING_SET_URL = "http://cbcl.mit.edu/software-datasets/heisele/download/download.html"
driver.get(TRAINING_SET_URL)
driver.find_element_by_link_text("download now").click();

#Wait to download to complete

file_path = os.getcwd() + "/MIT-CBCL-facerec-database.zip"
while not os.path.exists(file_path):
    time.sleep(1)

if os.path.isfile(file_path):
    print "Done!!"
    os.remove("chromedriver")
    driver.quit()
else:
    raise ValueError("%s isn't a file!" % file_path)
