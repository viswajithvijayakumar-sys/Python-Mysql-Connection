import mysql.connector
conn=mysql.connector.connect(host="localhost",user="root",password="root",database="DjangoORM")
cur=conn.cursor()
# cur.execute("create database DjangoORM")
# print("Database created")
print("successfully created")

# cur.execute('''create table employee(
# id int primary key auto_increment,
# name varchar(30),
# designation varchar(30),
# salary decimal(10,2)
# )''')
# print("table created")



class Employee:
    def create(self,*args,**kwargs):
        key=list(kwargs.keys())
        keys=""
        placeholder=""
        for x in key:
            if keys!="":
                keys+=","
                placeholder+=","
            keys+=x
            placeholder+="%s"

        query=f"insert into employee({keys}) values({placeholder})"
        values=tuple(kwargs.values())
        cur.execute(query,values)
        conn.commit()
    def list(self,*args,**kwargs):
        cur.execute("select * from employee")
        # for i in cur:
        #     print(i)
        print(cur.fetchall())
    def retrieve(self,*args,**kwargs):
        for key in kwargs:
            cur.execute(f"Select * from employee where {key}={kwargs.get(key)}")
            print(cur.fetchall())
    def update(self,*args,**kwargs):
        for key in kwargs:
            cur.execute(f"update employee set {key}='{kwargs.get(key)}' where id={args[0]}")
            conn.commit()
    def delete(self,*args,**kwargs):
        cur.execute(f"delete from employee where id={args[0]}")
    def filter(self,*args,**kwargs):
        for key in kwargs:
            cur.execute(f"select * from employee where {key}='{kwargs.get(key)}'")
            print(cur.fetchall())


employee=Employee()


while True:
    print("1.create employee")
    print("2.list all employee")
    print("3.employee detial view")
    print("4.update employee")
    print("5.delete employee")
    print("6.filter employee")
    print("7.exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        name=input("Enter the employee name:")
        desig=input("Enter the designation:")
        salary=float(input("Enter the salary:"))
        employee.create(name=name,designation=desig,salary=salary)
    elif choice==2:
        employee.list()
    elif choice==3:
        id=int(input("Enter the id:"))
        employee.retrieve(id=id)
    elif choice==4:
        id=int(input("Enter the id:"))
        print("Update:")
        print("1.name")
        print("2.Designation")
        print("3.Salary")
        choice=int(input(("Enter your choice:")))
        if choice==1:
            name=input("enter the new name:")
            employee.update(id,name=name)
        elif choice==2:
            desig=input("Enter the new designation:")
            employee.update(id,designation=desig)
        elif choice==3:
            salary=float(input("Enter the new salary:"))
            employee.update(id,salary=salary)
        else:
            print("Invalid input")
    elif choice==5:
        id=int(input(("enter your id:")))
        employee.delete(id)
    elif choice==6:
        print("Filter by:")
        print("1.Filter by name")
        print("2.Filter by designation")
        print("3.Filter by salary")
        choice=int(input(("Enter your choice:")))
        if choice==1:
            name=input("enter the  name:")
            employee.filter(name=name)
        elif choice==2:
            desig=input("Enter the  designation:")
            employee.filter(designation=desig)
        elif choice==3:
            salary=float(input("Enter the salary:"))
            employee.filter(salary=salary)
        else:
            print("Invalid input")

    elif choice==7:
        break
    else:
        print("invalid input")

conn.close()
print("connection closed")





conn.close()
