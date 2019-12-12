import scrapy
import getpass
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.chrome.options import Options







class FacebookSpider(scrapy.Spider):

    name = 'facebookspider'



    
    def get_details(self,url):

        options = Options()
        options.add_argument("--disable-notifications")
        user = input("Enter email:")
        pword = getpass.getpass("Enter password:")
        driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)
        driver.get(url)
        print("facebook opened")

        sleep(1)

        u_box = driver.find_element_by_id('email')
        u_box.send_keys(user)
        print("email entered")
        sleep(1)

        p_box = driver.find_element_by_id('pass')
        p_box.send_keys(pword)
        print("password entered")

        login = driver.find_element_by_id('loginbutton')
        login.click()



        
        # alert = driver.switch_to_alert()
        # alert.reject()
        # print("alert rejected")

        input("enter anything to quit")
        driver.quit()
        print("done")
        
    

a = FacebookSpider()
url = 'https://www.facebook.com/notifications'

a.get_details(url)