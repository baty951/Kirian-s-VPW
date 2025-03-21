import configparser
import mysql.connector as mysql
import datetime
import asyncio
from mysql.connector.aio import connect
config = configparser.ConfigParser()
config.read("config.ini")
'''
async def connect_to_db():
    bot_database = await connect(
        user=config["mysqlDB"]["user"],
        host=config["mysqlDB"]["host"],
        database=config["mysqlDB"]["database"],
        password=config["mysqlDB"]["password"]
    )
    database = await bot_database.cursor()
    return bot_database, database
'''
async def user_add_to_db(mess):
    #bot_data_base, data_base = connect_to_db()
    bot_database = await connect(
        user=config["mysqlDB"]["user"],
        host=config["mysqlDB"]["host"],
        database=config["mysqlDB"]["database"],
        password=config["mysqlDB"]["password"]
    )
    database = await bot_database.cursor()
    id = mess.from_user.id
    reg_date = str(datetime.datetime.now())

    sql = '''INSERT IGNORE INTO '''+config["mysqlDB"]["table"]+'''
    (id, reg_date) VALUES 
    (%s, %s)'''
    val = (id, reg_date)

    await database.execute(sql, val)
    await bot_database.commit()
    await database.close()
    await bot_database.close()
