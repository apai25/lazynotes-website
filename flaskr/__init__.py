from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'IJ0/tEzw{Yn-3x4aCj=mDWA9$cmker'

from flaskr import views