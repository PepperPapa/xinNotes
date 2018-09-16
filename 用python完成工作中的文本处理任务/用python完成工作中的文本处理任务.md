工作中经常遇到处理大量数据的情况，这些数据有一些显著的特点，数据量大、数据比较有规律，如果人工一条条的处理几乎不现实，而且吃力不讨好，严重消耗工作热情，如果懂点编程的话一切就会变的不一样，废话不多说，这里讲解一个我工作中实际遇到的使用python处理数据的一个例子，希望对你也有帮助。
## 数据处理诉求
我的工作主要是针对系统做性能测试，常常需要从数据库捞取大量数据，然后转换成需要的格式，比如，源数据格式内容如下（实际上有几十万行，这里仅作为示例）:
``` 
PAYQEITVX 20194385 02
PAYLGYKZH 01723465 02
PAYWLQVKD 70915382 05
PAYYPDHKI 32970614 03
```
这些数据需要加工成如下xml格式：
```
<?xml version="1.0" encoding="ISO-8859-1"?>
<items>
    <itemcode>
        <type>PAYQEITVX</type>
        <number>20194385</number>
        <reason>02</reason>
    </itemcode>
    <itemcode>
        <type>PAYLGYKZH</type>
        <number>01723465</number>
        <reason>02</reason>
    </itemcode>
    <itemcode>
        <type>PAYWLQVKD</type>
        <number>70915382</number>
        <reason>05</reason>
    </itemcode>
    <itemcode>
        <type>PAYYPDHKI</type>
        <number>32970614</number>
        <reason>03</reason>
    </itemcode>
</items>
```
## python实现
观察上节的内容我们发现要转换的数据的每一行以空格为分隔符分别对应xml中itemcode元素中的type、number、reason元素，所以我们实现的思路就是首先读取源数据到字符串，以换行符分割每一行形成一个列表，然后每一行再以空格进行分割提取其中的子项形成嵌套列表（也就是二维数组），接下来就可以根据下图中的对应关键去拼接成我们所需要的xml格式的文件了。
![转换示意图](./转换示意.png "转换示意图")
实现代码：
```
#! python3.7
"""
            transform.py
本代码实现将形如如下格式的数据

PAYQEITVX 20194385 02
PAYLGYKZH 01723465 02
PAYWLQVKD 70915382 05
PAYYPDHKI 32970614 03

转换为xml形式的数据

<?xml version="1.0" encoding="ISO-8859-1"?>
<items>
    <itemcode>
        <type>PAYQEITVX</type>
        <number>20194385</number>
        <reason>02</reason>
    </itemcode>
    <itemcode>
        <type>PAYLGYKZH</type>
        <number>01723465</number>
        <reason>02</reason>
    </itemcode>
    <itemcode>
        <type>PAYWLQVKD</type>
        <number>70915382</number>
        <reason>05</reason>
    </itemcode>
    <itemcode>
        <type>PAYYPDHKI</type>
        <number>32970614</number>
        <reason>03</reason>
    </itemcode>
</items>

执行步骤：
1. 将src.txt, transform.py创建在同一目录下
2. 将需要加工的数据复制到src.txt中
3. 打开cmd命令提示符cd到文件所在目录，执行命令python transform.py
4. 相同目录下就会生成dst.xml文件，文件内容即为成功转换后的内容

注：
为了示例尽量简单，代码实现未做异常错误处理
"""
src_file = open("src.txt")
#读取全部文本
src_items = src_file.read() 
src_file.close()
#根据换行符\n分割字符串生成列表
#['PAYQEITVX 20194385 02',
# 'PAYLGYKZH 01723465 02',
# 'PAYWLQVKD 70915382 05',
# 'PAYYPDHKI 32970614 03']
src_items = src_items.split('\n')
#每一行的字符串根据空格符进一步分割成嵌套列表
#[['PAYQEITVX', '20194385', '02'],
# ['PAYLGYKZH', '01723465', '02'],
# ['PAYWLQVKD', '70915382', '05'],
# ['PAYYPDHKI', '32970614' '03']]
for line in src_items:
    src_items[src_items.index(line)] = line.split()

# 根据提取的嵌套列表（二维数组）格式化为xml格式的字符串
dst_content = """<?xml version="1.0" encoding="ISO-8859-1"?>
<items>"""
# type number reason分别对应列表项的三个子项
# {0} {1} {2}为格式化字串的三个参数，分别使用type、number、reason进行替换
for type, number, reason in src_items:
    content = """
    <itemcode>
        <type>{0}</type>
        <number>{1}</number>
        <reason>{2}</reason>
    </itemcode>""".format(type, number, reason)
    dst_content += content
dst_content += "\n</items>"
# 将转换后的字符串写入文件
dst_file = open("dts.xml", 'w')
dst_file.write(dst_content)
dst_file.close()
```
## 总结
把学到的编程知识用于解决实际的问题，做到学以致用，这样带着目的去学习才是最高效的，也会持续得到正反馈，学习的热情才能持续。本文中的代码也可以通过我的[github](https://github.com/PepperPapa/xinNotes/tree/master/%E7%94%A8python%E5%AE%8C%E6%88%90%E5%B7%A5%E4%BD%9C%E4%B8%AD%E7%9A%84%E6%96%87%E6%9C%AC%E5%A4%84%E7%90%86%E4%BB%BB%E5%8A%A1)去下载。