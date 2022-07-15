import pickle
import os

"""
class used
"""


class student(object):
    def __int__(s):
        s.roll = 0
        s.name = " "
        s.Database = 0
        s.programming = 0
        s.security = 0
        s.digital_designs = 0
        s.web_development = 0
        s.total = 0
        s.per = 0
        s.grade = " "

    def add_rec(s):
        s.roll = int(input("Enter roll no"))
        s.name = input("Enter the name")
        s.name = s.name.upper()
        s.Database = float(input("Enter marks of Database"))
        s.programming = float(input("Enter marks of programming"))
        s.security = float(input("Enter marks of security"))
        s.digital_designs = float(input("Enter marks of digital_designs"))
        s.web_development = float(input("Enter marks of web_development"))
        s.total = s.Database + s.programming + s.security + s.digital_designs + s.web_development
        s.per = s.total / 5
        if (s.per >= 90):
            s.grade = "A1"
        elif (s.per >= 80 and s.per < 90):
            s.grade = "A2"
        elif (s.per >= 70 and s.per < 80):
            s.grade = "B1"
        elif (s.per >= 60 and s.per < 70):
            s.grade = "B2"
        else:
            s.grade = "C"

    def disp_rec(s):
        print("roll", s.roll)
        print("name", s.name)
        print("Database", s.Database)
        print("programming", s.programming)
        print("security", s.security)
        print("digital_designs", s.digital_designs)
        print("web_development", s.web_development)
        print("total", s.total)
        print("per", s.per)
        print("grade", s.grade)

    def display_rec(s):
        print("%-8s" % s.roll, "%-10s" % s.name, "%-10s" % s.Database, "%-12s" % s.programming, "%-10s" % s.security,
              "%-8s" % s.digital_designs, "%-10s" % s.web_development, "%-10s" % s.total, "%-10s" % s.per,
              "%-5s" % s.grade)
        # print("in display_rec")

    def modify_rec(s):
        s.roll = int(input("Enter new roll no"))
        s.name = input("Enter new name")
        s.name = s.name.upper()
        s.Database = float(input("Enter new marks of Database"))
        s.programming = float(input("Enter new marks of programming"))
        s.security = float(input("Enter new marks of security"))
        s.digital_designs = float(input("Enter new marks of digital_designs"))
        s.web_development = float(input("Enter new marks of web_development"))


def write_rec():
    try:
        rec = student()
        file = open("stud.dat", "ab")
        rec.add_rec()
        pickle.dump(rec, file)
        file.close()
        print("Record added in file")
        input("Press any key to cont....")
    except:
        pass


def display_all():
    os.system("cls")
    print(110 * "=")
    print("\n                                     RAMAKRISHNA VIDYA MANDIR                              \n")
    print("\n                           LIST OF MARKS OF STUDENTS OF CLASS XII OPTING PCM                  \n")
    print("\n                                                 -created by Mitushi Chauhan                  \n")
    print("\n                                       STUDENT MARKSHEET                                     \n")
    print(110 * "=")
    try:
        file = open("stud.dat", "rb")
        print("%-8s" % "Rollno", "%-10s" % "Name", "%-10s" % "Database", "%-14s" % "programming", "%-8s" % "security",
              "%-10s" % "digital_designs", "%-10s" % "web_development", "%-10s" % "Total", "%-8s" % "Per",
              "%-5s" % "Grade")
        print(110 * "=")
        while True:
            rec = pickle.load(file)
            rec.display_rec()

    except EOFError:
        file.close()
        print(110 * "=")
        input("Press any key to cont....")
    except IOError:
        print("File could not be opened")


def search_roll():
    os.system("cls")
    try:
        z = 0
        print(110 * "=")
        print("Record searching by roll no")
        print(110 * "=")
        n = int(input("Enter roll no to search"))
        file = open("stud.dat", "rb")
        while True:
            rec = pickle.load(file)
            if (rec.roll == n):
                z = 1
                print("\nRecord found and details are\n")
                rec.disp_rec()
                break

    except EOFError:
        file.close()
        if (z == 0):
            print("Record is not present")

    except IOError:
        print("File could not be opened")

    input("Press Enter to cont....")


def search_name():
    os.system("cls")
    try:
        z = 0
        n = input("Enter name to search  ")
        file = open("stud.dat", "rb")
        while True:
            rec = pickle.load(file)
            if (rec.name == n.upper()):
                z = 1
                rec.disp_rec()
                break

    except EOFError:
        file.close()
        if (z == 0):
            print("Record is not present")

    except IOError:
        print("File could not be opened")

    input("Press Enter to cont....")


def modify_roll():
    os.system("cls")
    z = 0
    try:
        n = int(input("Enter roll no to modify"))
        file = open("stud.dat", "rb")
        temp = open("temp.dat", "wb")
        while True:
            rec = pickle.load(file)
            if (rec.roll == n):
                z = 1
                print("Record found and details are")
                rec.disp_rec()
                print("Enter new data")
                rec.modify_rec()
                pickle.dump(rec, temp)
                print("Record updated")
            else:
                pickle.dump(rec, temp)

    except EOFError:
        file.close()
        temp.close()
        if (z == 0):
            print("Record not found")

    except IOError:
        print("File could not be opened")

    os.remove("stud.dat")
    os.rename("temp.dat", "stud.dat")
    input("Press Enter to cont....")


def delete_roll():
    os.system("cls")
    z = 0
    try:
        n = int(input("Enter roll no to delete"))
        file = open("stud.dat", "rb")
        temp = open("temp.dat", "wb")
        while True:
            rec = pickle.load(file)
            if (rec.roll == n):
                z = 1
                print("Record to delete found and details are")
                rec.disp_rec()
            else:
                pickle.dump(rec, temp)

    except EOFError:
        file.close()
        temp.close()
        if (z == 0):
            print("Record not found")

    except IOError:
        print("File could not be opened")

    os.remove("stud.dat")
    os.rename("temp.dat", "stud.dat")
    input("Press Enter to cont....")


while True:
    os.system("cls")
    print(110 * "=")
    print("""                    Main Menu
          ------------------------
          1. Add record
          2. Display all records
          3. Search by rollno
          4. Search by name
          5. Modify by rollno
          6. Delete by rollno
          7. Exit
    """)
    print(110 * "=")
    ch = int(input("Enter your choice"))
    print(110 * "=")
    if (ch == 1):
        write_rec()
    elif (ch == 2):
        display_all()
    elif (ch == 3):
        search_roll()
    elif ch == 4:
        search_name()
    elif (ch == 5):
        modify_roll()
    elif (ch == 6):
        delete_roll()
    elif (ch == 7):
        print("END")
        break
    else:
        print("INVALID CHOICE")
