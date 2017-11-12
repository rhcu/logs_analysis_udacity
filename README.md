# Udacity Logs Analysis Project
The 3rd projects made as a part of Udacity Full Stack Web Development Nanodegree. Project represents a reporting tool that prints the result of queries in the plain text to console, answering the following 3 questions:

**1. What are the most popular three articles of all time?**

**2. Who are the most popular article authors of all time?**

**3. On which days did more than 1% of requests lead to errors?**

# Required software
Vagrant and VirtualBox are needed to be installed before running the program to provide Linux environment. Vagrant can be downloaded from HashiCorp [website](https://www.vagrantup.com/), and VirtualBox from [here](https://www.virtualbox.org/). If you face some problems during the installation of Vagrant, you can find answers either at [Stack OverFlow](https://stackoverflow.com/search?q=vagrant) or in the [GitHub repository](https://github.com/hashicorp/vagrant) of Vagrant itself. 

Also, installed [Python 2.7](https://www.python.org/downloads/) is required, and `psycopg2` library, which connects Python code with PostgreSQL DBMS. 
# How to start
* After the installation, create your Virtual Machine by running in command line 
    `vagrant up`
* Enter  your Virtual Machine after the previous command by 
`vagrant ssh`
* [Download the data here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
and unzip the file and put newsdata.sql into your vagrant directory
* Download the data to your VM running `psql -d news -f newsdata.sql`
* Connect to your DB running: 
 `psql -d news`
* Run `CREATE VIEW` statements presented below
* Run the script `python log_analysis.py`
# Newsdata Database 
Database contains three tables: 
`articles`, `log`, `authors`.

In order to prevent multiple subqueries, views for the 2nd and 3rd questions were used.
**View for the 2nd question:**
The view to collect the number of views associated to author ID
```
CREATE VIEW author_views AS
SELECT a.author,
       COUNT(l.path) AS views
FROM articles AS a
LEFT OUTER JOIN log AS l ON '/article/'||a.slug = l.path
GROUP BY a.author
ORDER BY views DESC;
```

**View for the 3rd question**
Extracts the date from timestamp and calculates the number of errors and total number of requests
```
CREATE VIEW error_analysis AS
SELECT log.time::TIMESTAMP::date AS date,
       COUNT(CASE
                 WHEN log.status = '404 NOT FOUND' THEN 'error'
             END) AS errors,
       COUNT(*) AS requests
FROM log
GROUP BY date;
```
## Results of analysis
Answers for the questions are presented in the `answers.txt` file.

## License
Was built as a part of [Udacity Full Stack Web Developer Nanodegree Program](https://www.udacity.com/)
