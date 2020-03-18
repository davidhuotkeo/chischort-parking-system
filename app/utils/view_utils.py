import qrcode
from io import BytesIO
import base64
from datetime import datetime
from cryptography.fernet import Fernet
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from .file import social

def from_string_to_base64(string, img_only=False):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(string)
    qr.make(fit=True)
    stream_object = BytesIO()
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(stream_object, format="JPEG")
    jpg_value = stream_object.getvalue()
    if img_only:
        return jpg_value
    base64_jpg = base64.b64encode(jpg_value)
    src = "data:image/jpeg;base64, " + base64_jpg.decode()
    return src

def calculate_money(start:datetime, end:datetime, base_price, add_on, service_price):
    hours = (end - start).seconds // 3600
    if hours == 0:
        return base_price + service_price
    add_on_price_overall = (hours - 1) * add_on
    price = base_price + add_on_price_overall + service_price
    return price

def encrypt_cipher(value:str):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    token = fernet.encrypt(value.encode())
    return key.decode(), token.decode()

def encrypt_with_key(key, value):
    fernet = Fernet(key.encode())
    token = fernet.encrypt(value.encode())
    return token.decode()

def decrypt_cipher(key, encrypted_value):
    fernet = Fernet(key.encode())
    decrypted_string = fernet.decrypt(encrypted_value.encode())
    return decrypted_string.decode()

def send_email(email, _id, message):
    company_email = social["email"]
    company_password = social["password"]

    msg = MIMEMultipart()

    msg['Subject'] = "ChisChort Parking Ticket"
    msg['From'] = company_email
    msg['To'] = email

    text = MIMEText(message, "html")
    msg.attach(text)

    image = from_string_to_base64(_id, img_only=True)
    image = MIMEImage(image, name="chischort-parking-qrcode.jpeg")
    msg.attach(image)

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)

    try:
        server.ehlo()
        server.login(company_email, company_password)
        server.sendmail(company_email, email, msg.as_string())
    except:
        print("sth wrong")
