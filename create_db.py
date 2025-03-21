import configparser
import mysql.connector as mysql

config = configparser.ConfigParser()
config.read("config.ini")

def connect_to_db():
    bot_db = mysql.connect(
        user=config["mysqlDB"]["user"],
        host=config["mysqlDB"]["host"],
        database=config["mysqlDB"]["database"],
        password=config["mysqlDB"]["password"]
    )
    db = bot_db.cursor()
    return bot_db, db

def create_db_table(bot_db, db):
    create_bot_users_ask = '''CREATE TABLE bot_vpw_users (
        id BIGINT UNSIGNED PRIMARY KEY Not NULL,
        buy_date DATE,
        date_to_buy DATE,
        reg_date DATE
    )'''

    db.execute(create_bot_users_ask)
    bot_db.commit()

bot_db, db = connect_to_db()
create_db_table(bot_db, db)