from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


def read_json():
    try:
        with open('products.json', 'r') as f:
            return json.load(f)
    except Exception:
        return []


def read_csv():
    products = []
    try:
        with open('products.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # id və price convert et
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
    except Exception:
        return []
    return products


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    # 🔴 source yoxlama
    if source not in ['json', 'csv']:
        return render_template('product_display.html',
                               error="Wrong source",
                               products=[])

    # 📦 data oxu
    if source == 'json':
        data = read_json()
    else:
        data = read_csv()

    # 🔍 id varsa filter et
    if product_id:
        try:
            product_id = int(product_id)
            data = [p for p in data if p['id'] == product_id]

            if not data:
                return render_template('product_display.html',
                                       error="Product not found",
                                       products=[])
        except ValueError:
            return render_template('product_display.html',
                                   error="Invalid ID",
                                   products=[])

    return render_template('product_display.html',
                           products=data,
                           error=None)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
