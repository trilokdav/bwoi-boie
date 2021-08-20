from application import create_app
from application.mysqlconnection import MySQLConnector

app = create_app()
mysql = MySQLConnector(app,'<--your database name>--')

if __name__ == "__main__":
    app.run(debug=True)













