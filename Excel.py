#lines to import scores from excel to database
#database: allumni_record


from xlrd import open_workbook 
import mysql.connector as mq

con=mq.connect(host="localhost",user="root",passwd="root",database="allumni_record")

cur=con.cursor()
def a():
    wb=open_workbook("Allumni_file.xlsx")

    s=wb.sheet_by_index(0)

    for r in range(4,1000):
        try:
            d=[s.cell(r,8).value,s.cell(r,9).value,s.cell(r,10).value,s.cell(r,11).value,s.cell(r,12).value]
            #print(d)
            query="insert into students values ({},'{}',{},{},'{}')".format (d[0],d[1],d[2],d[3],d[4])
            cur.execute(query)
            con.commit()
        except:
            break

    con.close()
