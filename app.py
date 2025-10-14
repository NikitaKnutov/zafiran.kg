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

# @app.route('/licenses')
# def software():
#     return render_template('licenses.html')

@app.route('/advantages')
def advantages():
    return render_template('advantages.html')

@app.route('/documents')
def documents():
    return render_template('documents.html')


if __name__ == '__main__':
    app.run(debug=True)
