import mysql.connector
#conn=mysql.connector.connect(user='root',password='root',database='5d',use_unicode=True)
conn = mysql.connector.connect(user='root', password='root', database='5d', use_unicode=True)
cursor=conn.cursor()
cursor.execute('select * from esc_admin where id=%s',('1',))
values=cursor.fetchall()
print values
cursor.close()
conn.commit()
conn.close()