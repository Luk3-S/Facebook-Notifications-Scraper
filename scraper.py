import scrapy
import getpass
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.chrome.options import Options

class FacebookSpider(scrapy.Spider):

    name = 'facebookspider'
    url = ""

    # def start_requests(self):
    #     self.url = 'https://www.facebook.com/notifications'
    #     yield scrapy.Request(self.url,self.parse)

    def parse(self,response):
        for notif in response.css('div._33c jewelItemNew'):
            print("found notif")

    
    def get_details(self):
        url = 'https://www.facebook.com/notifications'

        options = Options()
        options.add_argument("--disable-notifications")
        #options.add_argument("--headless")
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

        yield scrapy.Request(url,self.parse)

        input("enter anything to quit")
        driver.quit()
        print("done")

        
    

a = FacebookSpider()
a.get_details()
