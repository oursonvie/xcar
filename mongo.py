# -*- coding: utf-8 -*-

# mongodb module

# import mongo driver
from pymongo import MongoClient
client = MongoClient()

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