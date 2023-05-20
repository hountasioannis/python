import sys
import config
sys.path.append(config.APP_PATH)
from abc import ABC, abstractmethod
from service.exceptions import teacher_not_found_exception
from dao import teacher_dao


class ABCTeacherService(ABC):

    @abstractmethod
    def insert_teacher(firstname, lastname):
        pass

    @abstractmethod
    def update_teacher(id , firstname, lastname):
        pass

    @abstractmethod
    def delete_teacher(id):
        pass

    @abstractmethod
    def get_teacher_by_lastname(lastname):
        pass

    @abstractmethod
    def get_teacher_by_id( id):
        pass

class TeacherServiceImpl(ABCTeacherService):

    def insert_teacher( firstname, lastname):
        try:
            return teacher_dao.TeacherDAOImpl.insert( firstname, lastname)
        except teacher_dao.teacher_dao_exception.TeacherDaoError as e:
            print(e)
    
    def update_teacher( id, firstname, lastname):
            try:
                if teacher_dao.TeacherDAOImpl.get_by_id(id):
                    return teacher_dao.TeacherDAOImpl.update(id, firstname, lastname)
                else:
                    return teacher_not_found_exception.TeacherNotFoundError()
            except (teacher_dao.teacher_dao_exception.TeacherDaoError, teacher_not_found_exception.TeacherNotFoundError) as e:
                print(e)

    def delete_teacher(id):
            try:
                if teacher_dao.TeacherDAOImpl.get_by_id(id):
                    return  teacher_dao.TeacherDAOImpl.delete(id)
                else:
                     return teacher_not_found_exception.TeacherNotFoundError() 
            except (teacher_dao.teacher_dao_exception.TeacherDaoError, teacher_not_found_exception.TeacherNotFoundError) as e:
                print(e)
            
    
    def get_teacher_by_lastname(lastname):
            try:
                if teacher_dao.TeacherDAOImpl.get_by_lastname(lastname):
                    results = teacher_dao.TeacherDAOImpl.get_by_lastname(lastname)
                    return results
                else:
                    return teacher_not_found_exception.TeacherNotFoundError()  
            except (teacher_dao.teacher_dao_exception.TeacherDaoError, teacher_not_found_exception.TeacherNotFoundError) as e:
                print(e)
            
    def  get_teacher_by_id(id):
        try:
            if teacher_dao.TeacherDAOImpl.get_by_id(id):
                return  teacher_dao.TeacherDAOImpl.get_by_id(id)
            else:
                return teacher_not_found_exception.TeacherNotFoundError() 
        except (teacher_dao.teacher_dao_exception.TeacherDaoError, teacher_not_found_exception.TeacherNotFoundError) as e:
                print(e)

