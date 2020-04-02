import pymysql

host="esmosticket.cdf4pnuq8quq.us-east-1.rds.amazonaws.com"
port=3306
dbname="stocks"
user="admin"
password="enterprise123!"

conn = pymysql.connect(host, user=user,port=port,
                           passwd=password, db=dbname)

cur = conn.cursor()
cur.execute("INSERT INTO stocks VALUES('amelia1', 'aapl1', 12, 121.00, 'pending', 'unuique')")
conn.commit()









    # data = json.loads(request.data)
    # unique = data['unique']
    
    # amt = json.loads(request.data)['amt']
    # current = json.loads(request.data)['current']
    
    # return {'a': unique, 'b': 'ticker'}, 200

    # host="esmosticket.cdf4pnuq8quq.us-east-1.rds.amazonaws.com"
    # port=3306
    # dbname="stocks"
    # user="admin"
    # password="enterprise123!"

    # conn = pymysql.connect(host, user=user,port=port,
    #                         passwd=password, db=dbname)

    # cur = conn.cursor()
    # cur.execute("INSERT INTO stocks VALUES('test', '"+str(ticker)+"', '"+str(amt)+"', '"+str(current)+"', 'pending', '"+str(unique)+"')")
    # conn.commit()

    return {'status': 'good', 'data': data}, 200
    #return request.data, 200