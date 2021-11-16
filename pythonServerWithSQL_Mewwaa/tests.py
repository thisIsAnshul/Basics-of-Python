import unittest
import os
import mysql
import mysql.connector
import mock
from utils import getPupilsFromDb

mydb = None

class TestGetPupils(unittest.TestCase): 


    def testGetPupilsFromDb(self): 
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="zadPy"
        )
        result = getPupilsFromDb(mydb)
        self.assertEqual(15,len(result))

    
    @mock.patch("utils.getPupilsFromDb", return_value=['dasdas','dsadsads'] )
    def testGetPupilsFromDbMocked(self, mocked_get_pupils): 
        result = mocked_get_pupils.return_value
        self.assertEqual(2,len(result) )


if __name__ == '__main__': 
    unittest.main()