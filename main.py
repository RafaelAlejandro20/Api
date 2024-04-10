from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

def cargar_datos():
    df = pd.read_csv('datos.csv')
    return df.head()

@app.route('/')
def index():
    datos = cargar_datos()
    return render_template('index.html', datos=datos.to_html())

if __name__ == '__main__':
    app.run(debug=True)