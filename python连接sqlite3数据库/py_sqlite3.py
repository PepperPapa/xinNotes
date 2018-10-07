# python3.7
import sqlite3

# 创建并连接数据库py_demo.db
conn = sqlite3.connect("py_demo.db3")

# 创建游标
cur = conn.cursor()

# 通过cur.execute执行sql语句，操作数据库
# 1.创建表demo
cur.execute("""
    create table demo (id INT not null, name varchar(20));
""")

# 2.插入数据到表demo
cur.execute("insert into demo (id, name) values (1, 'richard');")
cur.execute("insert into demo (id, name) values (2, 'bluce');")
cur.execute("insert into demo (id, name) values (3, 'grace');")
cur.execute("insert into demo (id, name) values (4, 'jhon');")
cur.execute("insert into demo (id, name) values (5, 'nio');")

# 3.查询表
cur.execute("""
select * from demo;
""")
print(cur.fetchall())   # 打印所有的查询的结果

# 提交修改
conn.commit()

# 关闭数据库连接
conn.close()
