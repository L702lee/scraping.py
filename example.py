
import selenium
from selenium import webdriver as wb
from selenium.webdriver.support.ui import Select
import pandas as pd
import time
wbD=wb.Chrome('chromedriver.exe')
wbD.get('https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1')
listOflinks =[]
condition =True
while condition:
    time.sleep(3)
    productInfoList=wbD.find_elements_by_class_name('a-size-mini')
    for el in productInfoList:
        if(el.text !="" and el.text !="Sponsored"):
            pp2=el.find_element_by_tag_name('a')
            listOflinks.append(pp2.get_property('href'))
    try:
        wbD.find_element_by_class_name('a-last').find_element_by_tag_name('a').get_property('href')
        wbD.find_element_by_class_name('a-last').click()
    except:
        condition=False
len(listOflinks)`
from tqdm import tqdm
alldetails=[]
brand=""
model=""

for i in tqdm(listOflinks):
    wbD.get(i)
    time.sleep(3)
    sku = wbD.find_element_by_xpath('//*[@id="productTitle"]').text
    category= wbD.find_element_by_xpath('//*[@id="wayfinding-breadcrumbs_feature_div"]/ul/li[7]/span/a').text
    try:
        try:
            price = wbD.find_element_by_xpath('//*[@id="priceblock_ourprice"]').text
        except:
            price = wbD.find_element_by_xpath('//*[@id="priceblock_dealprice"]').text
    except:
        price=""
        
    pp=wbD.find_element_by_class_name('pdTab')
    pp1=pp.find_elements_by_tag_name('tr')
    for el in range(len(pp1)-1):
        if (pp1[el].find_element_by_class_name("label").text) == 'Brand':
            brand= pp1[el].find_element_by_class_name("value").text
        if (pp1[el].find_element_by_class_name("label").text) == 'Model':
            model= pp1[el].find_element_by_class_name("value").text
        
    temp ={
        'SKU':sku,
        'Category':category,
        'Price':price,
        'Brand':brand,
        'Model':model,
        'linkofproduct':i}
    alldetails.append(temp)
pd.DataFrame(alldetails)
data = pd.DataFrame(alldetails)
data.to_csv('Amazon_tv.csv')
