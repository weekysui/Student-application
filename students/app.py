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
    name = db.Column(db.String(64), nullable=False)
    grade = db.Column(db.Integer)
    school = db.Column(db.String(64))
    gender = db.Column(db.String(64))
    birthday = db.Column(db.String(64))
    gpa = db.Column(db.Integer)
    address = db.Column(db.String())
    phone = db.Column(db.String())
    mom = db.Column(db.String(64))
    momcell = db.Column(db.String())
    momemail = db.Column(db.String())
    dad = db.Column(db.String(64))
    dadcell = db.Column(db.String())
    dademail = db.Column(db.String())
    aciE = db.Column(db.String())
    aciM = db.Column(db.String())
    

    # ,nullable=False



    def __repr__(self):
        return '<Pet %r>' % (self.nickname)


@app.before_first_request
def setup():
    # Recreate database each time for demo
    # db.drop_all()
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


@app.route("/list")
def list_students():
    results = db.session.query(
        Students.name, 
        Students.grade, 
        Students.school, 
        Students.gender, 
        Students.birthday, 
        Students.gpa, 
        Students.address, 
        Students.phone,
        Students.mom,
        Students.momcell,
        Students.momemail,
        Students.dad,
        Students.dadcell,
        Students.dademail,
        Students.aciE,
        Students.aciM
       ).all()
    #     Students.aciEnglish,
        # Students.aciMath

    # students = []
    # for result in results:
    #     students.append({
    #         "Student's name": result[0],
    #         "grade": result[1],
    #         "School":result[2],
    #         "gender":result[3]
    #     })
    return render_template("list.html",results = results) 
    # jsonify(students)


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
        mom = request.form["mom"]
        momcell = request.form["momcell"]
        momemail = request.form["momemail"]
        dad = request.form["dad"]
        dadcell = request.form["dadcell"]
        dademail = request.form["dademail"]
        aciE = request.form["aciE"]
        aciM = request.form["aciM"]
        


        student = Students(
            name=name, 
            grade = grade, 
            school = school, 
            gender = gender, 
            birthday = birthday,
            gpa=gpa,
            address=address,
            phone=phone,
            mom = mom,
            momcell = momcell,
            momemail = momemail,
            dad = dad,
            dadcell = dadcell,
            dademail = dademail,
            aciE = aciE,
            aciM = aciM)
           
        db.session.add(student)
        db.session.commit()

        return "Thanks for the form data!"

    return render_template("form.html")

if __name__ == "__main__":
    app.run()
