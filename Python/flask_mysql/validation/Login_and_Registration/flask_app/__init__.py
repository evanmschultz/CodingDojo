from flask import Flask

app: Flask = Flask(__name__)
app.secret_key = 'secret_key'
