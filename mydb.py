import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='nandhaaku',database='employedb')
mycursor=mydb.cursor()

mycursor=mydb.cursor()
mycursor.execute('select e1.id,e1.name,e1.teamleadId,e2.name as leadname from employee e1 join employee e2 on e1.teamleadId = e2.id ')
data = mycursor.fetchall()
print(data)
