#!/usr/bin/env python3  
import psycopg2


class DB:

    def __init__(self):
        self.connection_string = "dbname=news user=postgres password=postgres"
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
        for rec in data:
            print(rec[0] + " -- " + str(rec[1]) + " views")
        return

    def get_popular_authors(self):
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
        for rec in data:
            print(rec[0] + " -- " + str(rec[1]) + " views")
        return

    def get_log_errors(self, min_percent):
        if min_percent is None:
            min_percent = 1.0
        result = []
        try:
            self.connect()
            cursor = self.conn.cursor()

            cmd = """select *, %s as minpct from (
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
                     where t.PctError > %s
                     order by day;
                  """

            cursor.execute(cmd, [min_percent, min_percent])
            results = cursor.fetchall()
            self.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        return results

    def print_log_errors(self, data):
        title = "On which days did more than 1% of requests lead to errors?"

        if data.__len__() > 0:
            title = "On which days did more than " + str(data[0][2]) + \
                    "% of requests lead to errors?"

        print(title)
        for rec in data:
            print(rec[0] + " -- " + str(rec[1]) + "% errors")
        return


db = DB()
db.print_popular_articles(db.get_popular_articles())
print('')
db.print_popular_authors(db.get_popular_authors())
print('')
db.print_log_errors(db.get_log_errors(1.0))