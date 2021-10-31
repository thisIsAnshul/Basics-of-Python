def getPupilsFromDb(mydb):
    mycursor = mydb.cursor()
    sql = 'SELECT * FROM pupil'
    mycursor.execute(sql)
    results = mycursor.fetchall()
    return results