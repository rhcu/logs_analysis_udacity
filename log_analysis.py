import psycopg2


def main():
    conn = psycopg2.connect("dbname='news'")
    print("Answers for the required questions:")
    print("      ")
    # cursor object, used to perform queries
    cursor = conn.cursor()
    # uses top_three_articles view created previously
    sql_top_articles = """
        SELECT * from top_three_articles;
        """
    # executes the query
    cursor.execute(sql_top_articles)
    # result of the first question
    print("What are the most popular three articles of all time?")
    # increment for ordered list with elements
    i = 1
    for (article, views) in cursor.fetchall():
        print(str(i)+"    {} - {} views".format(article, views))
        i = i + 1
    # uses author_views view
    # associates id in author_views to name of the author from authors table
    sql_top_authors = """
        SELECT authors.name, author_views.views
        FROM authors LEFT OUTER JOIN author_views 
        ON authors.id = author_views.author;
        """
    # executes the query
    cursor.execute(sql_top_authors)
    print("     ")
    print("Who are the most popular article authors of all time?")
    i = 1
    for (name, views) in cursor.fetchall():
        print(str(i)+"    {} - {} views".format(name, views))
        i = i + 1
    sql_errors_ratio = """
        SELECT date, (CAST(errors AS FLOAT)*100/requests) AS percent 
        FROM error_analysis
        WHERE (CAST(errors AS FLOAT)*100/requests) > 1;
        """
    cursor.execute(sql_errors_ratio)
    print("      ")
    print("On which days did more than 1% of requests lead to errors?")
    i = 1
    for (date, percent) in cursor.fetchall():
        # to represent a date in Month day, year format
        date = date.strftime("%B %d, %Y")
        # rounds the result of the query to 2 decimal points
        percent = round(percent, 2)
        print(str(i)+"    {} - {}%".format(date, percent))
        i = i + 1
    print("      ")
    conn.close()
if __name__ == "__main__":
    main()
