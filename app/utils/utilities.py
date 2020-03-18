from random import randint
import base64
from datetime import datetime
from werkzeug.security import check_password_hash

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
