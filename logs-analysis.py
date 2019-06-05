#!/usr/bin/env python
import psycopg2

'''
Udacity Full Stack Web Developer Nanodegree
Project: Logs Analysis
Author: Jim Carter
Date: 6/3/2019
'''


class DB:
    #
    # Helper Class to provide connection to database
    # and methods to get and print required queries.
    #

    def __init__(self):
        self.connection_string = "dbname=news"
        self.conn = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(self.connection_string)
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        return self.conn

    def close(self):
        if self.conn is not None:
            self.conn.close()

    def get_popular_articles(self):
        #
        # Objective #1, obtain top three popular articles.
        #
        result = []
        try:
            self.connect()
            cursor = self.conn.cursor()

            cmd = """select a.title, count(log.path) as num
                     from log
                     join articles a on
                       log.path = concat('/article/', a.slug) and
                       log.method = 'GET' and log.status = '200 OK'
                     group by a.title
                     order by num desc
                     limit 3
                  """

            cursor.execute(cmd)
            results = cursor.fetchall()
            self.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        return results

    def print_popular_articles(self, data):
        print("What are the most popular three articles of all time?")
        for article, views in data:
            print("{} -- {} views".format(article, views))
        return

    def get_popular_authors(self):
        #
        # Objective #2, obtain popular authors along with number
        # of page views.
        #
        result = []
        try:
            self.connect()
            cursor = self.conn.cursor()

            cmd = """select auth.name, count(log.id) as num
                     from authors auth
                     join articles a on auth.id = a.author
                     join log on log.path = concat('/article/', a.slug)
                       and log.method = 'GET' and log.status = '200 OK'
                     group by auth.name
                     order by num desc
                  """

            cursor.execute(cmd)
            results = cursor.fetchall()
            self.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        return results

    def print_popular_authors(self, data):
        print("What are the most popular authors of all time?")
        for author, views in data:
            print("{} -- {} views".format(author, views))
        return

    def get_log_errors(self):
        #
        # Objective #3, obtain list of days where the error rate
        # is > 1%
        #

        result = []

        try:
            self.connect()
            cursor = self.conn.cursor()

            cmd = """select * from (
                       select cast(log.time as char(10)) as day,
                         round(
                           (sum(CASE
                                WHEN log.status != '200 OK'
                                THEN 1.0
                                ELSE 0.0
                            END) / sum(1.0)) * 100.0, 2) as PctError
                       from log
                       group by day
                     ) as t
                     where t.PctError > 1.0
                     order by day;
                  """

            cursor.execute(cmd)
            results = cursor.fetchall()
            self.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        return results

    def print_log_errors(self, data):
        title = "On which days did more than 1% of requests lead to errors?"

        print(title)
        for day, error_pct in data:
            print("{} -- {}% errors".format(day, error_pct))
        return


# Main Code
db = DB()
db.print_popular_articles(db.get_popular_articles())
print('')
db.print_popular_authors(db.get_popular_authors())
print('')
db.print_log_errors(db.get_log_errors())
print('')
