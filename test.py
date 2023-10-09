import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

PATH = "C:\Drivers\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.amazon.in/product-reviews/8119352947/ref=cm_cr_arp_d_paging_btm_next_2/261-5976745-5421030?pageNumber=1")
driver.maximize_window()
