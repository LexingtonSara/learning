DBMS数据库管理系统(Database Management System)
很多软件都能实现，比如MySQL、Oracle、SQL Server等。但MySQL是最流行的数据库管理系统。
1.安装MySQL,进行配置
2.内置客户端操作
查看当前所有的数据库：SHOW DATABASES;
创建数据库：CREATE DATABASE 数据库名 DEFAULT CHARASET utf8 COLLATE utf8_general_ci;
create database mydb default charset utf8 collate utf8_general_ci;
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
新增数据：insert into 表名(字段名1,字段名2,...) values(值1,值2,...);
删除数据：
delete from 表名;#删除所有数据
delete from 表名 where 条件;#删除指定条件的数据,可以用and或or连接多个条件
修改数据：
update 表名 set 字段名=新值;#修改该字段(列)所有数据
update 表名 set 字段名=新值 where 条件;#修改指定条件的数据,整型值可以加减,字符串值可以用concat函数拼接

查询数据：
select * from 表名;#查询表中所有数据
select 字段名1,字段名2 from 表名;#查询指定字段的数据
select 字段名1,字段名2 from 表名 where 条件;#查询指定条件的数据
select 字段名1,字段名2 as 别名 from 表名;#查询指定字段的数据并给其别名
select 字段名1,字段名2 from 表名 group by 字段名1;#分组查询
select 字段名1,字段名2 from 表名 order by 字段名1;#排序查询

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
cursor.execute("CREATE DATABASE mydb DEFAULT CHARASET utf8 ")
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

4.必备的SQL语句
4.1 条件
根据条件搜索数据：SELECT * FROM table_name WHERE condition;
条件包括：
=, >, <, >=, <=, !=, IS NULL, IS NOT NULL, 
IN, NOT IN, BETWEEN,
AND, OR, NOT,
EXISTS,NOT EXISTS,#子查询
LIKE, ALL, ANY, SOME
4.2通配符
一般用于模糊搜索，%表示任意字符，_表示一个字符
SELECT * FROM table_name WHERE column_name LIKE 'pattern';
数据量少可以使用, 数据量大时不推荐使用
4.3映射 指定列
SELECT column_name1, column_name2 FROM table_name;
SELECT column_name1, column_name2 FROM table_name WHERE condition;
4.4排序
先拿到结果再排序
SELECT * FROM table_name ORDER BY column_name1, column_name2 DESC;#降序
SELECT * FROM table_name ORDER BY column_name1, column_name2 ASC;#升序
select * from table_name order by id desc age asc;#先按id降序排列,id相同的按age升序排列
4.5取出部分数据
LIMIT 关键字
SELECT * FROM table_name LIMIT [offset,] row_count;
offset: 偏移量，从第几条开始取
row_count: 取多少条数据
select * from table_name limit 10;#取出前10条数据
select * from table_name limit 10,20;#取出10-20条数据
select * from table_name order by id desc limit 10;#取出id最大的10条数据
select * from table_name where id > 10 order by id desc limit 10;#取出id大于10的10条数据
select * from table_name limit 10 offset 20;#取出第21-30条数据#offset 显式指定偏移量和隐式的区别
4.6分组
GROUP BY 关键字
select age, count(*) as num from table_name group by age;#按年龄分组,统计每个年龄的人数
select age,max(id),min(id),sum(id),count(id),avg(id) from table_name group by age;#按年龄分组,统计每个年龄的最大、最小、和、平均值、数量
分组之后进行条件查询,不能使用where关键字,而是使用having关键字



4.7左右表连接
JOIN 关键字
select * from table1 join table2 on table1.id = table2.id;#左右连接
select * from table1 left join table2 on table1.id = table2.id;#左连接
select * from table1 right join table2 on table1.id = table2.id;#右连接
select * from table1 inner join table2 on table1.id = table2.id;#内连接
select * from table1 full join table2 on table1.id = table2.id;#全连接

优先级:
JOIN > ON > WHERE > GROUP BY > HAVING > ORDER BY > LIMIT

4.8联合union
UNION 关键字
select * from table1 union select * from table2;#合并两个表的所有数据,列数需要一致,自动去重
select * from table1 union all select * from table2;#合并两个表的所有数据,列数需要一致,不去重

5.表关系
单表：一个表就是一个关系,单独一张表就能保存所有的数据
一对多:需要两张表来存储信息,两张表存在一对多或者多对一的关系
多对多:需要三张表来存储信息,两张单表+关系表,关系表中存储两张表的关系，创造出两个单表之间的多对多关系

外键：
外键是用于两个表之间建立联系的列，它是参照完整性的一种约束。
外键的作用：
    1.保证数据的一致性2.简化数据处理3.提高查询效率

添加外键：
alter table table1 add constraint fk_name foreign key(column_name) references table2(column_name);
删除外键：
alter table table1 drop foreign key fk_name;

6.授权与权限
root用户默认拥有所有权限，普通用户默认没有权限，需要授权才能使用。

创建用户：
create user '用户名'@'IP地址' identified by '密码';
删除用户：
drop user '用户名'@'IP地址';
授权：
grant 权限列表 on 数据库.表 to '用户名'@'IP地址';
什么样的权限可以授予,权限的作用范围(数据库、表、列),权限的作用账户
查看权限：
show grants for '用户名'@'IP地址';
删除权限：
revoke 权限列表 on 数据库.表 from '用户名'@'IP地址';

数据库导出导入：
导出：
mysqldump -u用户名 -p密码 数据库名 > 导出文件名.sql
导入：
mysql -u用户名 -p密码 数据库名 < 导入文件名.sql

7.索引
mysql索引是一种数据结构,用于加快数据库查询的速度和性能。
索引分单列索引和组合索引。单列索引:一个索引只包含单个列,一个表可以有多个单列索引。组合索引:一个索引包含多个列,一个表可以有多个组合索引。
索引也是一张表,该表保存了主键和索引字段,并指向实体表的对应记录。
创建索引时,确保该索引应用在SQL查询语句的WHERE子句中,避免索引失效。
索引需要占用额外的存储空间,对表进行插入、更新、删除时,索引也要动态维护。
数据库中索引最核心的作用是加速查找
7.1索引的原理
以id为例子创建索引：二叉搜索树,log(n)时间复杂度

B+ 树由根节点、中间节点和叶子节点构成,其中叶子节点用来保存排序后的数据.由于记录在索引上是排序过的,因此在一个叶子节点内查找数据时可以使用二分查找,这种查找方式效率非常的高.当数据很少的时候,B+ 树只有一个根节点,数据也就保存在根节点上.随着记录越来越多,B+ 树会发生分裂,根节点不再保存数据,而是提供了访问下一层节点的指针,帮助快速确定数据在哪个叶子节点上.

聚簇索引：聚簇索引是一种索引类型,它将数据和索引保存在同一个B+ 树中,数据记录的物理位置与键值的逻辑位置相同,这就保证了数据的顺序性.聚簇索引的好处是数据访问更快,因为索引和数据保存在一起,可以直接访问,而非二分查找.
非聚簇索引：非聚簇索引是一种索引类型,它将数据保存在一个索引表中,索引表中的索引字段指向数据表的主键字段,这样索引和数据就分开了,索引表的主键就是数据表的主键.非聚簇索引的好处是索引的维护更简单,因为索引表中的数据量小于数据表,索引的维护只需要更新索引表中的数据,而数据表中的数据更新不需要更新索引表.

在创建二维表时,通常会为表指定主键列,主键列上会默认创建索引,对于MyAQL InnoDB引擎,主键上的索引就是整张表的数据,因此主键索引就是聚簇索引.一张表只能有一个聚簇索引,我们自己创建的索引都是二级索引,也叫做非聚簇索引.

7.2常见索引
主键索引：主键索引是一种特殊的索引,它唯一标识表中的每一行,每张表都应该有主键索引。
主键索引的创建,推荐使用自增主键。
加速查找、不能为空、不能重复.
primary key (id) #如果有多列,则用逗号分隔,称为联合主键
创建主键索引：alter table table_name add primary key(column_name);
删除主键索引：alter table table_name drop primary key;
如果主键索引自增,则使用alter table table_name change old_column_name new_column_name int not null;


唯一索引：唯一索引是一种索引,它保证表中的每一行的列值唯一,但允许有空值。
唯一索引的创建,推荐使用唯一列或组合列。
加速查找、不能重复,只允许一个空值。
unique key (column_name)
多个唯一索引:每个唯一索引都对应一个唯一的列,每列中不能有重复值。
联合唯一索引：alter table table_name add unique key(column_name1,column_name2);多个列联合构成一个索引,共同构成的值不能重复。


普通索引：普通索引是一种索引,它帮助mysql高效地找到满足查询条件的数据行,但不唯一,允许有空值。
普通索引的创建,推荐使用较长的列或较少的列。
加速查找、允许空值。
index key (column_name)
多个普通索引:每个普通索引都对应一个普通的列,每列中可以有重复值。
联合普通索引：alter table table_name add index key(column_name1,column_name2);多个列联合构成一个索引,共同构成的值可以重复。