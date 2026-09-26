
class Course:

    def __init__(self, course_id, course_code, course_name, credit_hours, department_id):
        self.course_id = course_id
        self.course_code = course_code
        self.course_name = course_name
        self.credit_hours = credit_hours
        self.department_id = department_id

    @property
    def course_id(self):
        return self.__course_id

    @property
    def course_code(self):
        return self.__course_code

    @property
    def course_name(self):
        return self.__course_name
    
    @property
    def credit_hours(self):
        return self.__credit_hours
    
    @property
    def department_id(self):
        return self.__department_id

    @course_id.setter
    def course_id(self, course_id):
        self.__course_id = course_id
        
    @course_code.setter
    def course_code(self, course_code):
        self.__course_code = course_code

    @course_name.setter
    def course_name(self, course_name):
        self.__course_name = course_name
    
    @credit_hours.setter
    def credit_hours(self, credit_hours):
        self.__credit_hours = credit_hours

    @department_id.setter
    def department_id(self, department_id):
        self.__department_id = department_id

    def __str__(self):
        return f"|Course ID      : {self.course_id}\n|Course Code    : {self.course_code}\n|Course Name    : {self.course_name}\n|Credit Hours   : {self.credit_hours}\n|Department     : {self.department_id}\n\n"


