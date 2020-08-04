 # Log-analysis
## Project Description

You've been hired onto a team working on a newspaper site. The user-facing newspaper site frontend itself, and the database behind it, are already built and running. You've been asked to build an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.
The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. Using that information, your code will answer questions about the site's user activity.
The program you write in this project will run from the command line. It won't take any input from the user. Instead, it will connect to that database, use SQL queries to analyze the log data, and print out the answers to some questions.


####    Why this project?
In this project, you will stretch your SQL database skills. You will get practice interacting with a live database both from the command line and from your code. You will explore a large database with over a million rows. And you will build and refine complex queries and use them to draw business conclusions from data.


####    Report generation
Building an informative summary from logs is a real task that comes up very often in software engineering. For instance, at Udacity we collect logs to help us measure student progress and the success of our courses. The reporting tools we use to analyze those logs involve hundreds of lines of SQL.]

####    Database as shared resource
In this project, you'll work with data that could have come from a real-world web application, with fields representing information that a web server would record, such as HTTP status codes and URL paths. The web server and the reporting tool both connect to the same database, allowing information to flow from the web server into the report.
This shows one of the valuable roles of a database server in a real-world application: it's a point where different pieces of software (a web app and a reporting tool, for instance) can share data.


####    Questions
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

#### Setup
1. To start on this project, you'll need database software (provided by a Linux virtual machine) and the data to analyze.
This will give you the PostgreSQL database and support software needed for this project. If you have used an older version of this VM, you may need to install it into a new directory. I used VM 6.1

You can download [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) to install and manage your virtual machine.

Use `vagrant up` to bring the virtual machine online and `vagrant ssh` to login. I modify the vagrant file and change 2nd line
"config.vm.box = "bento/ubuntu-16.04"
config.vm.box_version = "201912.15.0""

my virtual machine works on ubuntu16.04

2. Download the data provided by Udacity newsdata.zip. https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
 Unzip the file in order to extract newsdata.sql. This file should be inside the Vagrant folder.
line
"config.vm.box = "bento/ubuntu-16.04"
config.vm.box_version = "201912.15.0""



3. Load the database using `psql -d news -f newsdata.sql`.

4. Connect to the database using `psql -d news`.

5. Create the Views given below. Then exit `psql`.

6. import psycopg2 #import module for psql database

`import psycopg2`
#connecting to the database called  'news'
`conn = psycopg2.connect("dbname=news")`

7. execute python file python `python log_analysis.py` 

### Resources
- postgress documentation https://www.postgresql.org/docs/devel/app-psql.html
- postgress connecting database https://www.postgresql.org/docs/12/tutorial-accessdb.html
- sql basics https://www.sqltutorial.org/sql-cheat-sheet/
- sql advance https://hackr.io/blog/sql-cheat-sheet
- tutorial  https://www.youtube.com/watch?v=2PDkXviEMD0
