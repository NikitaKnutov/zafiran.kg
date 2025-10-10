from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/software')
def software():
    return render_template('software.html')

@app.route('/advantages')
def advantages():
    return render_template('advantages.html')

@app.route('/aml')
def aml():
    return render_template('aml.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/documents')
def documents():
    return render_template('documents.html')

@app.route('/products')
def products():
    return render_template('products.html')

if __name__ == '__main__':
    app.run(debug=True)
