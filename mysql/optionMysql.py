#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect(host="localhost",user="root",passwd="root",db="springboot",charset="utf8")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL插入语句
ins_sql1 = 'insert into person(name,age,address) values(%s,%s,%s)'

# SQL查询语句
sel_sql = 'select * from person order by id desc'

# SQL更新语句
upd_sql = 'update person set name=%s where id=%s'

# SQL删除语句
del_sql = 'delete from person where id=%s'

try:
	# select  OK
	
    #cursor.execute(sel_sql)
    #values = cursor.fetchall()
    #print(values)

    # 执行sql语句
    # insert
	#num = cursor.execute(ins_sql1, ('张飞',33,'柳州11'))
	#print(num)
	
    # update
	#num=cursor.execute(upd_sql, ('更新', 14))
	#print(num)
    # delete
	row = cursor.execute(del_sql,(11,))
	print(row)
    # 提交到数据库执行
	db.commit()
except Exception as e:
	print('Error:',e)
    # 发生错误时回滚
	db.rollback()

# 关闭数据库连接
db.close()