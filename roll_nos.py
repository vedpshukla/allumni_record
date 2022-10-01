def Z():
    import mysql.connector as p
    from tabulate import tabulate
    con=p.connect(host="localhost",user="root",passwd="root",database="allumni_record")
    cur=con.cursor()
    p=[]
    query="select roll from students"
    cur.execute(query)
    z=cur.fetchall()
    #print(z)
    for i in range(len(z)):
         z[i]=z[i][0]
    return z
