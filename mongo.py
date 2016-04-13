# -*- coding: utf-8 -*-

# mongodb module

# import mongo driver
from pymongo import MongoClient
client = MongoClient()

<<<<<<< HEAD
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
=======
db = client['test_car']

def insert_url(car):
    cars = db.cars_url
    car_id = cars.insert_one(car).inserted_id
    print car_id
    
def insert_model(car):
    cars = db.cars_model
    car_id = cars.insert_one(car).inserted_id
    print car_id
    
def insert_spec(car):
    cars = db.cars_spec_light
    car_id = cars.insert_one(car).inserted_id
    print car_id
>>>>>>> 72f120cca916b21bc73810607eb91f571b546c7b
