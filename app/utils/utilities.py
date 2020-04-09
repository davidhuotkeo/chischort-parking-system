from random import randint
import base64
from datetime import datetime
from werkzeug.security import check_password_hash
from uuid import uuid4

def generate_lane_id():
    id_ = str(uuid4()).replace("-", "")
    id_ = id_[:16]
    return id_.upper()

def generate_id(end_num):
    num = randint(0, end_num)
    str_num = str(num)
    num_length = len(str_num)
    if num_length < 6:
        zero_num = 6 - len(str_num)
        zero = "0" * zero_num
        str_num = zero + str_num
    return str_num

def get_date():
    return datetime.now()

def add_to_database(db, parking):
    db.session.add(parking)
    db.session.commit()

def continue_lane(db, lane_database, startlane, number_loop, base_price, add_on, place):
    total_start_length = len(startlane)
    int_start_lane = int(startlane)
    number_zero = "0"
    for i in range(int(number_loop)):
        string_lane = str(int_start_lane)
        lane_id = number_zero * (total_start_length - len(string_lane)) + string_lane
        lane = lane_database(lane_id, base_price, add_on, place)
        int_start_lane += 1
        db.session.add(lane)
    db.session.commit()
