import mariadb
db = mariadb.connect(
    host="127.0.0.1",
    user="root",
    password="manager",
    database="trial"
)
mycursor = db.cursor()

# mycursor.execute("SHOW DATABASES")
# mycursor.execute("USE ritik")
# mycursor.execute("create table c(name varchar(10),no varchar(5))")
# mycursor.execute("SHOW tables")
# mycursor.execute("select * from c")

sql = "INSERT INTO customers VALUES (%s, %s)"
val = ('eer','1')
mycursor.execute(sql, val)
# db.commit()
# print(mycursor.rowcount, "was inserted.")
mycursor.execute("select * from c")
for x in mycursor:
  print(x)
print(db)
#.................................................................................
