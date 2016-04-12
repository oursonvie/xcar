# -*- coding: utf-8 -*-

import crawler
import mongo

# this will go to the main page of xcar and get all the car brand and its model
# no spec for each model thought

mainpage = "http://newcar.xcar.com.cn/price/"

def main():
    mainpage_content = crawler.readlink(mainpage)
    
    for brand in mainpage_content.findAll('div', attrs = {'class':'column_content'}):
        brandName = brand.find('p').text
        for car in brand.findAll('a', title = True):
            name = car.text
            url = car['href']
            print brandName +'|'+ name + '|' + url

            car_url = {
                'Brand': brandName,
                'Name': name,
                'url': url
            }
        
            mongo.insert_url(car_url)
        
if __name__ == "__main__":
    main()