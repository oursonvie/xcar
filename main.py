# -*- coding: utf-8 -*-

import crawler
import mongo

# this will go to the main page of xcar and get all the car brand and its model
# no spec for each model thought

# define links
mainpage = "http://newcar.xcar.com.cn/price/"
baselink = "http://newcar.xcar.com.cn"

def getbrand():
    mainpage_content = crawler.readlink(mainpage)
    
    for brand in mainpage_content.findAll('div', attrs = {'class':'column_content'}):
        brandName = brand.find('p').text
        for car in brand.findAll('a', title = True):
            name = car.text
            url = car['href']
            #print brandName +'|'+ name + '|' + url

            brand = {
                'Brand': brandName,
                'Name': name,
                'Brand_url': url
            }
        
            mongo.insert(brand,brand)
            
def getmodel():
    
    # select collection
    cars = db.cars.find()
    cars_model = db.cars_model.find()
    
    for car in cars:
        brand = car['Brand']
        name = car['Name']
        url = car['Brand_url']
        
        if cars_model['Brand_url']
    
def main():
    getbrand()
    
        
if __name__ == "__main__":
    main()