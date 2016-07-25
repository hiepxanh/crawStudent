from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from time import sleep

from TheTableData import TheTableData
from CrawStudent import CrawStudent

def Quet_nganh(ten_nganh):
    fullNganh = []
    for nganhHoc in nganhHocs:
        #tim den the select sau do lay source trang web
        select = Select(driver.find_element_by_id(ten_nganh))                                                                            
        select.select_by_value(nganhHoc)
        driver.find_element_by_id('dnn_ctr1651_Default_ctl00_btnTim').click() 
        crawstudent = CrawStudent(driver)
        nganhdata = crawstudent.toList()
        fullNganh += nganhdata # noi list student craw duoc vao list tong.
    print('done')
    print('so luong:',len(fullNganh))
    return fullNganh

#khoi tao thong tin ban dau
driver = webdriver.Chrome()
driver.get("http://dkts.hvtc.edu.vn/tabid/927/act/danhsach/Default.aspx")
nganhHocs = ['H','K','Z','A','Q','T'] # nganh hoc tuong ung trong tag select/option[value=""]
nganh1 = "dnn_ctr1651_Default_ctl00_drpNganh1"
nganh2= "dnn_ctr1651_Default_ctl00_drpNganh2"
# tien hanh quet
print('Scanning nganh 1: ................')
driver.get("http://dkts.hvtc.edu.vn/tabid/927/act/danhsach/Default.aspx")
fullNganh1 = Quet_nganh(nganh1)

# xuat ra file excel
import pyexcel
import pyexcel.ext.xlsx
sheet = pyexcel.Sheet(fullNganh1)
sheet.save_as("nganh1.xlsx")
