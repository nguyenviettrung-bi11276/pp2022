num = 0
std_list = list() 
crs = list() 

def add_std():
    print("Imput number of students: ")
    num = int(input())
    for i in range(num):
        s_id = 0
        s_name = 0
        dob = 'i'
        print("Student " + str(i+1) + "th:")
        s_id = input("ID: ")            
        s_name = input("Name: ")
        dob = input("DoB - Day: ")
        new_s = {
            "id": s_id,
            "name": s_name,
            "dob": dob,
            "marks": list()
        }
        list.append(new_s)
    
def add_course():
    crs_id = input("Input course id: ")
    crs_name = input("Input course name: ")
    course = {
        "id": crs_id,
        "name": crs_name
    }
    crs.append(course)
    print("Done.")

def add_marks():
    crs_id = input("Input course id: ")
    crs_result = "";
    crs_display = "";
    for item in crs:
        if item["id"] == crs_id:
            crs_result = item["id"]
    print("Course: " + crs_display.upper())
    #print("Input mark for ", end='')
        
def show_std():
    for item in std_list:
        print("----- STUDENT ID " + item["id"] + " -----")
        print("Name: " + item["name"])
        print("DoB: " + item["dob"])

def show_courses():
    for item in crs:
        print("----- COURSES ID " + item["id"] + " -----")
        print("Name: " + item["name"])

def show_marks():
    crs_id = input("Input course id or name: ")
    crs_result = "";
    for item in crs:
        if item["id"] == crs_id:
            crs_result = item["id"]
    if crs_result == "":
        print("Course not found!!!")
        return
    print("Mark: ")
    for info in std_list:
        for markss in info["marks"]:
            if markss["course_id"] == crs_result:
                print(info["id"] + ", " + info["name"] + ": " + str(markss["mark"]))

def menu(choice):
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

def choice():
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
while True:
    menu(choice())
