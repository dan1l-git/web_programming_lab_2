from .models import Car
from . import db

def get_all_cars():
    return Car.query.all()

def get_car_by_id(car_id):
    return Car.query.get(car_id)

def create_car(model, year, manufacturer_id, color):
    new_car = Car(model=model, year=year, manufacturer_id=manufacturer_id, color=color)
    db.session.add(new_car)
    db.session.commit()

def update_car(car_id, model, year, manufacturer_id, color):
    car = get_car_by_id(car_id)
    if car:
        car.model = model
        car.year = year
        car.manufacturer_id = manufacturer_id
        car.color = color
        db.session.commit()

def delete_car(car_id):
    car = get_car_by_id(car_id)
    if car:
        db.session.delete(car)
        db.session.commit()