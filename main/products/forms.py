from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class ProductForm(FlaskForm):
    product_name = StringField('Ady', validators=[DataRequired()])
    product_price = StringField('Bahasy', validators=[DataRequired()])
    product_key = StringField('Harydyň kody', validators=[DataRequired()])
    product_type = StringField('Harydyň görnüşi', validators=[DataRequired()])
    product_sale = StringField('Arzanladyş(%)', validators=[DataRequired()])
    product_description = TextAreaField('Tanyşdyryş', validators=[DataRequired()])
    submit = SubmitField('Harydy goş')


class ProductUpdateForm(FlaskForm):
    product_name = StringField('Ady', validators=[DataRequired()])
    product_price = StringField('Bahasy', validators=[DataRequired()])
    product_key = StringField('Harydyň kody', validators=[DataRequired()])
    product_type = StringField('Harydyň görnüşi', validators=[DataRequired()])
    product_sale = StringField('Arzanladyş(%)', validators=[DataRequired()])
    product_description = TextAreaField('Tanyşdyryş', validators=[DataRequired()])
    submit = SubmitField('Tazelemek')
