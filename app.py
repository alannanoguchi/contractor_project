from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)
client = MongoClient()
db = client.Contractor
contractor = db.contractor

@app.route('/')
def index():
    """Return homepage."""
    return render_template('home.html', msg="Lanilulu's Bracelets")

@app.route('/')
def collections_index():
    """Show all items in collection"""
    return render_template('collections_index.html', items=items.find())


@app.route('/collections', methods=['POST'])
def item_submit():
    """Submit a new item."""
    item = {
        "title": request.form.get("title"),
        "description": request.form.get("description")
    }
    print(request.form.to_dict())
    return redirect(url_for('inventory'))


@app.route('/inventory/<item_id>')
def item_show(item_id):
    """Show a item."""
    return f'My ID is {item_id}'


@app.route('/inventory/<item_id>/delete', methods=['POST'])
def item_delete(item_id):
    """Delete one item."""
    item.delete_one({'_id': ObjectId(item_id)})
    return redirect(url_for('inventory'))

    

@app.route('/inventory')
def inventory_new():
    """Takes owner to inventory"""
    return render_template('inventory.html')


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