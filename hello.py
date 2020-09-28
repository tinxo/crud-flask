from flask import Flask

app = Flask(__name__)


@app.route('/')  # Esto indica que una función se convierte a una vista
def hello():
    return 'Hola mundo desde Flask'
