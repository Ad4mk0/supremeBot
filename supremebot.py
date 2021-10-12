from selenium import webdriver # For automating data input
from selenium.webdriver.chrome.options import Options # For providing custom configurations for Chrome to run

import schedule
import time

from time import sleep


mobile_emulation = {
    "deviceMetrics": { "width": 375, "height": 812, "pixelRatio": 3.0 },
    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"
}

chrome_options = Options()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
#ZAFAKEUJE IPHONE


class SupremeBot:
    
    def __init__(self, fullname, email, fon, address, city, zip, cnumber, cvv, month, year, country, size, quantity, colour):

        #self.driver = webdriver.Chrome()
        self.driver = webdriver.Chrome(r"C:\Users\ADAM\Downloads\chromedriver_win32\chromedriver.exe", options=chrome_options)   
        self.driver.get("https://www.supremenewyork.com/mobile/")
        
        
        sleep(1)
        
        self.driver.find_element_by_id('accessories-category').click()
        #STACI VEDIET NAZVY KATEGORII
        #jackets-category
        #shirts-category
        #tops/sweaters-category
        #sweatshirts-category
        #pants-category
        #shorts-category
        #t-shirts-category
        #hats-category
        #bags-category
        #accessories-category
        #skate-category
        #shoes-category ?
        #tieto categories -> poloziek -> produkt -> layer1.button -> layer1.button (categories)
        #//*[@id="Layer_1"] - back button id
        
        sleep(1)

        self.driver.find_element_by_xpath("//span[contains(.,'Supreme®/Hanes® Tagless Tees (3 Pack)')]").click()  #TU TREBA VEDIET NAZOV PRODUKTU V KATEGORII
        
        sleep(1)

        i = 1
        while self.driver.find_element_by_id('style-name').text != colour:
            path = "//ul[@class='style-selector']/li["+str(i)+"]"
            self.driver.find_element_by_xpath(path).click()
            # num = 31617 + i
            # self.driver.find_elements_by_id("style-"+str(num)).click()
            i+=1

        
        #sleep(1)
        self.driver.find_element_by_xpath('//*[@id="size-options"]').send_keys(size)
        #sleep(1)
        self.driver.find_element_by_xpath('//*[@id="qty-options"]').send_keys(quantity)
        #sleep(1)

        
        self.driver.find_element_by_xpath("//*[@id='cart-update']/span").click() #prida do kosa
        
        sleep(1)
        
        self.driver.find_element_by_xpath("//*[@id='checkout-now']/span").click() #prejde do kosa

        sleep(1)
        
        
        #SEKVENCIA UDAJOV NA DELIVERY
        self.driver.find_element_by_xpath('//*[@id="order_billing_name"]').send_keys(fullname) 
        self.driver.find_element_by_xpath('//*[@id="order_email"]').send_keys(email)
        self.driver.find_element_by_xpath('//*[@id="order_tel"]').send_keys(fon)
        self.driver.find_element_by_xpath('//*[@id="order_billing_address"]').send_keys(address)
        self.driver.find_element_by_xpath('//*[@id="order_billing_city"]').send_keys(city)
        self.driver.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys(zip)
        self.driver.find_element_by_xpath('//*[@id="order_billing_country"]').send_keys(country)
        self.driver.find_element_by_xpath('//*[@id="remember_address"]').click()

        self.driver.find_element_by_xpath('//*[@id="credit_card_n"]').send_keys(cnumber)
        self.driver.find_element_by_xpath('//*[@id="credit_card_month"]').send_keys(month)
        self.driver.find_element_by_xpath('//*[@id="credit_card_year"]').send_keys(year)
        self.driver.find_element_by_xpath('//*[@id="credit_card_cvv"]').send_keys(cvv)
        self.driver.find_element_by_xpath('//*[@id="order_terms"]').click()

        self.driver.find_element_by_xpath('//*[@id="submit_button"]').click()
 
my_bot = SupremeBot('Jano Mrkva', 'nieco@gmail.com', '0999999888', 'palackeho 15', 'Bratislava', '85202', '1111222233334444', '555', '02', '2021', 'SLOVAKIA', 'Medium', '1', 'Black') #DELIVERY UDAJE
sleep(600)
#dorobit automaticke spustenie--spravit - windows event scheduler + teamviewer + mulitpolozky//hard-code , stopky-test
