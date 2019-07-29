import time
import random as rn

i_list = []

def add_internship(iname,company,year):
    id = _get_new_id()
    inter_obj = {"id":id,"iname":iname, "company":company, "year":year,"status":1}
    i_list.append(inter_obj)
    print(f"Intership programm is added with id: {id} successfully...")

def view_all_internships():
    pass
def search_internship_by_name(name):
    pass
def change_status_internship(name):
    pass
def delete_internship():
    pass

def _get_new_id():
    t_obj = time.localtime()
    new_id = rn.randint(1000,9900) + (t_obj.tm_min + t_obj.tm_hour + t_obj.tm_sec)
    return new_id
    
