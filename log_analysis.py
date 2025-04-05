#!/usr/bin/env python3
import psycopg2

print('Please wait, calculating...\n')

# Connect to the 'news' database
conn = psycopg2.connect("dbname=news")
cursor = conn.cursor()

def fetch(query):
    cursor.execute(query)
    return cursor.fetchall()

# 1. What are the most popular three articles of all time?
query_1 = """
    SELECT title, COUNT(*) AS views
    FROM articles
    JOIN log ON log.path LIKE '%' || articles.slug
    GROUP BY title
    ORDER BY views DESC
    LIMIT 3;
"""
rows = fetch(query_1)
print("\n1. What are the most popular three articles of all time?")
for row in rows:
    print(f"Article: '{row[0]}' ------ {row[1]} Views")

print("---" * 20)

# 2. Who are the most popular article authors of all time?
query_2 = """
    SELECT authors.name, COUNT(*) AS views
    FROM articles
    JOIN authors ON articles.author = authors.id
    JOIN log ON log.path LIKE '%' || articles.slug
    GROUP BY authors.name
    ORDER BY views DESC;
"""
rows = fetch(query_2)
print("\n2. Who are the most popular article authors of all time?")
for row in rows:
    print(f"Author: {row[0]} ------ {row[1]} Views")

print("---" * 20)

# 3. On which days did more than 1% of requests lead to errors?
query_3 = """
    SELECT date, (error::float * 100) / total AS percent
    FROM (
        SELECT time::date AS date,
               COUNT(*) AS total,
               SUM(CASE WHEN status LIKE '404%' THEN 1 ELSE 0 END) AS error
        FROM log
        GROUP BY date
    ) AS result
    WHERE (error::float * 100) / total > 1.0;
"""
rows = fetch(query_3)
print("\n3. On which days did more than 1% of requests lead to errors?")
for row in rows:
    date_str = row[0].strftime("%b %d %Y")
    print(f"Date: {date_str} ----- {round(row[1], 2)}% Errors")

print("---" * 20)

# Close connection
conn.close()
print('Thank you!\n')
