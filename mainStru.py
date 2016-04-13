# -*- coding: utf-8 -*-

import crawler
import mongo

from pymongo import MongoClient
# can only refer to mongo ObjectID with this import
from bson.objectid import ObjectId

client = MongoClient() 

db = client['test_car_2']
# this version will breaking the main page in a more structured way

# define links
mainpage = "http://newcar.xcar.com.cn/price/"
baselink = "http://newcar.xcar.com.cn"

def resetCollection():
    mongo.resetCollection()

def getbrand():
    mainpage_content = crawler.readlink(mainpage)
    
    # get each car model with their corresponding brand name
    # extract the brand name
    
    # this is car containter accroding to their initials, there are total 22 initals in the main page
    car_container = mainpage_content.findAll('div',attrs={'class':'container'})
    
    # in each container there are N elements of tr, which represents a specfic car brand
    for init in car_container:
        # the following extract each brand into a block
        for each_tr in init.findAll('tr'):
            brand_name = each_tr.findAll('td')[0].text
            #print brand_name
            
            # each div is made of two parts, p for sub model name and li for each model under such sub model
            for each_column_content in each_tr.findAll('td')[1].findAll('div', attrs = {'class': 'column_content'}):
                sub_brand_name = each_column_content.p.text
                #print sub_brand_name
                
                for brand in each_column_content.findAll('li'):
                    name = brand.text
                    url = brand.a['href']
                    # print name
                    
                    # print brand_name, sub_brand_name, name, url
                    
                    car = {
                        'brand' : brand_name,
                        'sub_brand' : sub_brand_name,
                        'name' : name,
                        'url' : url
                    }
                    
                    mongo.insert_brand(car)

def getmodel():
    
    
    counter = 0
    
    for car in db.temp.find():
        
        url = car['url']
        brand = car['brand']
        sub_brand = car['sub_brand']
        name = car['name']
        
        counter += 1

        model_page = crawler.readlink(baselink + url)

        for each_model in model_page.findAll('td',{'class':'list_version'}):
            model = each_model.a.string
            model_url = each_model.a['href']

            car_model = {
                'brand' : brand,
                'sub_brand' : sub_brand,
                'name' : name,
                'url' : url,
                'model' : model,
                'model_url' : model_url
            }

            # print car_model

            mongo.insert_model(car_model)

    
def getspec():
    check = db.model
    
    for car in check.find():
        brand = car['brand']
        sub_brand = car['sub_brand']
        name = car['name']
        url = car['url']
        model = car['model']
        model_url = car['model_url']
        _id = car['_id']
        
        check_length = car.get('price')
        if type(check_length) != dict:
            specpage = crawler.readlink(baselink + model_url)
            
            if len(specpage.findAll('em', text = u'排量(L)：')) != 0:
                price = float(specpage.b.text) * 10
                horsepower = specpage.find('em', text = u'最大功率(kW/rpm)：').findNext('td').text
                liter = specpage.find('em', text = u'排量(L)：').findNext('td').text
                engine_type = specpage.find('em', text = u'进气形式：').findNext('td').text
                tourque = specpage.find('em', text = u'最大扭矩(Nm/rpm)：').findNext('td').text
                drive = specpage.find('em', text = u'驱动方式：').findNext('td').text
            else:
                price = float(specpage.find('div', attrs = {'class':'price'}).b.text) * 10
                horsepower = 0
                liter = 0
                engine_type = 0
                tourque = 0
                drive = 0
                
            car = {
                '_id': _id,
                'url': url,
                'brand': brand,
                'sub_brand': sub_brand,
                'name': name,
                'model': model,
                'model_url': model_url,
                'price': price,
                'engine_size': liter,
                'engine_type': engine_type,
                'horsepower': horsepower,
                'tourque': tourque,
                'drive': drive
            }
            
            s = check.update(
                {'_id':_id},
                {'$set': {
                        'price': price,
                        'engine_size': liter,
                        'engine_type': engine_type,
                        'horsepower': horsepower,
                        'tourque': tourque,
                        'drive': drive
                    }
                }
            )
            
            print car['_id'], car['brand'], car['sub_brand'], car['name'], car['model'], car['price'], s
            
        else:
            print('Spec already there')

def main():
    resetCollection()
    getbrand()
    getmodel()
    getspec()
        
if __name__ == "__main__":
    main()