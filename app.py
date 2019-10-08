from flask import Flask, render_template
from pymongo import MangoClient

app = Flask(__name__)
client = MangoClient()
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


if __name__ == '__main__':
    app.run(debug=True)