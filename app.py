from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    data = (1, "John Doe", "dj@yahoo.com","male")
    return render_template('home.html', person=data)

@app.route('/about')
def about():
    cars = ['Toyota','Honda','Landrover','Suzuki']
    user = "Edwin"
    date ="08-12-2018"

    return render_template('about.html', cars=cars, date=date, user=user)


@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/products/<id>')
def products(id):
    return 'You are on product number '+ id

@app.route('/items/<id>/<user>')
def items(id,user):
    return 'You are on item {} and you are user {}'.format(id, user)


@app.errorhandler(404)
def error(x):
    return('hey,That page is unavailable')





if __name__ == '__main__':
    app.run(debug=True)
