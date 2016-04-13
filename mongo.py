# -*- coding: utf-8 -*-

# mongodb module

# import mongo driver
from pymongo import MongoClient
client = MongoClient()

db = client['test_car_2']

#modelCarCounts = db.cars.count()

def resetCollection():
    db.temp.drop()

def insert_brand(car):
    cars = db.temp    
    car_id = cars.insert_one(car).inserted_id
    #print('%s %s/%s' % (car_id, cars.count(), modelCarCounts))
    print car_id, cars.count()
    
def insert_model(car):
    cars = db.model   
    car_id = cars.insert_one(car).inserted_id
    #print('%s %s/%s' % (car_id, cars.count(), modelCarCounts))
    print car_id, cars.count()