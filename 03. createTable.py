def createTable(schema,table,connection,code):

    #--- Check Table
    # schema: string, name of schema to create or load into
    # table: string, name of table to create or load into
    # connection: string, contining connection details e.g. host=<ip address> dbname=<db name> user=<user name> password=<pass word>
    # code: string, containing create table code e.g. CREATE TABLE test.test01(d_id bigint);
    
    import psycopg2
    
    conn = psycopg2.connect(connection)
    
    cursor = conn.cursor()
    cursor.execute(code)
    conn.commit()
    
    cursor.execute('ALTER TABLE '+schema+'.'+table+' OWNER TO superusers;')
    conn.commit()
    
    cursor.execute('GRANT All ON TABLE '+schema+'.'+table+' TO "superusers";')
    conn.commit()
    
    conn.close()
