import selenium
from selenium import webdriver
from details import pw

from time import sleep

class BitcoinBot:

    def __init__(self, username, pw):

        chromedriver = '/Users/gautham/Google Drive (gdk244@nyu.edu)/Coding/Bitcoin_bot/bitcoin_bot/chromedriver'
        self.driver = selenium.webdriver.Chrome(executable_path = chromedriver)
        self.driver.get("https://www.bustabit.com")
        sleep(2)

        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/a').click()
        sleep(2)

    def get_latest_x(self):

        current = self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div[4]/div/div[1]/div[1]/div[1]/div/div[3]/table/tbody/tr/td[1]/a').text
        
        self.write_to_file(current[:-1])
        while current == self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div[4]/div/div[1]/div[1]/div[1]/div/div[3]/table/tbody/tr/td[1]/a').text:
            pass
        
        self.get_latest_x()
        
    def write_to_file(self, value):
        data_file = open("data.txt","a+")
        data_file.write(value)
        data_file.write('\n')
        data_file.close()



myBot = BitcoinBot('GOATKING2020', pw)

myBot.get_latest_x()