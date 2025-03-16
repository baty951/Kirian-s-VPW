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
    create_bot_users_ask = '''CREATE TABLE bot_users (
        id BIGINT UNSIGNED PRIMARY KEY,
        username VARCHAR(255),
        first_name VARCHAR(255),
        last_name VARCHAR(255),
        chat_id BIGINT UNSIGNED,
        reg_date DATE
    )'''
    create_vpw_buyers_ask = '''CREATE TABLE vpw_buyers (
        id BIGINT UNSIGNED PRIMARY KEY,
        chat_id BIGINT UNSIGNED,
        buy_date DATE,
        date_to_buy DATE
    )'''