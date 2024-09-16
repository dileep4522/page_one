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

with app.app_context():
    db.create_all()
