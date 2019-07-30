import time
import random as rn
import dbcontext as db
from models import Internship 
from beautifultable import BeautifulTable

def _get_new_id():
    t_obj = time.localtime()
    new_id = rn.randint(1000,9900) + (t_obj.tm_min + t_obj.tm_hour + t_obj.tm_sec)
    return new_id

def add_internship(iname,company,i_year):
    id = _get_new_id()
    try:
        with db.DbContext() as connection:
            cursor = connection.cursor()
            cursor.execute("insert into internship(id,iname,company,i_year,status) values(?,?,?,?,?)",(id,iname,company,i_year,1))
            print(f"Internship is added successfully with id:{id}")
    except Exception as e:
        print(str(e))

def view_all_internships():
    try:
        with db.DbContext() as connection:
            cursor = connection.cursor()
            cursor.execute("select id,iname,company,i_year,status from internship")
            rows = cursor.fetchall()
            intern_pro_lst = [Internship(*row) for row in rows]
            _view_internship_list(intern_pro_lst)
    except Exception as e:
        print(str(e))
def search_internship_by_name(name):
    pass
def change_status_internship(name):
    pass
def delete_internship():
    pass

def add_student_internship(name,sem,iid):
    pass
def view_all_reg_student():
    pass
def search_student_by_name(name):
    pass
def update_student(sid,sem):
    pass
def delete_student(sid):
    pass


def company_ws_count():
    pass
def student_ws_count():
    pass
def ws_student_reports():
    pass

def reg_stu_internship():
    pass

def update_stu_intership_status():
    pass


def _view_internship_list(lst):
    if lst and len(lst) > 0:
        table = BeautifulTable()
        table.column_headers = ["ID", "NAME", "COMPANAY", "YEAR","STATUS"]
        for l in lst:
            status = "Comleted" if l.status == 0 else "Going on" 
            table.append_row([l.id, l.iname, l.company, l.i_year,status])
        print(table)
    else:
        print(f"There are no Intership programms, yet to add...")