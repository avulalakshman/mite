import database as db

def c_add_internship():
    
    iname = input("Internship name:")
    cname = input("Company name:")
    year =  int(input("Conducted year:"))
    db.add_internship(iname, cname, year)

def c_view_all_internships():
    pass

def c_search_internship_by_name():
    pass

def c_change_status_internship():
    pass

def c_delete_internship():
    pass


while True:
    print("*"*50)
    print("Internship programms conducted at MITE by Companies")
    print("1.Add 2.View All 3.Search 4.Update 5.Delete 6.Exit")
    print("*"*50)
    try:
        ch = int(input("Enter your choice:"))
        if ch == 1:
            c_add_internship()
        elif ch == 2:
            c_view_all_internships()
        elif ch == 3:
            c_search_internship_by_name()
        elif ch == 4:
            c_change_status_internship()
        elif ch == 5:
            c_delete_internship()
        elif ch == 6:
            exit()
        else:
            raise TypeError(f"Input value should be <= 6, it was :{ch}")
    except TypeError as e:
        print(f"{str(e)}")