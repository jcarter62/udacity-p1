# udacity-p1
This is a log analysis project required by the 
udacity Full Stack Web Developer Nanodegree program.
It generates three small text reports by way of 
a sample database and python code.  The three 
small reports are the following:
- What are the most popular three articles of all time?
- Who are the most popular article authors of all time? 
- On which days did more than 1% of requests lead to errors? 

The database was provided by the udacity team as part of the project.

# Getting Started
If you have not setup or run vagrant, you will need to download vagrant at the following [link](https://www.vagrantup.com/downloads.html).  Then you will also need to download the virtual machine configuration at this [link](https://classroom.udacity.com/nanodegrees/nd004-ent/parts/72d6fe39-3e47-45b4-ac52-9300b146094f/modules/0f94ae26-c39d-4231-924b-b1eb6e06cf41/lessons/5475ecd6-cfdb-4418-85a2-f2583074c08d/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0).

# Prerequisites
This application requires the following:
- [vagrant](https://www.vagrantup.com/downloads.html)
- [virtual machine configuration](https://classroom.udacity.com/nanodegrees/nd004-ent/parts/72d6fe39-3e47-45b4-ac52-9300b146094f/modules/0f94ae26-c39d-4231-924b-b1eb6e06cf41/lessons/5475ecd6-cfdb-4418-85a2-f2583074c08d/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0)
- [sample "news" database provided by udacity](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

# Installing
After downloading and installing the prerequisites, continue:

Start the vm using the following commands
```
$ cd <to the directory containing Vagrantfile>
$ vagrant up
```

Connect to vm using ssh
```
$ cd <to the directory containing VagrantFile>
$ vagrant ssh
```
Download the sample data available at the following [link](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip):

*Copy the newsdata.sql file to the directory containing VagrantFile*
```
$ cd <to the directory containing VagrantFile>
$ vagrant ssh
$ cd /vagrant
$ psql -d news -f newsdata.sql
```

Download this project's code using the following
```
$ cd <to the directory containing VagrantFile>
$ vagrant ssh
$ cd /vagrant
$ git clone https://github.com/jcarter62/udacity-p1.git
$ cd udacity-p1
$ ./logs-analysis.py
```

# Other Information
Vagrant and the virtual machine configuration will setup the environment that includes:
- python
- postgres database server
- psycopg2 python library

# Usage
```
$ cd <to the directory containing VagrantFile>
$ vagrant ssh
$ cd /vagrant/udacity-p1
$ ./logs-analysis.py
```

# Design
The design was rather simple.  I created a class called DB, and implemented several methods to implement the required reports.

# Authors
Jim Carter

# License
This project is licensed under the MIT License