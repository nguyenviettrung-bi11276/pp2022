import math
import numpy as np
num = 0

class Student():
    def __init__(self, i, n, d):
        self._sid = i
        self._name = n
        self._dob = d
        self._mark = {}

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

class Course():
    def __init__(self, i, n):
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

class Sys():
    def __init__(self):
        self.std = list()
        self.crs  = list()

    def input_Std(self):
        numStudent = int(input("Enter number of students: "))
        for i in range(numStudent): 
            sid = input("Student ID: ")
            sname = input("Name: ")
            sdob = input("Date of Birth: ")

            snew = Student(sid, sname. sdob)
            self.std.append(snew)

    def output_Std(self):
        for i in self.std():
            print("\n\n   Student ID: " + i.get_sid())
            print("     Name: " + i.get_name())
            print("     DoB: " + str(i.get_dob()))

    def sort(self):
        getlist = []
        for i in self.std:
            getlist.append((i.get_sid(), ))
    
    def input_Crs(self):
        numCourse = int(input("Input number of courses: "))
        for i in range(numCourse):
            name = input("Input course's name: ")
            cid = input("Input course's id: ")
            cnew = Course(name, cid)
            self.crs.append(cnew)

    def output_Crs(self):
        for i in self.crs():
            print("\n\n    Course ID " + i.get_cid())
            print("     Name: " + i.get_name())

    def validate_StudentID(self):
        pass 
    def validate_CourseID(self):
        pass

    def input_Mark(self):
        for i in self.std():
            cinput = input("Input the mark: ")
            cmark = math.floor(float(cinput)*10)/10
            self._mark.append(cmark)

    def putput_Mark(self):
        pass
    def gpa(self):
        pass
    def sorting(self):
        pass

def main():
    while True:    
        print("1. Add students.")
        print("2. Add courses.")
        print("3. Add marks for a course.")
        print("4. Show all students.")
        print("5. Show all courses.")
        print("6. Show marksheet.")
        choice = input()
        if choice == "":
            return -1
        else:
            return int(choice)
        
        if choice == 1:
            add_std()
        elif choice == 2:
            add_course()
        elif choice == 3:
            add_marks()
        elif choice == 4:
            show_std()
        elif choice == 5:
            show_courses()
        elif choice == 6:
            show_marks()
        else:
            exit()   
    return
    
if __name__ == '__main__':
    main()
    
