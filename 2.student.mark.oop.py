num = 0

class Student():
    def _init_(self, i, n, d):
        self._sid = i
        self._name = n
        self._dob = d

    def set_sid(self, i):
        self._sid = i
    def set_name(self, n):
        self._name = n
    def set_dob(self, d):
        self._dob = d

    def get_sid(self):
        return self._sid
    def get_name(self):
        return self._name
    def get_dob(self):
        return self._dob

class In4S():
    def _init_(self):
        self.std = list()

    def input(self):
        numStudent = int(input("Enter number of students: "))
        for i in range(numStudent): 
            sid = input("Student ID: ")
            sname = input("Name: ")
            sdob = input("Date of Birth: ")

            snew = Student(sid, sname. sdob)
            self.std.append(snew)

    def output(self):
        for i in self.std():
            print("\n\n   Student ID: " + i.get_sid())
            print("     Name: " + i.get_name())
            print("     DoB: " + str(i.get_dob()))

class Course():
    def _init_(self, i, n):
        self._cid = i
        self._name = n

    def set_cid(self, i):
        self._cid = i
    def set_name(self, n):
        self._name = n

    def get_cid(self):
        return self._cid
    def get_name(self):
        return self._name

class In4C():
    def _init_(self):
        self._crs = list()
    
    def input(self):
        numCourse = int(input("Input number of courses: "))
        for i in range(numCourse):
            name = input("Input course's name: ")
            cid = input("Input course's id: ")
            cnew = Course(name, cid)
            self._crs.append(cnew)

    def output(self):
        for i in self.crs():
            print("\n\n    Course ID " + i.get_cid())
            print("     Name: " + i.get_name())

class Mark():

    def _init_(self, cid, sid, m: float):
        self._cid = cid
        self._sid = sid
        self._mark = m

    def set_cid(self, i):
        self._cid = i
    def set_mark(self, m: float):
        self._mark = m
    def set_sid(self, i):
        self._sid = i

    def get_cid(self):
        return self._cid
    def get_mark(self):
        return self._mark
    def get_sid(self):
        return self._sid

    
