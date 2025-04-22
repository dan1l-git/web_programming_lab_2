from flask import Blueprint, render_template, request, redirect, url_for, flash
from .services import get_all_cars, get_car_by_id, create_car, update_car, delete_car
from .models import Manufacturer

main = Blueprint('main', __name__)

@main.route('/')
def index():
    cars = get_all_cars()
    return render_template('index.html', cars=cars)

@main.route('/car/add', methods=['GET', 'POST'])
def add_car():
    if request.method == 'POST':
        model = request.form['model']
        year = int(request.form['year'])
        if year <1960 or year > 2025:
            flash('Некоректний рік випуску')
            manufacturers = Manufacturer.query.all()
            return render_template('car_form.html', manufacturers=manufacturers)
        manufacturer_id = int(request.form['manufacturer_id'])
        color = request.form['color']
        create_car(model, year, manufacturer_id, color)
        return redirect(url_for('main.index'))
    manufacturers = Manufacturer.query.all()
    return render_template('car_form.html', manufacturers=manufacturers)

@main.route('/car/<int:car_id>/edit', methods=['GET', 'POST'])
def edit_car(car_id):
    car = get_car_by_id(car_id)
    if request.method == 'POST':
        model = request.form['model']
        year = int(request.form['year'])
        manufacturer_id = int(request.form['manufacturer_id'])
        color = request.form['color']
        update_car(car_id, model, year, manufacturer_id, color)
        return redirect(url_for('main.index'))
    manufacturers = Manufacturer.query.all()
    return render_template('car_form.html', car=car, manufacturers=manufacturers)

@main.route('/car/<int:car_id>/delete')
def delete_car_route(car_id):
    delete_car(car_id)
    return redirect(url_for('main.index'))