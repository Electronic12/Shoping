from datetime import datetime
from main import app, db


class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(150), nullable=False)
    product_price = db.Column(db.String(255))
    description = db.Column(db.String(1000))
    product_key = db.Column(db.String(150), nullable=False, unique=True)
    product_sale = db.Column(db.String(50))
    product_type = db.Column(db.String(150))
    product_image = db.Column(db.String(20))
    dateAdded = db.Column(db.DateTime,default=datetime.now())
    dateUpdated = db.Column(db.DateTime,default=datetime.now(),onupdate=datetime.now())
    
    def json(self):
        product = {
            "id": self.id,
            "product_name": self.name,
            "description": self.description,
            "product_key": self.product_key,
            "product_sale": self.product_sale,
            "product_image": self.product_image,
            "dateAdded": self.dateAdded
        }
        return product

    def __repr__(self):
        return f"User('{self.product_name}', '{self.product_key}', '{self.product_sale}', '{self.product_image}', '{self.description}')"

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    surname = db.Column(db.String(150))
    email = db.Column(db.String(150), nullable=False, unique=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(150))
    phone_number = db.Column(db.String(50))
    secret_key = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(1000))
    dateAdded = db.Column(db.DateTime,default=datetime.utcnow)
    dateUpdated = db.Column(db.DateTime,default=datetime.now(),onupdate=datetime.now())

    def json(self):
        user = {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "email": self.email,
            "username": self.username,
            "password": self.password,
            "phone_number": self.phone_number,
            "secret_key": self.secret_key,
            "description": self.description,
            "dateAdded": self.dateAdded
        }
        return user

    def __repr__(self):
        return f"User('{self.name}', '{self.surname}', '{self.email}', '{self.password}', '{self.phone_number}', '{self.secret_key}', '{self.description}', '{self.username}')"

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    surname = db.Column(db.String(150))
    email = db.Column(db.String(150), nullable=False, unique=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(150))
    phone_number = db.Column(db.String(50))
    passport_number = db.Column(db.String(50))
    secret_key = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(1000))
    dateAdded = db.Column(db.DateTime,default=datetime.now())
    dateUpdated = db.Column(db.DateTime,default=datetime.now(),onupdate=datetime.now())

    def json(self):
        admin = {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "email": self.email,
            "username": self.username,
            "password": self.password,
            "phone_number": self.phone_number,
            "passport_number": self.passport_number,
            "secret_key": self.secret_key,
            "description": self.description,
            "dateAdded": self.dateAdded
        }
        return admin
        
    def __repr__(self):
        return f"User('{self.name}', '{self.surname}', '{self.email}', '{self.password}', '{self.phone_number}', '{self.secret_key}', '{self.description}', '{self.username}')"