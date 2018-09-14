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
4. 相同目录下就会生成dst.xml文件，文件内容即为所需要转换的格式

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