from flask import Flask

app = Flask(__name__)

@app.route('/')

# Función raíz
def home():
    return 'home'

# Función about, una subruta en la página.
@app.route('/about')
def about():
    return 'About'

if __name__ == '__main__':
    app.run()