from flask import Flask
from my_app.url_shortener.views import url_shortener

app = Flask(__name__)
app.register_blueprint(url_shortener)