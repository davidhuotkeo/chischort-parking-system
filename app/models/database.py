from app import app
from app.utils.utilities import generate_lane_id, get_date
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class Parking(db.Model):
    _id = db.Column(db.String(10), primary_key=True)
    location = db.Column(db.String(10))
    service = db.Column(db.String(30))
    park = db.Column(db.DateTime)
    end = db.Column(db.DateTime)
    payment = db.Column(db.Integer)
    encryption = db.Column(db.String(150))

    def __init__(self, _id, location, service, encryption):
        self._id = _id
        self.location = location
        self.service = service
        self.park = get_date()
        self.end = None
        self.payment = None
        self.encryption = encryption

class LaneId(db.Model):
    lane = db.Column(db.String(10), primary_key=True)
    lane_id = db.Column(db.String(20))
    base_price = db.Column(db.Integer)
    add_on = db.Column(db.Integer)

    def __init__(self, lane, base_price, add_on):
        self.lane = lane
        self.lane_id = generate_lane_id()
        self.base_price = base_price
        self.add_on = add_on
