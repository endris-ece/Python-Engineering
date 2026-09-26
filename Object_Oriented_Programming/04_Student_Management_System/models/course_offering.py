

class CourseOffering:

    def __init__(self, offering_id, course_id, semester, academic_year, capacity):
        self.offering_id = offering_id
        self.course_id = course_id
        self.semester = semester
        self.academic_year = academic_year
        self.capacity = capacity
    
    @property
    def offering_id(self):
        return self.__offering_id
    
    @property
    def course_id(self):
        return self.__course_id

    @property
    def semester(self):
        return self.__semester

    @property
    def academic_year(self):
        return self.__academic_year

    @property
    def capacity(self):
        return self.__capacity

    @offering_id.setter
    def offering_id(self, offering_id):
        self.__offering_id = offering_id

    @course_id.setter
    def course_id(self, course_id):
        self.__course_id = course_id
        
    @semester.setter
    def semester(self, semester):
        self.__semester = semester

    @academic_year.setter
    def academic_year(self, academic_year):
        self.__academic_year = academic_year

    @capacity.setter
    def capacity(self, capacity):
        self.__capacity = capacity
    
    def __str__(self):
        return f"Offering ID      : {self.offering_id}\nCourse ID        : {self.course_id}\nSemester         : {self.semester}\nAcademic Year    : {self.academic_year}\nCapacity         : {self.capacity}\n\n"
    
    
    
    
    
    
    
    
    