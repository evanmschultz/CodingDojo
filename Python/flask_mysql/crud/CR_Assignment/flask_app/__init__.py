from flask import Flask

app = Flask(import_name=__name__)
app.secret_key = 'secret_key'
