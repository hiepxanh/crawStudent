from selenium import webdriver
from TheTableData import TheTableData
class CrawStudent:
    def __init__(self,driver):
        self.driver = driver
        clickFirstPageButton = clicknextButton = self.driver.find_elements_by_xpath('//div[@id="dnn_ctr1651_Default_ctl00_AspNetPager1"]/a')[0].click()
        self.presentPage = int(self.driver.find_elements_by_xpath('//div[@id="dnn_ctr1651_Default_ctl00_AspNetPager1"]/span')[0].text)        
    def toList(self): # thuat toan de craw student ve: 
        i = 0
        nganh = []
        while i != self.presentPage:  # neu trang hien tai ma van co the tang len duoc thi gan gia tri moi cho i va tiep tuc tang, cho den khi nao trang hien tai khong the tang len duoc nua thi dung
            i = self.presentPage 
            page = TheTableData(self.driver.page_source).tolist()
            nganh += page            
            clicknextButton = self.driver.find_elements_by_xpath('//div[@id="dnn_ctr1651_Default_ctl00_AspNetPager1"]/a')[-2].click()
            self.presentPage = int(self.driver.find_elements_by_xpath('//div[@id="dnn_ctr1651_Default_ctl00_AspNetPager1"]/span')[0].text) # gan gia tri trang hien tai moi duoc cap nhat sau khi an next
        return nganh
