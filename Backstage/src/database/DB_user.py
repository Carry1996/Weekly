# -*- coding: utf-8 -*-
import pymysql
from database import DBConnection

def insert(email,password,userName,Wnumber,LWnumber):

    flag = False
    # 打开数据库连接
    db = DBConnection.connection()

    # 使用cursor()方法创建一个游标对象cursor
    cursor = db.cursor()

    #SQL插入语句
    sql = "insert into user(email,password,userName,Wnumber,LWnumber)\
          values('%s','%s','%s','%d','%d')" % \
          (email,password,userName,Wnumber,LWnumber)

    try:
        #执行sql语句
        cursor.execute(sql)
        #提交到数据库执行
        db.commit()
        flag = True
    except:
        #如果发生错误则回滚
        db.rollback()

    #关闭数据库连接
    db.close()
    return flag

def Search(userID):
    result = 0
    # 打开数据库连接
    db = DBConnection.connection()

    # 使用cursor()方法创建一个游标对象cursor
    cursor = db.cursor()

    # SQL查找语句
    sql = "select password from user where userID = '%s'" % (userID)

    try:
        # 执行sql语句
        cursor.execute(sql)
        # 获取所有记录列表
        result = cursor.fetchone()
    except:
        # 如果发生错误则回滚
        db.rollback()

    # 关闭数据库连接
    db.close()
    return result

def SubSearch(LWnumber):
    list = []
    # 打开数据库连接
    db = DBConnection.connection()

    # 使用cursor()方法创建一个游标对象cursor
    cursor = db.cursor()

    # SQL查找语句
    sql = "select * from user where LWnumber  = '%d'" % (LWnumber)

    try:
        # 执行sql语句
        cursor.execute(sql)
        # 获取所有记录列表
        result = cursor.fetchall()
        for row in result:
            list.append(row)
    except:
        # 如果发生错误则回滚
        db.rollback()

    # 关闭数据库连接
    db.close()
    return list