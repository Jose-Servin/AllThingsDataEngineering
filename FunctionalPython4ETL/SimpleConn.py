import psycopg2
from config import DATABASE_CONFIG

# Connect to DB
conn = psycopg2.connect(**DATABASE_CONFIG)

# create cursor
cur = conn.cursor()

# execute query
cur.execute(
    "select customer_id, year_birth, education from master_data where customer_id = 5524")

# return tuple for rows
rows = cur.fetchall()

for r in rows:
    print(f"Customer ID: {r[0]}, Year of Birth: {r[1]}, Education: {r[2]}.")

# close the cursor
cur.close()

# close connection
conn.close()
