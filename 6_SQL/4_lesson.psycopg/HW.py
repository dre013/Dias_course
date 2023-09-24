import psycopg2
from psycopg2 import Error


con = psycopg2.connect(dbname="testDB", user="postgres",
                       password="something")
cur = con.cursor()

# cur.execute("DROP TABLE IF EXISTS CARS")
# con.commit()

# cur.execute(
#     "CREATE TABLE CARS (car_id serial PRIMARY KEY, car_name varchar, engine_volume int)")
# con.commit()

try:
    cur.execute(
        "INSERT INTO cars (car_name, engine_volume) VALUES (%s, %s)", ("FIAT", 1.5))
    cur.execute("INSERT INTO cars (car_name, engine_volume) VALUES (%(name)s, %(volume)s)",
                {"name": "Volkswagen", "volume": 1.6})
    con.commit()
except (Exception, Error) as e:
    print("Error", e)
finally:
    if con:
        cur.close()
        con.close()
        print("Done, data been inserted")
