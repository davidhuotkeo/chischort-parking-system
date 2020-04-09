# Load Flask App
from app import app

# Load all flask functions
from flask import (
    request,
    render_template,
    redirect,
    url_for,
    session
)

# Load models (databases) and sql conjunction
from app.models.database import db
from app.models.database import Parking, LaneId
from sqlalchemy import and_

# Load utils functions
from app.utils.utilities import (
    add_to_database,
    get_date,
    generate_id,
    continue_lane
)
from app.utils.view_utils import (
    from_string_to_base64,
    calculate_money,
    encrypt_cipher,
    encrypt_with_key,
    decrypt_cipher,
    send_email
)
from app.utils.file import service_parking

# Home Route
@app.route("/", methods=["GET", "POST"])
def home():
    email = session.get("email")
    if request.method == "POST":
        email = request.form.get("email")
        session["email"] = email
    return render_template("index.html", email=email)

# Service Route
@app.route("/services/<token_id>", methods=["GET", "POST"])
def service(token_id):
    # check lane is in the database or not avoid scamming
    lane = LaneId.query.filter(LaneId.lane_id == token_id).first()
    if not lane:
        return redirect(url_for("not_found"))
    max_number_ticket = 999999999
    # get the location if the lane is exist in database
    location = lane.lane

    # Check wether the lane is used or not
    # with query : SELECT * FROM parking WHERE location=loc AND end=NULL
    lane_used = Parking.query.filter(
        and_(
            Parking.location == location,
            Parking.end == None
        )
    ).first()

    # if the lane is used redirect the lane used route
    if lane_used:
        return redirect(url_for("lane_used"))

    # if select the service choice
    if request.method == "POST":
        form = request.form

        # get the service from chosen service
        service_chosen = form.get("service")

        # get the add on service (check tire)
        payment = service_parking[service_chosen]

        key, encrypted = encrypt_cipher(token_id)
        session["key"] = key

        _id = generate_id(max_number_ticket)
        ticket_numbers = Parking.query.with_entities(Parking._id).all()
        tickets = [ticket[0] for ticket in ticket_numbers]

        while _id in tickets:
            _id = generate_id(max_number_ticket)

        # add to database
        parking = Parking(_id, location, service_chosen, encrypted)
        add_to_database(db, parking)

        user_email = session.get("email")
        qrcode_base = from_string_to_base64(_id)
        message = f"""
        <html>
            <body>
                <strong>No reply</strong><br>
                <p>Here is the ticket from <strong>Chis Chort</strong>!</p>
                <p>{_id}</p>
            </body>
        </html>
        """

        if user_email:
            send_email(user_email, _id, message)

        return redirect(url_for("ticket", token_id=token_id))
    return render_template("service.html", base_price=lane.base_price, each=lane.add_on)

# Ticket Route
@app.route("/ticket/<token_id>", methods=["GET"])
def ticket(token_id):
    # if the user is parked with the cookies
    key = session.get("key")
    lane = LaneId.query.filter(LaneId.lane_id == token_id).first()
    encrypted = Parking.query.with_entities(Parking.encryption).filter(
        and_(
            Parking.location == lane.lane,
            Parking.end == None
        )
    ).first()
    if key and encrypted:
        if decrypt_cipher(key, encrypted[0]):
            # Query lane and parking data 
            parking = Parking.query.filter(
                and_(
                    Parking.location == lane.lane,
                    Parking.end == None
                )
            ).first()

            # get the id
            _id = parking._id

            # generate qrcode to bse64 for web browser
            qrcode = from_string_to_base64(_id)
            return render_template("ticket.html", _id=qrcode, ticket_num=_id, park=parking)
        return redirect(url_for("not_found"))
    return redirect(url_for("not_found"))

@app.route("/scanned/<ticket_id>", methods=["GET"])
def scanned(ticket_id):
    ticket_status = ""
    ticket_price = None

    # query for the lane location
    ticket = Parking.query.filter(
        and_(
            Parking._id == ticket_id,
            Parking.end == None
        )
    ).first()

    # if the ticket is not found
    if not ticket:
        ticket_status = "Ticket Not Found"

    try:
        lane_info = LaneId.query.filter(LaneId.lane==ticket.location).first()

        # if found
        # change get the addon and base price
        add_on_price = lane_info.add_on
        base_price = lane_info.base_price
        now = get_date()

        # changing the end and payment from null to
        # number
        start_parking = ticket.park
        service_price = service_parking[ticket.service]
        parking_price = calculate_money(start_parking, now, base_price, add_on_price, service_price)
        ticket.end = now
        ticket.payment = parking_price
        ticket.encryption = ""

        # commit the database
        db.session.commit()
        ticket_price = parking_price
    except:
        pass

    return render_template("result.html", status=ticket_status, price=ticket_price, lane=ticket.location)

@app.route("/chischort/authentication/login", methods=["GET", "POST"])
def login():
    args = request.args.get("type")
    # login for the security
    if request.method == "POST":
        # get the form input
        username = request.form["username"]
        password = request.form["password"]

        # if match the user given
        if username == "chis" and password == "chort":
            session["user"] = "admin"
            if args == "scanner":
                return redirect(url_for("scanner"))
            return redirect(url_for("addlane"))
    return render_template("login.html")

@app.route("/scanner", methods=["GET"])
def scanner():
    # get the session from the login
    # if not login, we will not given the authorization
    # and return redirect to the login page
    if not session.get("user"):
        return redirect(url_for("home"))
    return render_template("scanner.html")

@app.route("/chischort/addlane", methods=["GET", "POST"])
def addlane():
    admin = session.get("user")
    lane_added = False
    if not admin:
        return redirect(url_for("login"))
    if request.method == "POST":
        lane_name = request.form["lane"]
        base_price = request.form["price"]
        add_on = request.form["add"]
        place = request.form["place"]
        multiple = request.form.get("numberplace")
        if multiple:
            continue_lane(db, LaneId, lane_name, multiple, base_price, add_on, place)
        else:
            lane = LaneId(lane_name, base_price, add_on, place)
            add_to_database(db, lane)
        lane_added = True
        return redirect(url_for("display"))
    return render_template("add-lane.html", added=lane_added)

@app.route("/chischort/display/lane", methods=["GET"])
def display():
    admin = session.get("user")
    query = request.args.get("search")
    parking_lane = LaneId.query.order_by(LaneId.lane_id).all()
    if query:
        parking_lane = LaneId.query.filter(LaneId.place == query).all()
    if not admin:
        return redirect(url_for("home"))
    return render_template("display.html", lane=parking_lane)
    
@app.route("/not_found", methods=["GET"])
def not_found():
    return render_template("404.html")

@app.route("/lane_used", methods=["GET"])
def lane_used():
    return render_template("lane_used.html")
