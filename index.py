from flask import Flask, render_template
# from flask import make_response 

# cursor = <connection-name>.cursor(buffered=True)

app = Flask(__name__)
# app = APIFlask(__name__)

@app.route('/')

def home():
    return 'home'

# Función raíz

# Función about, una subruta en la página.
@app.route('/about')
def about():
    return 'About'


if __name__ == '__main__':
    app.run()