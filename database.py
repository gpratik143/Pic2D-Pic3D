import sqlite3

def create_table():
    con=sqlite3.connect("Employees.db")
    cur=con.cursor()
    
    cur.execute("create table if not exists Employess(id int primary key,Name TEXT,Role TEXT,Gender TEXT,Status TEXT)")
    con.commit()
    con.close()
    
def fetch_employess():
    con=sqlite3.connect('Employees.db')
    cur=con.cursor()
    cur.execute("select * from Employee")
    con.close()
    return fetch_employess

def insert_employees(id , name,role,gender,status):
    con=sqlite3.connect("Enmployees.db")
    cur=con.cursor()
    cur.execute("insert into Employees (id,name,role,gender,status) values (?,?,?,?,?)"(id,name,role,gender,status))
    con.commit()
    con.close()
    
def dlt_employee(id):
    con=sqlite3.connect('Employee.db')
    cur=con.cursor()
    cur.execute("delete from employee where id=?",(id))
    con.commit()
    con.close()
    
def update_employee(new_name,new_role,new_gemder,new_status,id):
    con=sqlite3.connect('Employee.db')
    cur=con.cursor()
    cur.execute('update employee set name=?,role=?,gender=?,status=?'(new_name,new_role,new_gemder,new_status,id))
    con.commit()
    con.close()
    
def id_exists(id):
    con=sqlite3.connect("Employees.db")
    cur=con.cursor()
    cur.execute('select count(*) form employee where id=?',(id))
    result=cur.fetchone()
    con.close()
    return result[0]>0


create_table()
    

