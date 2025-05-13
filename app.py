from flask import Flask, render_template, jsonify, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import json
from models import db, Shop # models.py から db と Shop をインポート

app = Flask(__name__)

# SQLAlchemyの設定
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shops.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app) # Flaskアプリと関連付け


def init_database():
    with app.app_context():
        db.create_all()
        from shops import shops_data
        for shop_data in shops_data:
            shop = Shop(**shop_data)
            db.session.add(shop)
        db.session.commit()

with app.app_context():
    init_database()



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/shops')
def get_shops():
    shops = Shop.query.all()
    return jsonify([
        {
            'id': shop.id,
            'name': shop.name,
            'address': shop.address,
            'lat': shop.lat,
            'lng': shop.lng,
            'cashless': shop.cashless
        } for shop in shops
    ])

@app.route('/admin/add', methods=['GET', 'POST'])
def add_shop():
    """
    店舗追加フォームと処理
    """
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        lat = float(request.form['lat'])
        lng = float(request.form['lng'])
        cashless = request.form['cashless']
        shop = Shop(name=name, address=address, lat=lat, lng=lng, cashless=cashless)
        db.session.add(shop)
        db.session.commit()
        return redirect(url_for('index'))  # 追加後に一覧ページにリダイレクト
    return render_template('add_shop.html')

@app.route('/admin/insert', methods=['POST'])
def insert_shop():
    # ...
    shop = Shop(name=name, address=address, lat=lat, lng=lng, cashless=cashless)
    db.session.add(shop)
    db.session.commit()
    return jsonify({'message': 'Data inserted successfully!'}), 200

@app.route('/admin/delete/<int:id>', methods=['POST'])
def delete_shop(id):
    shop = Shop.query.get_or_404(id)
    db.session.delete(shop)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)