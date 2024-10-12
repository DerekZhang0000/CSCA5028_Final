from flask import Flask, render_template, jsonify, Response

import auth
import kroger
import db
import analyze

app = Flask(__name__)

# Home route to render the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Route to generate the first plot
@app.route('/plot1.png')
def plot1_png():
    return Response(analyze.plot_prices('product_1111040101'), mimetype='image/png')

# Route to generate the second plot
@app.route('/plot2.png')
def plot2_png():
    return Response(analyze.plot_prices('product_1111009434'), mimetype='image/png')

# Update database function
@app.route('/call-function', methods=['POST'])
def call_function():
    access_token = auth.get_access_token()
    data = kroger.get_product_infos('milk', access_token, limit=10)
    for id, name, price in data:
        db.add_product(id, name, price)
    data = kroger.get_product_infos('cheese', access_token, limit=10)
    for id, name, price in data:
        db.add_product(id, name, price)
    print("Milk and cheese updated.")
    result = {"message": "Milk and cheese updated."}
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)