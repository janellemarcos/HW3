from myapp import myapp_obj
from myapp.forms import TopCities
from flask import render_template, flash, redirect, escape

from myapp import db
from myapp.models import City

    
@myapp_obj.route("/", methods=['GET', 'POST'])
def hello():
    name = 'Janelle'
    title = 'Top Cities'
    top_cities = City.query.order_by(City.city_rank.asc()).all()
    
    form = TopCities()
    if form.validate_on_submit():
        city = City(city_name = form.city_name.data, city_rank = form.city_rank.data, is_visited = form.is_visited.data)
        db.session.add(city)
        db.session.commit()
        flash(f'City {form.city_name.data} ranked {form.city_rank.data} added!, visited={form.is_visited.data}')
        return redirect('/')
    return render_template('hello.html', name=name, title=title, top_cities=top_cities, form=form)

