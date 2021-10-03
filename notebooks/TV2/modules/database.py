import mysql.connector as mysql
from modules.classes import Car, User, DataBaseException

def setup_db():
    cnx = mysql.connect(host = "db", user = "root", passwd = "root", db = "db")


    cursor = cnx.cursor()
    drop_users=('DROP TABLE IF EXISTS testUser;')
    create_users='create table users(id intemail varchar(100) not null, password varchar(100) not null, primary key(id));'
    
   
    
    cursor.execute(drop_users)
    cursor.execute(create_users)    

    # Commit the changes
    cnx.commit()
    cursor.close()
    cnx.close()
    
    print('Setup completed')




def add_new(car,user_name):
    try:
        cnx = mysql.connect(host = "db", user = "root", passwd = "root", db = "db")
        car['owner']=user_name
        cursor = cnx.cursor()
        print("car to save: ",car)
        query = "INSERT INTO cars VALUES (%(car_id)s,%(model)s,%(fuel)s,%(year)s,%(km)s,%(capacity)s,%(estimated_price)s,%(sale_price)s,%(owner)s);"
        cursor.execute(query,car)
        car['car_id']=cursor.lastrowid

        cnx.commit()
        
        cursor.close()
        cnx.close()
        car_obj=Car(car['model'],car['fuel'],car['year'],car['km'],car['capacity'],car['estimated_price'],car['sale_price'],car['car_id'])
        return car, car_obj
    except Exception as e:
        print("add_new:   ",e)
        raise DataBaseException("Saving the car aborted ")

def register_user(user_name, password):
    try:
        cnx = mysql.connect(host = "db", user = "root", passwd = "root", db = "db")
        
        cursor = cnx.cursor()
        query = "INSERT INTO users VALUES (%(user_name)s,%(password)s);"
        cursor.execute(query,{'user_name':user_name,'password':password})
        

        cnx.commit()
        
        cursor.close()
        cnx.close()
        user_obj=User(user_name,password)
        return {"user_name":user_name,"added":True}, user_obj
    except Exception as e:
        print(e)
        raise DataBaseException("Saving the user aborted ")
