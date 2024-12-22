from mysql.connector import connect

USERNAME="azamat"
PASSWORD="27052705"


db = connect(
    user = USERNAME,
    password = PASSWORD,
    host = "localhost",
    database = "Application"
)
dbc = db.cursor()
db.autocommit = True
