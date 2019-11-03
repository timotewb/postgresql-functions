def returnData(code, connection):

    #--- Return Data
    # code: string, containing select code e.g. select distinct table_name from information_schema.tables;
    # connection: string, contining connection details e.g. host=<ip address> dbname=<db name> user=<user name> password=<pass word>
    #
    # rows: list of tuples, containg data from db. no header is returned

    import psycopg2
    
    conn = psycopg2.connect(connection)
    cursor = conn.cursor()
    cursor.execute(code)
    
    rows = cursor.fetchall()
    return rows
    
    conn.close()
