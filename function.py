import pymysql

conn= pymysql.connect(host="localhost", user="root", password="", database="BillManagement")


def delete(table, column, id):
    with conn.cursor() as cur:
        sql=f'''delete from {table} where {column}={id}'''
        print(sql)
        result=cur.execute(sql)
        conn.commit()
    
    if result:
        return True
    else:
        return False
            
