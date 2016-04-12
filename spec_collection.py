# -*- coding: utf-8 -*-

import crawler
import mongo

# in this module, data form model will be read and spec of each model is 
# recorded int he database

# import mongo driver
from pymongo import MongoClient
client = MongoClient()

db = client['test_car']

# define base link
baselink = "http://newcar.xcar.com.cn"

# select DB collection
cars = db.cars_model.find()

# loop in collection and get spec

for car in cars:
    brand = car['Brand']
    name = car['Name']
    model = car['Model']
    url = car['Model_url']
    car_id = car['_id']
    
    specpage = crawler.readlink(baselink + url)

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
    
    car = {'url': url,
           'Brand': brand,
           'Name': name,
           'Model': model,
           'Price': price,
           'Engine_size': liter,
           'Engine_type': engine_type,
           'Horsepower': horsepower,
           'Tourque': tourque,
           'Drive': drive
    }
    
    print ('%s %s %s %sk %skW') % (brand, name, model, price, horsepower)
    mongo.insert_spec(car)
    