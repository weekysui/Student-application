# import necessary libraries
import numpy as np
from flask import (
    Flask,
    render_template,
    jsonify,
    request)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Database Setup
#################################################

from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite"

db = SQLAlchemy(app)

class Students(db.Model):
    __tablename__ = 'students'

    num = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    grade = db.Column(db.Integer)
    school = db.Column(db.String(64))
    gender = db.Column(db.String(64))
    birthday = db.Column(db.String(64))
    gpa = db.Column(db.Integer)
    address = db.Column(db.String())
    phone = db.Column(db.String())


    def __repr__(self):
        return '<Pet %r>' % (self.nickname)


@app.before_first_request
def setup():
    # Recreate database each time for demo
    db.drop_all()
    db.create_all()


#################################################
# Routes
#################################################

# @app.route("/send", methods=["GET", "POST"])
# def send():
#     if request.method == "POST":
#         name = request.form["name"]
#         grade = request.form["grade"]
#         school = request.form["school"]
#         gender = request.form["gender"]
#         birthday = request.form["birthday"]
#         gpa = request.form["gpa"]
#         address = request.form["address"]
#         phone = request.form["phone"]


#         student = Students(
#             name=name, 
#             grade = grade, 
#             school = school, 
#             gender = gender, 
#             birthday = birthday,
#             gpa=gpa,
#             address=address,
#             phone=phone)
#         db.session.add(student)
#         db.session.commit()

#         return "Thanks for the form data!"

#     return render_template("form.html")


# @app.route("/pets")
# def list_pets():
#     results = db.session.query(Pet.nickname, Pet.age).all()

#     pets = []
#     for result in results:
#         pets.append({
#             "nickname": result[0],
#             "age": result[1]
#         })
#     return jsonify(pets)


@app.route("/",methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]
        grade = request.form["grade"]
        school = request.form["school"]
        gender = request.form["gender"]
        birthday = request.form["birthday"]
        gpa = request.form["gpa"]
        address = request.form["address"]
        phone = request.form["phone"]


        student = Students(
            name=name, 
            grade = grade, 
            school = school, 
            gender = gender, 
            birthday = birthday,
            gpa=gpa,
            address=address,
            phone=phone)
        db.session.add(student)
        db.session.commit()

        return "Thanks for the form data!"

    return render_template("form.html")

if __name__ == "__main__":
    app.run()
