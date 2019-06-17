import pymysql

def connection():
    try:
	#enables connection to the database, using the endpoint provided by AWS rds
        conn = pymysql.connect(host="rds-demo.csaruqlxxway.us-east-1.rds.amazonaws.com",user="root",passwd="*******",port=3306, db="Game" )
        print("connected.")
        return conn
    except Exception as e:
        print(e)

# create a cursor object of the database
db = connection()
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
# Create operaration
sql = """CREATE TABLE EMPLOYEE (
   FIRST_NAME  CHAR(20) NOT NULL,
   LAST_NAME  CHAR(20),
   AGE INT,  
   Gender CHAR(1),
   INCOME FLOAT )"""

cursor.execute(sql)
print("created table")
cursor.execute("INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, Gender, INCOME) VALUES ('Vishal', 'Bisht', 22, 'M', 100)")
cursor.execute("INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, Gender, INCOME) VALUES ('Austin', 'Dzousa', 21, 'M', 200)")
cursor.execute("INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, Gender, INCOME) VALUES ('Akash', 'Mahale', 2, 'M', 300)")
cursor.execute("Select * from  EMPLOYEE")
results = cursor.fetchall()
print(results)

