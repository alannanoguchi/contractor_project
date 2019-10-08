from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient()
db = client.Contractor
contractor = db.contractor

@app.route('/')
def index():
    """Return homepage."""
    return render_template('home.html', msg='Homepage')


@app.route('/')
def collections_index():
    """Show all items in collection"""
    return render_template('collections_index.html', collections=collections.find())
    

@app.route('/cart')
def cart_new():
    """Takes user to view the cart"""
    return render_template('cart.html')


@app.route('/collections')
def collections_page():
    """Takes user to collections"""
    return render_template('collections.html')


@app.route('/new')
def new_items_page():
    """Takes user to new items page"""
    return render_template('new.html')

    
@app.route('/sale')
def sale_page():
    """Takes user to sale items page"""
    return render_template('sale.html')


@app.route('/casual')
def casual_items_page():
    """Takes user to casual items page"""
    return render_template('casual.html')


if __name__ == '__main__':
    app.run(debug=True)