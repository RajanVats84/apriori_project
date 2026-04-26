# -------------------------------
# EXPERIMENT 2: MULTI-DIMENSIONAL DATA MODEL USING SQL
# -------------------------------

import sqlite3

# Connect in-memory SQLite DB
conn = sqlite3.connect(":memory:")
cur = conn.cursor()

# Create table
cur.execute("""
CREATE TABLE sales (
    product TEXT,
    region TEXT,
    year INTEGER,
    amount INTEGER
)
""")

 # Insert sample data
sales_data = [
    ("Laptop", "North", 2023, 50000),
    ("Laptop", "South", 2023, 45000),
    ("Mobile", "North", 2023, 30000),
    ("Mobile", "South", 2024, 35000),
    ("Laptop", "North", 2024, 55000),
]
cur.executemany("INSERT INTO sales VALUES (?,?,?,?)", sales_data)
conn.commit()

# SQL Query: Region-Year Sales
query = "SELECT region, year, SUM(amount) FROM sales GROUP BY region, year"
print("Region-Year Sales:")
for row in cur.execute(query):
    print(row)


