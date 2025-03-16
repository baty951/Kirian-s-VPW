import configparser
import mysql.connector as mysql

config = configparser.ConfigParser()
config.read("config.ini")

def connect_to_db():
    bot_database = mysql.connect(
        user=config["mysqlDB"]["user"],
        host=config["mysqlDB"]["host"],
        database=config["mysqlDB"]["database"],
        password=config["mysqlDB"]["password"]
    )
    database = bot_database.cursor()
    return bot_database, database

def user_add_to_db(mess, data_base, cursorobject):
    try:
        user_user_id = mess.from_user.id
        user_username = mess.from_user.username
        user_first_name = mess.from_user.first_name
        user_last_name = mess.from_user.last_name

        sql = '''INSERT IGNORE INTO bot_users (user_id,
        user_username, user_first_name, user_last_name)\
            VALUES (%s, %s, %s, %s)'''