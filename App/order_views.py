
import os
from datetime import datetime

from flask import Blueprint, render_template, session, jsonify, request

from App.models import User, House, Order
from utils import status_code

order_blueprint = Blueprint('order', __name__)

'''
下单，创建预约单
'''
@order_blueprint.route('/', methods=['POST'])
def order():
    # 接收参数
    dict = request.form
    house_id = int(dict.get('house_id'))
    start_date = datetime.strptime(dict.get('start_date'), '%Y-%m-%d')
    end_date = datetime.strptime(dict.get('end_date'), '%Y-%m-%d')
    # 验证有效性
    if not all([house_id, start_date, end_date]):
        return jsonify(status_code.PARAMS_ERROR)
    if start_date > end_date:
        return jsonify(status_code.ORDER_START_END_TIME_ERROR)
    # 查询房屋对象
    try:
        house = House.query.get(house_id)
    except:
        return jsonify(status_code.DATABASE_ERROR)
    # 创建订单对象
    order = Order()
    order.user_id = session['user_id']
    order.house_id = house_id
    order.begin_date = start_date
    order.end_date = end_date
    order.days = (end_date - start_date).days + 1
    order.house_price = house.price
    order.amount = order.days * order.house_price

    try:
        order.add_update()
    except:
        return jsonify(status_code.DATABASE_ERROR)

    # 返回信息
    return jsonify(code=status_code.OK)


'''
订单
'''
@order_blueprint.route('/orders/')
def orders():

    return render_template('orders.html')


'''
所有订单接口
作为租客查询订单
'''
@order_blueprint.route('/allorders/', methods=['GET'])
def all_orders():

    uid = session['user_id']
    order_list = Order.query.filter(Order.user_id == uid).order_by(Order.id.desc())
    order_list2 = [order.to_dict() for order in order_list]
    return jsonify(olist=order_list2)


@order_blueprint.route('/lorders/', methods=['GET'])
def lorders_html():

    return render_template('lorders.html')

'''
作为房东查询订单
'''
@order_blueprint.route('/fd/',methods=['GET'])
def lorders():
    uid=session['user_id']
    #查询当前用户的所有房屋编号
    hlist=House.query.filter(House.user_id==uid)
    hid_list=[house.id for house in hlist]
    #根据房屋编号查找订单
    order_list=Order.query.filter(Order.house_id.in_(hid_list)).order_by(Order.id.desc())
    #构造结果
    olist=[order.to_dict() for order in order_list]
    return jsonify(olist=olist)


'''
修改订单状态
'''
@order_blueprint.route('/order/<int:id>/',methods=['PUT'])
def status(id):
    #接收参数：状态
    status=request.form.get('status')
    #查找订单对象
    order=Order.query.get(id)
    #修改
    order.status=status
    #如果是拒单，需要添加原因
    if status=='REJECTED':
        order.comment=request.form.get('comment')
    #保存
    try:
        order.add_update()
    except:
        return jsonify(status_code.DATABASE_ERROR)

    return jsonify(code=status_code.OK)
