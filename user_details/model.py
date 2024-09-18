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


with app.app_context():
    db.create_all()
