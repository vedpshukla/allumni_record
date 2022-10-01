

import mysql.connector as p
from tabulate import tabulate
con=p.connect(host="localhost",user="root",passwd="root",database="allumni_record")
cur=con.cursor()
query="select roll from students"
cur.execute(query)
z=cur.fetchall()
print(z)
                
m=int(input("roll:"))
print(m)
for v in z:
    if m == v[0]:
        print("ÿes")
        break
   
