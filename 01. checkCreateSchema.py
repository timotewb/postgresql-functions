def checkCreateSchema(schema, connection):

  #--- Check and Create Schema
  # schema: string, name of schema to create or load into
  # connection: string, contining connection details e.g. host=<ip address> dbname=<db name> user=<user name> password=<pass word>
  
  import psycopg2

  conn = pgclass.psycopg2.connect(connection)
  cursor = conn.cursor()
  cursor.execute("select distinct schema_name from information_schema.schemata where schema_name = '"+schema+"'")
  if cursor.rowcount >= 1:
    pass
  else:
    cursor.execute('create schema '+schema+' authorization "superusers"')
    conn.commit()
    cursor.execute('GRANT ALL ON SCHEMA '+schema+' TO "superusers"')
    conn.commit()
  conn.close()
