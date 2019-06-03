# udacity-p1
This is a log analysis project required by the udacity Full Stack Web Developer Nanodegree program.  It generates three small text
reports by way of a sample database and python code.  The three small reports are the following:
* What are the most popular three articles of all time?
* Who are the most popular article authors of all time? 
* On which days did more than 1% of requests lead to errors? 

The database was provided by the udacity team as part of the project.

# Installation
`$ git clone https://github.com/jcarter62/udacity-p1.git`

`$ cd udacity-p1`

`$ ./logs-analysis.py`


# Requirements
This application requires the following:
* python3
* postgres database server
* "news" database provided by udacity
* psycopg2 library used to connect to database

# Usage
`$ cd udacity-p1`

`$ ./logs-analysis.py`

# Design
The design was rather simple.  I created a class called DB, and implemented several methods to implement the required reports.
