from flask import Flask

app = Flask(__name__)
app.config.from_pyfile("../config.py")

from app import views

from app.users.views import user_bp
app.register_blueprint(user_bp, url_prefix='/users')

from app.products.views import product_bp
app.register_blueprint(product_bp, url_prefix='/products')
