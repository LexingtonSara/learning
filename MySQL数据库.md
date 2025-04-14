DBMS数据库管理系统(Database Management System)
很多软件都能实现，比如MySQL、Oracle、SQL Server等。但MySQL是最流行的数据库管理系统。
1.安装MySQL,进行配置
2.内置客户端操作
查看当前所有的数据库：SHOW DATABASES;
创建数据库：CREATE DATABASE 数据库名 DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
create database mydb default character set utf8 collate utf8_general_ci;
删除数据库：DROP DATABASE 数据库名;
删除数据库：drop database mydb;
选择数据库：USE 数据库名;
显示当前选择的数据库：SELECT DATABASE();

创建表：
```create table tb3(
 id int primary key auto_increment not null,
 name varchar(16) not null,
 age int default 3
 )default charset=utf8;```
主键一般用于表示当前这条数据的id编号，主键只能有一个，不能重复。一般将主键和自增键结合使用。
```
CREATE TABLE 表名 (
    字段名1 数据类型1,#主键(不能为空,不能重复),自增键
    字段名2 数据类型2 not null,#本列数据不能为空
    字段名3 数据类型3 null,#本列数据可以为空
    ...
)default charset=utf8;
```
show tables;查看当前数据库中的所有表；
删除表：drop table 表名;
清空表：truncate table 表名;delete from 表名;
查看表结构：desc 表名;
修改表:
添加列：alter table 表名 add 字段名 数据类型;
删除列：alter table 表名 drop 字段名;
修改列：alter table 表名 modify 字段名 数据类型;
修改列名：alter table 表名 change 旧字段名 新字段名 数据类型;
添加主键：alter table 表名 add primary key(字段名);
删除主键：alter table 表名 drop primary key;

3.MySQL数据类型
MySQL支持的数据类型有：
int 整型 -2147483648~2147483647(-2^31~2^31-1)
int unsigned 无符号整型 0~4294967295(0~2^32-1)
int(M) zerofill 零填充整型,M表示总长度 
tinyint 1字节整型 -128~127
smallint 2字节整型 -32768~32767
mediumint 3字节整型 -8388608~8388607
bigint 8字节整型 -2^63~2^63-1
float 浮点型 4字节
double 浮点型 8字节
decimal 定点数 (10,2)最多10位,2位小数
char 定长字符串 最多255个字符
varchar 可变长字符串 最多65535个字节
text 长文本字符串 65535个字符 2^16-1个字符
mediumtext 中等长度文本字符串
longtext 长文本字符串 
enum 枚举类型
set 集合类型
binary 二进制字符串
varbinary 可变长二进制字符串
blob 二进制大对象
date 日期
time 时间
year 年份
datetime 日期时间  YYYY-MM-DD HH:MM:SS
timestamp 时间戳 1970-01-01 00:00:00 UTC+00:00~2038-01-19 03:14:07 UTC+00:00
geometry 几何数据类型
json JSON数据类型



```
import pymysql

# 连接数据库
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='Lexington9436', charset='utf8')
cursor = conn.cursor()

#查看数据库
cursor.execute("SHOW DATABASES")
result = cursor.fetchall()
print(result)

#创建数据库
cursor.execute("CREATE DATABASE mydb DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci")
conn.commit()#新增、删除、修改数据库后必须提交

#进入数据库,创建表
cursor.execute("USE mydb")
sql ="""
create table tb1(
    id int primary key auto_increment not null,
    title varchar(128) not null,
    content text not null,
    ctime datetime
)default charset=utf8;
"""
conn.commit()#新增、删除、修改数据库后必须提交

#查看表
cursor.execute("SHOW TABLES")
result = cursor.fetchall()
print(result)

#删除表
cursor.execute("DROP TABLE tb1")
conn.commit()

#清空表
cursor.execute("TRUNCATE TABLE tb1")
conn.commit()

#删除数据库
cursor.execute("DROP DATABASE mydb")
conn.commit()

# 关闭数据库连接
cursor.close()
conn.close()
```