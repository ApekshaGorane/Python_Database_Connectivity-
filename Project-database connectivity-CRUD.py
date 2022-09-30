import pymysql as p
def getconnect():
    return p.connect(host="localhost",user="root",password="",database="mydb")

def add(t):
    db=getconnect()
    cr=db.cursor()
    sql="insert into employee values(%s,%s,%s,%s)"
    cr.execute(sql,t)
    db.commit()
    db.close()

def read():
    db=getconnect()
    cr=db.cursor()
    sql="select * from employee"
    cr.execute(sql)
    data=cr.fetchall()
    print(data)
    db.commit()
    db.close()
    #return data

def update(t):
    db=getconnect()
    cr=db.cursor()
    sql="update employee set name=%s,dept=%s,salary=%s where id=%s"
    cr.execute(sql,t)
    db.commit()
    db.close()
    

def delete(id):
    db=getconnect()
    cr=db.cursor()
    sql="delete from employee where id=%s"
    cr.execute(sql,id)
    db.commit()
    db.close()
