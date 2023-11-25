import psycopg2

# PostgreSQL database details
database = "stock_data"
user = "postgres"
password = "postgres"
host = "localhost"
port = "5432"

# Connect to the PostgreSQL database
connection = psycopg2.connect(
    database=database,
    user=user,
    password=password,
    host=host,
    port=port
)

# Create a cursor object
cursor = connection.cursor()

# データベースの一覧を取得するクエリを実行
cursor.execute("SELECT datname FROM pg_database")

# Fetch all the rows
rows = cursor.fetchall()

for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
connection.close()
