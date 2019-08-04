def checkTable(schema,table,connection):

    #--- Check Table
    # schema: string, name of schema to create or load into
    # table: string, name of table to create or load into
    # connection: string, contining connection details e.g. host=<ip address> dbname=<db name> user=<user name> password=<pass word>
    
    import psycopg2

    conn = psycopg2.connect(connection)
    cursor = conn.cursor()
    cursor.execute("select distinct table_name from information_schema.tables where upper(table_schema) = upper('"+schema+"') and upper(table_name) = upper('"+table+"')")
    if cursor.rowcount >= 1:
        return True
    else:
        return False
        
    conn.close()
