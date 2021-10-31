# Author: Ewa Zalewska
# Concept: simple server in python using SQL database
# Github: https://github.com/Mewwaa



from flask import Flask, redirect, url_for, jsonify 
app = Flask(__name__)
import mysql
import mysql.connector
import requests
import random

from utils import getPupilsFromDb

# Jeśli pojawi się błąd przy imporcie to ja użyłam tych komend:
# pip install Flask
# pip install mysqlclient
# pip install mysql-connector-python


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="zadPy"
)

# Pupil's endpoints
# -----------------------------------------------
@app.route('/addPupil/<name>/<surname>/<pesel>/<class_name>') # localhost:3000/addPupil/Ewa/Zalewska/1234/2PUp
def addPupil(name, surname, pesel, class_name):
    mycursor = mydb.cursor(buffered=True)
    checkIfPupilExists = "Select * from pupil where pupil.pesel={}".format(pesel)
    mycursor.execute(checkIfPupilExists)
    result = mycursor.fetchone()   
    if result is None:
        newPupil = "INSERT INTO pupil (name, surname, pesel, class) VALUES (%s, %s, %s, %s)"
        newPupilValues = (name, surname, pesel, class_name)
        mycursor.execute(newPupil, newPupilValues)   
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
        return jsonify(
            IMPORTANT="Pupil "+ name +" "+ surname+" added to database."
        )
    return jsonify(
        IMPORTANT="User "+ name +" "+ surname+" already exists in the database."
    )

@app.route('/showAllPupils') # localhost:3000/showAllPupils
def showAllPupils():
    results = getPupilsFromDb(mydb)
    for x in results:
        print(x)
    return jsonify(
        results,
    )

@app.route('/removeAllPupils') # localhost:3000/removeAllPupils
def removeAllPupils():
    mycursor = mydb.cursor()
    sqlQuery = "DELETE FROM pupil"
    mycursor.execute(sqlQuery)
    mydb.commit()
    print(mycursor.rowcount, "record deleted")
    return jsonify(
        IMPORTANT="All Pupils removed succesfully"
    )

@app.route('/removePupilById/<id>') # localhost:3000/removePupilById/1
def removePupilById(id):
    mycursor = mydb.cursor()
    sqlQuery = "DELETE FROM pupil WHERE pupil_id = {}".format(id)
    mycursor.execute(sqlQuery,id)
    mydb.commit()
    print(mycursor.rowcount, "record deleted")
    return jsonify(
        IMPORTANT="Pupil with id "+ id +" removed succesfully"
    )
# -----------------------------------------------

# Teacher's endpoints
# -----------------------------------------------
@app.route('/addTeacher/<name>/<surname>/<requestPesel>/<subject>') # localhost:3000/addTeacher/Agata/Kowalczyk/2222/Math
def addTeacher(name, surname, requestPesel, subject):
    mycursor = mydb.cursor()
    newTeacher = "INSERT INTO teacher (name, surname, pesel, subject) VALUES (%s, %s, %s, %s)" 
    newTeacherValues = (name, surname, requestPesel, subject)
    mycursor.execute(newTeacher, newTeacherValues)   
    mydb.commit()
    print(mycursor.rowcount, " record successfully inserted.")
    return jsonify(
        IMPORTANT="Teacher "+ name +" "+ surname+" added to database.",
    )

@app.route('/showAllTeacher') # localhost:3000/showAllTeacher
def showAllTeacher():
    mycursor = mydb.cursor()
    sql = 'SELECT * FROM Teacher'
    mycursor.execute(sql)
    results = mycursor.fetchall()
    for x in results:
        print(x)
    return jsonify(
        IMPORTANT='All teachers showed'
    )
    
@app.route('/removeAllTeachers') # localhost:3000/removeAllTeachers
def removeAllTeachers():
    mycursor = mydb.cursor()
    sqlQuery = "DELETE FROM teacher"
    mycursor.execute(sqlQuery)
    mydb.commit()
    print(mycursor.rowcount, "record deleted")
    return jsonify(
        IMPORTANT="All teachers removed succesfully"
    )

@app.route('/removeTeacherById/<id>') # localhost:3000/removeTeacherById/1
def removeTeacherById(id):
    mycursor = mydb.cursor()
    sqlQuery = "DELETE FROM teacher WHERE teacher_id = {}".format(id)
    mycursor.execute(sqlQuery,id)
    mydb.commit()
    print(mycursor.rowcount, "record deleted")
    return jsonify(
        IMPORTANT="Teacher with id "+ id +" removed succesfully"
    )
# -----------------------------------------------

# Subject's endpoints
# -----------------------------------------------
@app.route('/addSubject/<id>/<name>') # localhost:3000/addSubject/2/Math
def addSubject(id,name ):
    mycursor = mydb.cursor()
    newSubject = "INSERT INTO Subject (subject_id, name) VALUES (%s, %s)"
    newSubjectValues = (id, name)
    mycursor.execute(newSubject, newSubjectValues)   
    mydb.commit()
    print(mycursor.rowcount, " record inserted.")
    return jsonify(
        IMPORTANT="Subject with id "+ id +" added to database. If there is an error change id then try again"
    )

@app.route('/showAllSubjects') # localhost:3000/showAllSubjects
def showAllSubjects():
    mycursor = mydb.cursor()
    sql = 'SELECT * FROM Subject'
    mycursor.execute(sql)
    results = mycursor.fetchall()
    for x in results:
        print(x)
    return jsonify(
        IMPORTANT='All subjects showed'
    )

@app.route('/removeSubjectById/<id>') # localhost:3000/removeSubjectById/1
def removeSubjectById(id):
    mycursor = mydb.cursor()
    sqlQuery = "DELETE FROM subject WHERE subject_id = {}".format(id)
    mycursor.execute(sqlQuery,id)
    mydb.commit()
    print(mycursor.rowcount, "record deleted")
    return jsonify(
        IMPORTANT="Subject with id "+ id +" removed succesfully"
    )

@app.route('/removeAllSubjects') # localhost:3000/removeAllSubjects
def removeAllSubjects():
    mycursor = mydb.cursor()
    sqlQuery = "DELETE FROM subject"
    mycursor.execute(sqlQuery)
    mydb.commit()
    print(mycursor.rowcount, "record deleted")
    return jsonify(
        IMPORTANT="All subjects removed succesfully"
    )
# -----------------------------------------------

# Pupil_Subject's endpoints
# -----------------------------------------------
@app.route('/addPupilSubject/<pupil_id>/<subject_id>') # localhost:3000/addPupilSubject/1/1
def addPupilSubject(pupil_id, subject_id):
    mycursor = mydb.cursor()
    newPupilSubject = "INSERT INTO Pupil_Subject (pupil_id, subject_id) VALUES (%s, %s)"
    newPupilSubjectValues = (pupil_id, subject_id)
    mycursor.execute(newPupilSubject, newPupilSubjectValues)   
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    return jsonify(
        IMPORTANT= "Pupil with id " +pupil_id + " added to subject successfully",
    )

@app.route('/showAllPupilsSubjects') # localhost:3000/showAllPupilsSubjects
def showAllPupilsSubjects():
    mycursor = mydb.cursor()
    sql = 'SELECT * FROM Pupil_Subject'
    mycursor.execute(sql)
    results = mycursor.fetchall()
    for x in results:
        print(x)
    return jsonify(
        IMPORTANT='All pupil_subjects showed'
    )

@app.route('/removeAllPupilsSubjects') # localhost:3000/removeAllPupilsSubjects
def removeAllPupilsSubjects():
    mycursor = mydb.cursor()
    sqlQuery = "DELETE FROM Pupil_Subject"
    mycursor.execute(sqlQuery)
    mydb.commit()
    print(mycursor.rowcount, "record deleted")
    return jsonify(
        IMPORTANT="All pupil_subjects removed succesfully"
    )
# -----------------------------------------------

# Pupil_Teacher's endpoints
# -----------------------------------------------
@app.route('/addPupilTeacher/<pupil_id>/<teacher_id>') # localhost:3000/addPupilTeacher/1/1
def addPupilTeacher(pupil_id, teacher_id):
    mycursor = mydb.cursor()
    newPupilteacher = "INSERT INTO Pupil_Teacher (pupil_id, teacher_id) VALUES (%s, %s)"
    newPupilteacherValues = (pupil_id, teacher_id)
    mycursor.execute(newPupilteacher, newPupilteacherValues)   
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    return jsonify(
        IMPORTANT ="Pupil with id "+ pupil_id + " added successfully to teacher"
    )

@app.route('/showAllPupilTeachers') # localhost:3000/showAllPupilTeachers
def showAllPupilTeachers():
    mycursor = mydb.cursor()
    sql = 'SELECT * FROM Pupil_Teacher'
    mycursor.execute(sql)
    results = mycursor.fetchall()
    for x in results:
        print(x)
    return jsonify(
        IMPORTANT='All Pupil_Teachers showed'
    )

@app.route('/removeAllPupilTeachers') # localhost:3000/removeAllPupilTeachers
def removeAllPupilTeachers():
    mycursor = mydb.cursor()
    sqlQuery = "DELETE FROM Pupil_Teacher"
    mycursor.execute(sqlQuery)
    mydb.commit()
    print(mycursor.rowcount, "record deleted")
    return jsonify(
        IMPORTANT="All Pupil_Teacher removed succesfully"
    )
# -----------------------------------------------

if __name__ == "__main__":
    app.run("localhost", 3000, True, {})