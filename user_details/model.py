from sqlalchemy import Boolean
from sqlalchemy.dialects.postgresql import NUMRANGE

from __init__ import app, db
# from sqlalchemy.testing import db


class User(db.Model):
    __tablename__ = "user_details2"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50), nullable=False)
    photo = db.Column(db.String(255),nullable = True)  # Adjusted to store file paths
    mobile_no = db.Column(db.String(15), nullable=False)
    company_id = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<id{self.user_id}>"

    def save(self):
        db.session.add(self)
        db.session.commit()


class Technical(db.Model):
    __tablename__ = "Technical_details"
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(50), nullable=False)
    manufacture_name = db.Column(db.String(100), nullable=False)
    manufacture_model_no = db.Column(db.String(100), nullable=False)
    expiry_date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f"<id{self.user_id}>"

    def save(self):
        db.session.add(self)
        db.session.commit()


class Modules(db.Model):
    __tablename__ = "Modules_table"
    id = db.Column(db.Integer, primary_key=True)
    module_name = db.Column(db.String(50), nullable=False)
    icons = db.Column(db.String(200), nullable=False)
    type = db.Column(db.String(100),nullable=False)

    def __repr__(self):
        return f"<id{self.user_id}>"

    def save(self):
        db.session.add(self)
        db.session.commit()


class Manuals(db.Model):
    __tablename__ = "Manuals_table"
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(200),nullable=False)
    fileurl = db.Column(db.String(1000),nullable=False)

    def __repr__(self):
        return f"<id{self.user_id}>"

    def save(self):
        db.session.add(self)
        db.session.commit()


class Machine_form(db.Model):
    __tablename__ = "Machine_details"
    id = db.Column(db.Integer, primary_key=True)
    machine_id = db.Column(db.String(100),nullable=False)
    machine_name = db.Column(db.String(150),nullable=False)
    model_no = db.Column(db.String(300),nullable=False)
    gateway_id = db.Column(db.String(200),nullable=False)
    manual = db.Column(db.String(300),nullable=False)
    technical_table = db.Column(db.String(500),nullable=False)
    io_group_id = db.Column(db.String(100),nullable=False)


    def __repr__(self):
        return f"<id{self.user_id}>"

    def save(self):
        db.session.add(self)
        db.session.commit()


class Layers(db.Model):
    __tablename__ = "Layers_table"
    id = db.Column(db.Integer,primary_key=True)
    layer_type = db.Column(db.String(200),nullable=False)
    layer_name = db.Column(db.String(200),nullable=False)
    company_logo = db.Column(db.String(500),nullable=False)
    location = db.Column(db.String(500),nullable=False)

    def __repr__(self):
        return f"<id{self.user_id}>"

    def save(self):
        db.session.add(self)
        db.session.commit()

class Cards(db.Model):
    __tablename__ = "Cards_table"
    id = db.Column(db.Integer,primary_key=True)
    card_type = db.Column(db.String(299),nullable=False)

    def __repr__(self):
        return f"<id{self.user_id}>"

    def save(self):
        db.session.add(self)
        db.session.commit()



class Machine(db.Model):
    __tablename__ = "Machine_table"
    id = db.Column(db.Integer, primary_key=True)
    machine_id = db.Column(db.String(299),nullable=False)
    kpi_name = db.Column(db.String(299),nullable=False)
    datapoints = db.Column(db.String(299),nullable=False)
    mode = db.Column(db.String(299),nullable=False)
    conversion = db.Column(db.String(299),nullable=False)
    x_label = db.Column(db.String(299),nullable=False)
    y_label = db.Column(db.String(299),nullable=False)
    ledger = db.Column(db.String(299),nullable=False)
    title = db.Column(db.String(299),nullable=False)
    card_type = db.Column(db.String(299),nullable=False)
    unit = db.Column(db.String(299),nullable=False)


    def __repr__(self):
        return f"<id{self.user_id}>"


    def save(self):
        db.session.add(self)
        db.session.commit()


class Iodata(db.Model):
    __tablename__ = 'io_data'

    id = db.Column(db.Integer, primary_key=True)
    io_group = db.Column(db.String(100), nullable=False)
    io_type = db.Column(db.String(100), nullable=False)
    io_name = db.Column(db.String(100), nullable=False)
    io_value = db.Column(db.String(100), nullable=False)
    io_color = db.Column(db.String(50), nullable=False)
    io_range = db.Column(db.Float, nullable=False)
    io_unit = db.Column(db.String(50), nullable=False)
    control = db.Column(Boolean, nullable=False, default=False)  # Radio button (True/False)
    alarm = db.Column(Boolean, nullable=False, default=False)  # Radio button (True/False)

    def __repr__(self):
        return f"<IOData {self.io_name}>"


    def save(self):
        db.session.add(self)
        db.session.commit()



with app.app_context():
    db.create_all()
