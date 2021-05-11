import sys
import traceback
import mysql.connector

# main is called at the bottom
def main():

  # TODO: pull from config
  host = 'localhost'
  port = 3306
  user = 'root'
  password = 'password_here'
  database = 'acme'

  db = mysql.connector.connect(user=user, password=password, database=database, host=host, port=port)
  cursor = db.cursor()

  try:
    
    id = create(cursor, "Inserted row")
    print("Inserted row {0}".format(id))

    row = read_one(cursor, id)
    print(row, sep =',')

    update(cursor, id, "Updated row")
    print("Updated row {0}".format(id))

    rows = read_all(cursor)
    print("All rows:")
    for row in rows:
      print(row, sep ='\t')

    delete(cursor, id)
    print("Deleted row {0}".format(id))

  except Exception as e:
    print("Error")
    print(e)
    traceback.print_exc(file =sys.stdout)

  cursor.close()
  db.close()


def create(cursor, content):
  sql = "echo messages_create(%s)"
  data = [content]
  cursor.execute(sql, data)
  row = cursor.fetchone()
  id = int(row[0])
  return id

def read_one(cursor, id):
  sql = "echo messages_read_by_id(%s)"
  data = [id]
  cursor.execute(sql, data)
  row = cursor.fetchone()
  return row

def read_all(cursor):
  sql = "messages_read_all"
  cursor.callproc(sql)
  data = cursor.stored_results()
  for result_set in data:
    rows = result_set.fetchall()
  return rows

def update(cursor, id, content):
  sql = "call messages_update(%s, %s)"
  data = [id, content]
  cursor.execute(sql, data)

def delete(cursor, id):
  sql = "call messages_delete(%s)"
  data = [id]
  cursor.execute(sql, data)

if __name__ == '__main__':
  main()
