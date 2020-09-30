
import psycopg2
import datetime

connection = psycopg2.connect(user="elanco_user", password="elanco_pass",
                              host="51.91.120.89", database="elanco", port="5432")
connection.set_session(autocommit=False, readonly=False)
print(connection)

cursor = connection.cursor()

# SELECT SQL
sql = "SELECT * FROM public.city WHERE city_id=255"
cursor.execute(sql)
row = cursor.fetchone()
print(row)

print("="*60)
sql = "SELECT * FROM public.city ORDER BY city LIMIT 10 "
cursor.execute(sql)
rows = cursor.fetchall()
for row in rows:
    print(row)

# INSERT
sql= " INSERT INTO public.country (country, last_update) VALUES (%s, %s) "
data = "Nibylandia" , datetime.datetime.today()
cursor.execute(sql, data)
connection.commit()

# UPDATE
sql = "UPDATE public.country set country=%s WHERE country=%s"
data = "Nibylandia2", "Nibylandia"
cursor.execute(sql, data)
connection.commit()

# DELETE
sql = "delete FROM public.country WHERE country=%s "
data = "Nibylandia2",
cursor.execute(sql, data)
connection.commit()

if connection:
    cursor.close()
    connection.close()