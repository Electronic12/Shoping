from turtle import pos
from flask import render_template, Blueprint
from .forms import ProductForm
from main.models import Products
from main import db

products = Blueprint('products', __name__)

@products.route('/all_products/')
def all_products():
    our_products = Products.query.all()
    return render_template("products.html", our_products=our_products)

@products.route('/yuwunmak_ucin/')
def yuwunmak_ucin():
    clear_products = Products.query.filter_by(product_type=2)
    return render_template("clear_pro.html", clear_products=clear_products)

@products.route('/electronics_tel/')
def electronics_tel():
    tel_products = Products.query.filter_by(product_type=3)
    return render_template("electronics.html", tel_products=tel_products)

@products.route('/azyk_haryt/')
def azyk_haryt():
    azyk_products = Products.query.filter_by(product_type=1)
    return render_template("azyk_haryt.html", azyk_products=azyk_products)

@products.route('/product/<int:id>/delete/', methods=['GET', 'POST'])
def delete_product(id):
    print(id)
    delete_product = Products.query.get_or_404(id)
    print(delete_product)
    db.session.delete(delete_product)
    db.session.commit()
    our_products = Products.query.all()
    return render_template("products.html", our_products=our_products)


@products.route('/add_product/', methods=['GET', 'POST'])
def add_products():
    form = ProductForm()
    if form.validate_on_submit():
        new_product = Products.query.filter_by(product_key=form.product_key.data).first()
        if new_product is None:
            new_product = Products(product_name=form.product_name.data, product_price=form.product_price.data, product_key=form.product_key.data, product_type=form.product_type.data, product_sale=form.product_sale.data, description=form.product_description.data)
            db.session.add(new_product)
            db.session.commit()
        name = form.product_name.data
        form.product_name.data = ''
        form.product_price.data = ''
        form.product_key.data = ''
        form.product_type.data = ''
        form.product_sale.data = ''
        form.product_description.data = ''
    title = "hi"
    return render_template('add_product.html', form=form)
