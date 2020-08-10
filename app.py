from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbhomework


## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
# 여길 채워나가세요!
    name_receive = request.form.get('name_give')
    count_receive = request.form.get('count_give')
    address_receive = request.form.get('address_give')
    phone_receive = request.form.get('phone_give')

    information = {
        'name': name_receive,
        'count': count_receive,
        'address': address_receive,
        'phone': phone_receive
    }
    # print(information)
    db.orders.insert_one(information)

    return jsonify({'result': 'success', 'msg': '주문이 완료되었습니다!'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
# 여길 채워나가세요!
    all_orders = list(db.orders.find({}, {'_id': False}))
    return jsonify({'result': 'success', 'orders': all_orders})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
