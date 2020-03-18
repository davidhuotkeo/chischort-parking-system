from app import app
from app.models.database import db, Parking
import pymysql

if __name__ == "__main__":
    pymysql.install_as_MySQLdb()
    db.create_all()
    app.run(host="0.0.0.0")
    