

class Enrollment:

    def __init__(self, enrollment_id, student_id, offering_id, grade, status):
        self.enrollment_id = enrollment_id
        self.student_id = student_id
        self.offering_id = offering_id
        self.grade = grade
        self.status = status

    @property
    def enrollment_id(self):
        return self.__enrollment_id

    @property
    def student_id(self):
        return self.__student_id

    @property
    def offering_id(self):
        return self.__offering_id

    @property
    def grade(self):
        return self.__grade

    @property
    def status(self):
        return self.__status
    
    @enrollment_id.setter
    def enrollment_id(self, enrollment_id):
        self.__enrollment_id = enrollment_id
        
    @student_id.setter
    def student_id(self, student_id):
        self.__student_id = student_id

    @offering_id.setter
    def offering_id(self, offering_id):
        self.__offering_id = offering_id
    
    @grade.setter
    def grade(self, grade):
        self.__grade = grade

    @status.setter
    def status(self, status):
        self.__status = status

    def __str__(self):
        return f"|Enrollment ID     : {self.enrollment_id}\n|Student ID        : {self.student_id}\n|Offering ID       : {self.offering_id}\n|Grade             : {self.grade}\n|Status            : {self.status}\n\n" 



