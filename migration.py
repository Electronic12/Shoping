from main import db

from main.models import (
	User,
    Products,
    Admin,
)

from main.db_migration_data.data_config import admins
from main.db_migration_data.products_config import products

db.drop_all()
db.create_all()

for admin in admins:
    db_admin = Admin(**admin)
    db.session.add(db_admin)
    db.session.commit()

for product in products:
    db_product = Products(**product)
    db.session.add(db_product)
    db.session.commit()