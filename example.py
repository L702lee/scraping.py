import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from urllib.request import urlopen 
import requests

headers_std = {
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
'Content-Type': 'text/html',
}

url = "https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1"
html = requests.get(url,headers=headers_std).text
soup = BeautifulSoup(html,'lxml')

product_name_class = "a-size-base-plus a-color-base a-text-normal"
actual_price_class = "a-price"
rating_class = "a-icon-alt"
number_of_reviewss_class = 'a-size-base'
main_page_url_class ="a-link-normal a-text-normal"
asin="a-asin"

#scrape the product details
product_names = soup.find_all("span", {"class":product_name_class})
product_prices = soup.find_all("span",{"class":actual_price_class})
ratings = soup.find_all("span",{"class":rating_class})
number_of_reviewss = soup.find_all('span',{'class':number_of_reviews_class})
main_page_urls = soup.find_all("a",{'class': main_page_url_class})
asin = soup.find_all("a",{'class':asin_class})

print(product_names[0].text.strip())
print(product_prices[0].text.strip())
print(ratings[0].text.strip())
print(number_of_reviews[0].content)
print(main_page_urls[0].get('href').strip())
print(asin[0].text.strip())

print(len(product_names))
print(len(product_prices))
print(len(ratings))
print(len(number_of_reviews))
print(len(main_page_urls))
print(len(asin))

product_names_df = []
product_prices_df = []
ratings_df = []
number_of_reviews = []
main_page_urls_df = []
asin = []

for i in range(len(product_names)):

	product_names_df.append(product_names[i].text.strip())
	product_prices_df.append(product_prices[i].text.strip())
	main_page_urls_df.append("amazon.in" + main_page_urls[i].get('href').strip())
    asin_df.append(asin[0].text.strip())

	try:
		ratings_df.append(ratings[i].text.strip())
        number_of_reviews.append(number_of_reviews.text.strip())
	except:
		ratings_df.append(None)

df = pd.DataFrame({'product_page':main_page_urls_df,'product_name':product_names_df,'rating':ratings_df,'number_of_reviews':number_of_reviews_df,'price (INR)':product_prices_df,'asin':asin_df})
print(df.head())

df.to_csv('amazon.csv',index=False)
