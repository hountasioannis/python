import sys
import config
sys.path.append(config.APP_PATH)
from abc import ABC, abstractmethod
from dao.exceptions import teacher_dao_exception
from service.db_util import mysql


class ABCTeacherDAO(ABC):

    @abstractmethod
    def insert( firstname, lastname):
        pass

    @abstractmethod
    def update(id , firstname, lastname):
        pass

    @abstractmethod
    def delete( id):
        pass

    @abstractmethod
    def get_by_lastname(lastname):
        pass

    @abstractmethod
    def get_by_id( id):
        pass


class TeacherDAOImpl(ABCTeacherDAO):
     
     
     def insert(firstname, lastname):
        try:
            cursor = mysql.conn.cursor()
            cursor.execute("SELECT MAX(ID) FROM TEACHERS")
            id = cursor.fetchone()[0] + 1
            cursor.execute("INSERT INTO TEACHERS (ID, FIRSTNAME, LASTNAME) VALUES (%s, %s, %s)", (id, firstname, lastname)) 
            mysql.conn.commit()
            cursor.close()
            return "teacher was inserted"
        except mysql.mysql.connector.Error:
            raise teacher_dao_exception.TeacherDaoError("error in inserting teacher")
            
            

     
     def update(id, firstname, lastname):
        try:
            cursor = mysql.conn.cursor()
            cursor.execute("UPDATE TEACHERS SET FIRSTNAME = %s, LASTNAME = %s WHERE ID = %s", (firstname, lastname, id)) 
            mysql.conn.commit()
            cursor.close()
            return "teacher was updated"
        except mysql.mysql.connector.Error:
            raise teacher_dao_exception.TeacherDaoError("error in updating teacher")
     
     def delete(id):
        try:
            cursor = mysql.conn.cursor()
            cursor.execute("DELETE FROM TEACHERS WHERE ID = %s", [(id)]) 
            mysql.conn.commit()
            cursor.close()
            
            return "teacher was deleted"
        except mysql.mysql.connector.Error:
            raise teacher_dao_exception.TeacherDaoError("error in updating teacher")
     
     def get_by_lastname(lastname):
        try:
            cursor = mysql.conn.cursor()
            cursor.execute("SELECT ID, FIRSTNAME, LASTNAME FROM TEACHERS WHERE LASTNAME = %s", [(lastname)])
            results = cursor.fetchall()
            mysql.conn.commit()
            cursor.close()
            
            return results
        except mysql.mysql.connector.Error:
            raise teacher_dao_exception.TeacherDaoError("error in updating teacher") 
     
     def get_by_id(id):
        try:
            cursor = mysql.conn.cursor()
            cursor.execute("SELECT ID, FIRSTNAME, LASTNAME FROM TEACHERS WHERE ID = %s", [(id)]) 
            results = cursor.fetchall()
            mysql.conn.commit()
            cursor.close()
            
            return results
        except mysql.mysql.connector.Error:
            raise teacher_dao_exception.TeacherDaoError("error in updating teacher")
        