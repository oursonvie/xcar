# -*- coding: utf-8 -*-

import crawler
import mongo

# import mongo driver
from pymongo import MongoClient
client = MongoClient()

db = client['test_car']

# this is the second part of the program which take infromation already have in the database
# and fatch more spec information of each model 

# define base link
baselink = "http://newcar.xcar.com.cn"

# select DB collection
cars = db.cars_url.find()

check = db.cars_model

# loop in collection
for car in cars:
    brand = car['Brand']
    name = car['Name']
    url = car['url']
    car_id = car['_id']
    
    check_length = check.find_one({'url':url})
    if type(check_length) != dict:
        allspecpage = crawler.readlink(baselink + url)
    
        for each in allspecpage.findAll('td',{'class':'list_version'}):
            model = each.a.string
            model_url = each.a['href']

            car_model = {
                'Brand': brand,
                'Name': name,
                'url': url,
                'Model': model,
                'Model_url': model_url
            }
            print brand + '|' + name + '|' + model
            mongo.insert_model(car_model)
    else:
        print brand,name,car_id
    