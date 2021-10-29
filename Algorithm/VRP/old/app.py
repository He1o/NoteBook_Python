# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name: Passengers-scheduling-plus
File Name: app.py
Author: hhx
Contact: houhaixu_email@163.com
Create Date: 2021/1/31
-------------------------------------------------
"""
import json
from typing import List

from flask import Flask, render_template, jsonify, request

from schedule_utils.data_utils import receive_data, send_data, load_data
from schedule_utils.models import Car, Order
from schedule_utils.scheduling import run, test_schedule, is_in_scope
from schedule_utils.pso_by_car import Pso
from collections import defaultdict
import numpy as np
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/schedule/<mode>/')
def schedule(mode):
    result = run(int(mode), debug=True)

    if result is None:
        return jsonify({'status': 500})
    return jsonify({
        'status': 200,
        'data': result
    })

PSO = []
def pso(driver_list, user_list):


    cars = []
    size_cars = []
    for car in driver_list:
        cars.append([float(car["coordinate"][0]), float(car["coordinate"][1])])
        size_cars.append(car["sites"])

    psgs = []
    size_psgs = []
    for psg in user_list:
        psgs.append([float(psg["coordinate"][0]), float(psg["coordinate"][1])])
        size_psgs.append(int(psg["size"]))

    cars = cars + [[103.90, 30.50]]
    size_cars = np.array(size_cars + [100])
    size_psgs = np.array(size_psgs)

    p = Pso(cars, psgs, size_cars, size_psgs)
    PSO.append(p)

@app.route('/test/', methods=["POST"])
def test():
    data_txt = str(request.form["data_txt"])
    order_distance = int(request.form["order_distance"])
    car_distance = int(request.form["car_distance"])
    reserve_rate = float(request.form["reserve_rate"])
    type_ = str(request.form["data_type"])
    mode = int(request.form["mode"])
    radius = int(request.form['radius'])
    data = json.loads(data_txt)
    # with open('data.json') as f:
    #     data = json.load(f)
    driver_list = data['driver_list']
    user_list = data['user_list']

    if mode == 1:
        try:
            pso(driver_list, user_list)
            zbest = next(PSO[0].iteration())
            print(zbest)
            result = []
            design = defaultdict(list)
            for i in range(len(user_list)):
                design[zbest[i]].append(i)
            for car, psg in design.items():
                temp = []
                for p in psg:
                    temp.append({
                        'order': {
                            'id': user_list[p]['id'], 'lnglat': [float(user_list[p]["coordinate"][0]), float(user_list[p]["coordinate"][1])],
                            'passenger_num': user_list[p]['size'],
                            'is_grab': user_list[p]['is_grab']
                        }
                    })        
                result.append({
                            'car': {'id': driver_list[car]['driver_id'], 'sites': driver_list[car]['sites'],
                                    'lnglat': [float(driver_list[car]["coordinate"][0]), float(driver_list[car]["coordinate"][1])]},
                            'orders': temp
                        })
        
            return jsonify({
                'status': 200,
                'data': result
            })    
        except Exception as e:
            print(e)
            return jsonify({
                'status': 500
            })




        # zbest =[20,27,26,26,26,27,27,12,10,5,4,13,1,1,12,10,11,11,13,4,5,1,11,1,12,12,12,12]
    if mode == 2:
        try:        
            zbest = next(PSO[0].iteration())
            print(zbest)
            result = []
            design = defaultdict(list)
            for i in range(len(user_list)):
                design[zbest[i]].append(i)
            for car, psg in design.items():
                temp = []
                for p in psg:
                    temp.append({
                        'order': {
                            'id': user_list[p]['id'], 'lnglat': [float(user_list[p]["coordinate"][0]), float(user_list[p]["coordinate"][1])],
                            'passenger_num': user_list[p]['size'],
                            'is_grab': user_list[p]['is_grab']
                        }
                    })        
                result.append({
                            'car': {'id': driver_list[car]['driver_id'], 'sites': driver_list[car]['sites'],
                                    'lnglat': [float(driver_list[car]["coordinate"][0]), float(driver_list[car]["coordinate"][1])]},
                            'orders': temp
                        })
        
            return jsonify({
                'status': 200,
                'data': result
            })

        except Exception as e:
            print(e)
            return jsonify({
                'status': 500
            })


@app.route('/check_data/', methods=["POST"])
def check_data():
    try:
        data_txt = str(request.form["data_txt"])
        type_ = str(request.form["data_type"])
        radius = int(request.form['radius'])

        data = json.loads(data_txt)

        car_list: List[Car] = []  # 车辆列表
        order_list: List[Order] = []  # 订单列表

        for order in data['user_list']:
            o = Order(
                id_=int(order['id']),
                passenger_num=int(order['size']),
                lng=float(order['coordinate'][0]),
                lat=float(order['coordinate'][1]),
                is_grab=is_in_scope(float(order['coordinate'][0]), float(order['coordinate'][1]), radius)
            )
            if order['bind_car'] != '':
                o.bind_car = int(order['bind_car'])
            order_list.append(o)

        if type_ == "receive":
            for car in data['driver_list']:
                car_list.append(
                    Car(
                        id_=int(car['driver_id']),
                        lng=float(car['coordinate'][0]),
                        lat=float(car['coordinate'][1]),
                        sites=int(car['sites'])
                    )
                )
        elif type_ == "send":
            for car in data['driver_list']:
                car_list.append(
                    Car(
                        id_=int(car['driver_id']),
                        lng=0,
                        lat=0,
                        sites=int(car['sites'])
                    )
                )

        orders = [{"lnglat": [order.lng, order.lat], "id": order.id_, "passenger_num": order.passenger_num,
                   "is_grab": order.is_grab} for order in
                  order_list]
        cars = [{"lnglat": [car.lng, car.lat], "id": car.id_, "site_num": car.sites} for car in car_list]

        return jsonify({
            'status': 200,
            'orders': orders,
            'cars': cars
        })
    except:
        return jsonify({
            'status': 500
        })


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8808, debug=False)
