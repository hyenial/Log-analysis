# !/usr/bin/env python
# import module for psql database

import psycopg2

print('please wait, Calculating...\n')

# connecting to the database called  'news'
conn = psycopg2.connect("dbname=news")

# making a cursor with the connection and creating a variable for this.
cursor = conn.cursor()


def execute(query):
    cursor.execute(query)

# query_1 shows What are the most popular three articles of all time?
query_1 = ("""
            select title, count(title) as Views
            from articles, log
            where log.path like concat ('%', articles.slug)
            group by title order by views desc limit 3;
            """)

# execure query_1 to get result
execute(query_1)
rows = cursor.fetchall()
print "\n1. What are the most popular three articles of all time?:"
for row in rows:
    print "Article: '" + str(row[0]) + "' ------ " + str(row[1]) + " Views"

# making seperator to make result easy to read
line = "---"
print(line * 20)

# query_2 show popular_authors by decending order
# Who are the most popular article authors of all time?
query_2 = ("""
            select authors.name, count(articles.author) as Views
            from articles, log, authors
            where log.path like concat ('%', articles.slug)
            and articles.author = authors.id
            group by authors.name order by Views desc;
            """)

execute(query_2)
rows = cursor.fetchall()
print "\n2. Who are the most popular article authors of all time?:"
for row in rows:
    print "Author: " + str(row[0]) + " ------ " + str(row[1]) + " Views"

# making seperator to make result easy to read
print(line * 20)

# query_3 shows On which days did more than 1% of requests lead to errors?
query_3 = ("""
            select Date, (Error::float * 100) / Total::float as Percent
            from (select time::timestamp::date as Date, count(status) as Total,
            sum(case when status like '%404%' then 1 end) as Error
            from log group by Date) as Result
            where (Error::float * 100)/ Total::float > 1.00;
            """)

execute(query_3)
rows = cursor.fetchall()
print "\n3. On which days did more than 1% of requests lead to errors?:"
for row in rows:

    # chaging format of date and floating two decimals of error result
    x = row[0]
    print "Date: " + x.strftime("%b %d %Y") \
     + " ----- " + str(round(row[1], 2)) + "% Errors"

# closing the connection.
conn.close()

# making seperator to make result easy to read
print(line * 20)

print('Thank You...\n')
